#!/usr/bin/env python3
"""Reproduce paper aggregates from a dashboard, checked against scored CSVs.

The dashboard is parsed as data; no JavaScript or external code is executed.
Only the output directory is written. Uses the Python standard library.
"""

import argparse
import base64
from collections import Counter, defaultdict
import csv
import gzip
import hashlib
import json
import math
from pathlib import Path
import re


FACTORS = ("context", "comment", "var", "loop", "if", "param", "distance")


def number(value):
    return isinstance(value, (int, float)) and math.isfinite(value)


def integer(value):
    return number(value) and value >= 0 and int(value) == value


def quantile(values, fraction):
    if not values:
        return None
    values = sorted(values)
    index = (len(values) - 1) * fraction
    low, high = math.floor(index), math.ceil(index)
    return values[low] + (values[high] - values[low]) * (index - low)


def summarize(records, definitions):
    results = {}
    executed = [r for r in records if r["inference_status"] == "OK"]

    def put(key, numerator, denominator, eligible, unit, value=None, **extra):
        results[key] = dict(
            value=value if value is not None else numerator / denominator if denominator else None,
            numerator=numerator, denominator=denominator, eligible=eligible,
            excluded=len(records) - eligible, unit=unit, **extra,
        )

    for key, field in (("answer", "correctness_answer"), ("path", "correctness_path")):
        # This frozen experiment contains no NOT_EVALUATED or infrastructure failures.
        assert all(r[field] in {"TRUE", "FALSE", "NO_RESPONSE"} for r in records)
        put(key, sum(r[field] == "TRUE" for r in records), len(records), len(records), "fraction")
    put("nr", sum(r["correctness_answer"] == "NO_RESPONSE" for r in executed),
        len(executed), len(executed), "fraction")
    for key, predicate in (
        ("answer_without_path", lambda r: r["correctness_answer"] == "TRUE" and r["correctness_path"] != "TRUE"),
        ("joint_correct", lambda r: r["correctness_answer"] == r["correctness_path"] == "TRUE"),
    ):
        put(key, sum(predicate(r) for r in records), len(records), len(records), "fraction")

    for metric in definitions:
        key, kind = metric["key"], metric["kind"]
        unit = metric.get("scale", "fraction")
        if kind == "difficulty_mean":
            count, total = metric["countColumn"], metric["sumColumn"]
            rows = [r for r in executed if integer(r[count]) and r[count] > 0
                    and number(r[total]) and r[total] >= 0]
            put(key, sum(r[total] for r in rows), sum(r[count] for r in rows), len(rows), unit)
        elif kind in {"t01", "target_bad_if_share", "target_bad_if_case_incidence", "target_bad_if_exposure_share"}:
            rows = [r for r in executed if integer(r["misjudged_if_count"])]
            if kind in {"t01", "target_bad_if_exposure_share"}:
                rows = [r for r in rows if integer(r["trace_call_guard_count"])
                        and r["trace_call_guard_count"] > 0
                        and r["misjudged_if_count"] <= r["trace_call_guard_count"]]
            if kind != "t01":
                rows = [r for r in rows if integer(r["target_reachable_misjudged_if_count"])
                        and r["target_reachable_misjudged_if_count"] <= r["misjudged_if_count"]]
            numerator = sum(
                r["misjudged_if_count"] if kind == "t01" else
                int(r["target_reachable_misjudged_if_count"] > 0) if kind == "target_bad_if_case_incidence" else
                r["target_reachable_misjudged_if_count"] for r in rows)
            denominator = (
                sum(r["trace_call_guard_count"] for r in rows) if kind in {"t01", "target_bad_if_exposure_share"} else
                sum(r["misjudged_if_count"] for r in rows) if kind == "target_bad_if_share" else len(rows))
            put(key, numerator, denominator, len(rows), unit)
        else:
            field = metric["column"]
            rows = [r for r in executed if number(r[field])
                    and (key not in {"t02", "t11"} or r["path_length"] > 0)]
            values = [r[field] for r in rows]
            if kind == "quartiles":
                results[key] = dict(value=quantile(values, .5), q1=quantile(values, .25),
                                    q3=quantile(values, .75), numerator=None, denominator=None,
                                    eligible=len(rows), excluded=len(records) - len(rows), unit=unit)
            else:
                numerator = sum(v > 0 for v in values) if kind in {"incidence", "boolean"} else sum(values)
                put(key, numerator, len(rows), len(rows), unit)
    # Compare error and non-error difficulty using the same attributable
    # exposures. Unrestricted D1 includes ambiguous traces excluded by D3/D5.
    attributable = [r for r in executed if all(integer(r[c]) for c in (
        "if_difficulty_count", "misjudged_if_difficulty_count", "correct_if_difficulty_count"))
        and r["if_difficulty_count"] > 0]
    assert all(r["if_difficulty_count"] == r["misjudged_if_difficulty_count"]
               + r["correct_if_difficulty_count"] for r in attributable)
    put("if_difficulty_attributable", sum(r["if_difficulty_sum"] for r in attributable),
        sum(r["if_difficulty_count"] for r in attributable), len(attributable), "count")
    negatives = [r for r in executed if r["expected_truth"] == "False"
                 and integer(r["target_reachable_misjudged_if_count"])]
    for key, subset in (
        ("false_positive_with_target_guard_error", [r for r in negatives if r["target_reachable_misjudged_if_count"] > 0]),
        ("false_positive_without_target_guard_error", [r for r in negatives if r["target_reachable_misjudged_if_count"] == 0]),
    ):
        put(key, sum(r["answer_outcome"] == "FALSE_POSITIVE" for r in subset),
            len(subset), len(subset), "fraction")
    return results


