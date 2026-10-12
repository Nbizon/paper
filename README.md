# ReachabilityBench paper

LaTeX sources for *ReachabilityBench: Diagnosing LLMs on Controlled Java
Method-Reachability Tasks*. ReachabilityBench names the final generated dataset of classes, questions, labels
and executable-graph oracles. The configurable construction algorithm produces
that dataset. Validation covers the complete final benchmark used for evaluation.

The main structural and trace analyses use the supplied
Gemma-4-26B-A4B-it and Qwen3.6-35B-A3B `last_exp` experiment:

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
The ten-page version excludes the extensive experimental appendix, whose
sources and diagnostic exports remain available in this repository.

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

## Prompt-context comparison (2026-10-12)

RQ3 compares ReachabilityBench (CO: Class-only, archived v1) with
ReachabilityBench (EE: Explicit execution, archived v4). These are two prompting
variants of the same generated dataset: TheClass programs, questions, labels
and executable-graph oracles are identical. CO leaves the entry point and the
deterministic execution assumptions implicit, adding the need to infer the
intended invocation context. EE supplies Main and explicitly states that all
relevant values and execution outcomes are determined by the code. Prompt structure is described in Design. The main Qwen3.6 comparison
covers 46,656 common questions; Gemma's provisional figures cover 11,824 common
questions, rather than the full grid. These comparisons also change the requested
reasoning budget from 16,384 to 32,768. The complementary Qwen3.8-Flash-Next
comparison uses 216 difficult questions at a fixed requested budget of 16,384.

Validation of the final dataset is presented with the evaluation set; scoring
rules are presented with response parsing and metrics. The Discussion compares
all three models on the same 216 difficult questions and reports reconstructed
input and reasoning token counts. EE has a larger budget to accommodate longer
execution analysis; observed mean consumption is not twice that of CO. Token
counts and difficult-subset scores are retained in the same summary.

Reproduce the comparison counts, token summaries, source hashes, and manuscript table:

```bash
python3 scripts/aggregate_prompt_comparison.py \
  --results-root /home/nbizon/Thèse/Projects/results
python3 scripts/aggregate_prompt_comparison.py \
  --results-root /home/nbizon/Thèse/Projects/results --check
```

Gemma prose and the table are ready for final figures; replace the provisional
comparison support when the complete results arrive. The aggregate script accepts
up to 46,656 Gemma questions and regenerates its denominator and scores. Then
update the corresponding prose and remove the provisional annotation. Do not use
subset scores as full-grid estimates. See
[validation](data/prompt_comparison/VALIDATION.md),
[revision specification](docs/product-specs/SPEC-20261012-prompt-comparison.md), and
[change record](docs/changes/CHG-20261012-prompt-comparison.md).

## Verified construction and Figure 1

The Design section is checked against the supplied versioned construction code.
An independent rooted Java audit verifies all 1,232 classes and all 46,656
labels of the final ReachabilityBench dataset used in the main evaluation. Signed distances are reference DFS target positions for positive queries
and source-reachable region sizes minus one for negative queries. See
[construction evidence](data/design/VALIDATION.md).

Figure 1 now contains a complete four-method program produced by that generator;
no call or guard is removed. Its sources and reproduction command are in
[examples/design](examples/design/README.md). The diagram distinguishes methods
executed elsewhere from methods reachable from the selected source.
