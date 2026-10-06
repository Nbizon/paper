# ReachabilityBench paper

LaTeX sources for *ReachabilityBench: Diagnosing LLMs on Controlled Java
Method-Reachability Tasks*. The current Results section analyzes the supplied
Gemma-4-26B-A4B-it and Qwen3.6-35B-A3B experiment:

- 46,656 shared questions per model, from 1,232 Java classes;
- unguarded: `nb_if = 0`, 11,664 questions per model;
- condition-aware: `nb_if ∈ {1, 3, 5}`, 34,992 questions per model;
- balanced polarities and factorial grid; one requested reasoning budget (16,384);
- independent final-answer and executable-path correctness, retaining non-responses.

The archived `n_if`/`if` field corresponds to `nb_if` in the manuscript. The old
`variant`/generator-mode metadata does not select the analysis family. The author's
2026-10-06 instruction supersedes the previous family interpretation.

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The wrapper uses `IEEEtran`, BibTeX, TikZ and PGFPlots. Figures are native vectors;
no Python plotting dependency or external image is needed to build.
The inclusion switches in `main.tex` control which manuscript sections appear.

The shared figure style is defined in `figures/styles.tex`. Diagrams use aligned
neutral boxes and uniform arrow weights; query examples are separate from call
edges. Result plots use a common 0–100% scale, labeled axes and visual legends.
Gemma uses orange circles and Qwen blue squares; solid lines show answer scores
and dashed lines path scores. Marker shapes also distinguish models in grayscale.
Edit result plots through `scripts/render_results.py` and regenerate them.

## Reproduce the results

From this repository, with the supplied experiment archive available:

```bash
python3 scripts/aggregate_results.py \
  --results-root /home/nbizon/Thèse/Projects/results/last_exp
python3 scripts/render_results.py
python3 scripts/render_results.py --check
```

The scripts use only the Python standard library. The archive and presentation
are read-only inputs. `--output PATH` selects an alternative aggregate directory;
rendering uses the repository's canonical `data/results/aggregates.csv`.

The aggregator verifies that both models received the same queries and checks
primary scores in every joint factor/polarity cell against corrected CSVs. It
exports metric units, numerators, denominators, eligible counts and exclusions,
plus SHA-256 source hashes. The renderer produces the manuscript's result tables
and appendix figures; `--check` detects generated drift.

Diagnostics have distinct populations. T01 and D1/D3/D5 are ratios of sums;
T04/T13 and D9 are means of per-question quantities. D5 means no attributed error
in an exposed guard, not proof of correct internal condition evaluation.
D1* uses the attribution population shared by D3/D5. Literal conditions and
unresolved origins are excluded from origin-distance metrics. The analysis is
descriptive; shared Java classes are not independent replications.

See [validation](data/results/VALIDATION.md),
[bibliographic verification](bibliography/verification.md), and
[source provenance](data/results/provenance.json). External scores are vendor
reports under other protocols, not runs added to this experiment.

## Revision requirements

The current author instruction is captured in
[the results specification](docs/product-specs/SPEC-20261006-results.md) and
[its change record](docs/changes/CHG-20261006-results.md).
`specifications.md` retains historical requirements and their supersession.
The derived index is regenerated and checked with:

```bash
python3 scripts/check_knowledge.py --write-index
python3 scripts/check_knowledge.py
```