def signature(row, field):
    return tuple(str(row[k]) for k in FACTORS + ("source", "target", "expected_truth")) + (row[field],)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-root", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "data/results")
    args = parser.parse_args()
    dashboard = args.results_root / "dashboards/nouvelles_metriques.html"
    html = dashboard.read_text()
    payload = json.loads(re.search(r'<script id="embedded-results" type="application/json">(.*?)</script>', html, re.S).group(1))
    definitions = json.loads(re.search(r'const SYNTHESIS_METRICS = (\[.*?\]);', html, re.S).group(1))
    assert payload["encoding"] == "gzip-base64-columnar-json"
    aggregates, checks = [], []
    question_sets = []
    for model in payload["models"]:
        data = json.loads(gzip.decompress(base64.b64decode(model["data"])))
        columns, dictionaries = data["columns"], data["dictionaries"]
        records = [{k: dictionaries[k][v[i]] if k in dictionaries and v[i] is not None else v[i]
                    for k, v in columns.items()} for i in range(data["rows"])]
        assert len(records) == 46656
        assert len({r["case"] for r in records}) == 1232
        assert {r["if"] for r in records} == {0, 1, 3, 5}
        assert {r["reasoning_budget"] for r in records} == {16384}
        assert all(r["inference_status"] == "OK" for r in records)
        source = args.results_root / "result_analysis_executable_graph" / model["name"] / "stats.csv"
        with source.open(newline="") as handle:
            scored = list(csv.DictReader(handle))
        assert len(scored) == len(records)
        # The dashboard omits method names. Verify both metrics in every joint
        # factor/polarity cell against CSV, then verify model query sets directly.
        for field in ("correctness_answer", "correctness_path"):
            keys = FACTORS + ("expected_truth",)
            assert Counter(tuple(str(r[k]) for k in keys) + (r[field],) for r in records) == Counter(
                tuple(r[k] for k in keys) + (r[field],) for r in scored)
        question_sets.append(Counter(signature(r, "expected_truth") for r in scored))
        checks.append(dict(model=model["name"], source=str(source.relative_to(args.results_root)),
                           sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                           status="primary metrics agree in every joint factor/polarity cell"))
        for r in records:
            r["abs_distance"] = abs(r["distance"])
            for field in ("if", "param", "context"):
                r[field + "_truth"] = f'{r[field]}:{r["expected_truth"]}'
            r["if_param"] = f'{r["if"]}:{r["param"]}'
        for group, rows in (
            ("all", records), ("unguarded", [r for r in records if r["if"] == 0]),
            ("condition", [r for r in records if r["if"] > 0]),
        ):
            assert len(rows) == {"all": 46656, "unguarded": 11664, "condition": 34992}[group]
            assert sum(r["expected_truth"] == "True" for r in rows) * 2 == len(rows)
            # Four queries per signed distance per factorial cell.
            assert set(Counter(tuple(r[k] for k in FACTORS) for r in rows).values()) == {4}
            factors = ("overall", "expected_truth")
            if group == "all":
                factors += ("if", "if_param", "if_truth")
            if group == "condition":
                factors += ("context", "param", "comment", "var", "loop", "distance", "abs_distance",
                            "context_truth", "param_truth")
            for factor in factors:
                groups = defaultdict(list)
                for row in rows:
                    groups[str(row[factor]) if factor != "overall" else "all"].append(row)
                for level, subset in sorted(groups.items()):
                    for metric, stats in summarize(subset, definitions).items():
                        aggregates.append(dict(model=model["name"], group=group, factor=factor,
                                               level=level, metric=metric, **stats))
    assert len(question_sets) == 2 and question_sets[0] == question_sets[1]
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "aggregates.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(aggregates[0]) + ["q1", "q3"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(aggregates)
    (args.output / "metric_definitions.json").write_text(json.dumps(definitions, ensure_ascii=False, indent=2) + "\n")
    provenance = dict(
        source_root=str(args.results_root), dashboard="dashboards/nouvelles_metriques.html",
        dashboard_sha256=hashlib.sha256(dashboard.read_bytes()).hexdigest(),
        groups={"unguarded": [0], "condition": [1, 3, 5]}, checks=checks,
        queries_match=True, grid_balanced=True,
        generator="python3 scripts/aggregate_results.py --results-root PATH",
        interpretation="Diagnostics retain their eligibility; repeated guard exposures are occurrence weighted. No causal estimates.",
    )
    (args.output / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(f"Verified two models, 46,656 identical queries each; exported {len(aggregates)} aggregate rows.")


if __name__ == "__main__":
    main()
