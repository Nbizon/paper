# Revision validation — 2026-10-06

## Data and derived output

Executed `scripts/aggregate_results.py` against the supplied `last_exp` archive.
It verified 46,656 records and 1,232 Java classes per model, identical query
multisets, balanced polarities, four questions per signed-distance factorial
cell, successful inference status, and one requested reasoning budget.

The new partition contains 11,664 unguarded (`nb_if=0`) and 34,992
condition-aware (`nb_if>0`) questions per model. Primary answer/path outcome
counts match the corrected executable-graph CSVs in every joint
factor/polarity cell. This checks aggregation against existing scored outputs;
it does not independently regenerate or validate the graph oracle.

Re-ran aggregation into `/tmp/reachability-aggregate-check`: all three exported
files match the canonical exports byte for byte (5,676 aggregate rows).
The attributable D1 population partitions into D3 and D5. Diagnostic units,
eligible populations, exclusions, numerators and denominators are retained.
Source hashes are recorded in `provenance.json`.

Executed `scripts/render_results.py --check`: all nine generated tables and
three appendix figures match their source aggregates. Results prose was
checked against the corresponding strata, including joint guard/parameter
contrasts, polarity reversals, and target-directed guard-error associations.

## Manuscript and references

Executed `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
The current included manuscript compiles. All 18 bibliography entries are
cited and resolve; the final logs contain no undefined citations/references,
BibTeX missing-entry warnings, errors, or overfull boxes. Remaining underfull
boxes concern justified text/table or float layout, without clipping.

Visually inspected the compiled setup/results, diagnostic tables, appendix
figures, external comparison and bibliography. Figures are native vector
TikZ, with consistent colors, units and captions. Appendix floats are flushed
and full-height columns restored before the bibliography. Reference metadata
and associated claims were checked against primary sources; see
`bibliography/verification.md` for the individual audit and source links.

Executed `git diff --check` and `scripts/check_knowledge.py`; the current
CHG/SPEC references and generated index are valid. The knowledge check also
verifies implementation SHAs when completion states are recorded.

## Scope of the evidence

No new model runs, scoring changes, significance tests, or causal
interventions were performed. Diagnostics describe output-conditioned
associations, not private model reasoning. External benchmark scores are
vendor reports under different protocols. Named checkpoints are not pinned
to immutable revisions in the supplied logs. Existing `main.tex` changes and
the untracked `t.txt` are preserved and excluded from task commits; manuscript
section inclusion switches are unchanged.

## Contribution-focused editorial revision — 2026-10-12

The manuscript now consistently calls the archived path-correctness measure
"trace correctness": the output is an ordered exploration, while "path" remains
the graph-theoretic term. The internal metric keys and all scoring rules remain
unchanged. Both renderers were updated before regenerating the tables and plots.

- render_results.py --check: all 12 generated tables/figures match.
- aggregate_prompt_comparison.py --results-root /home/nbizon/Thèse/Projects/results
  --check: the summary and comparison table match.
- Numeric tokens in all edited generated score tables and result plots, and
  in Results prose, match their previous committed versions exactly.
  aggregates.csv and data/prompt_comparison/summary.json are unchanged.
- check_knowledge.py: six current records and their index validate.
- latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex: successful
  ten-page build, with no undefined references/citations or overfull boxes.
- PDF text contains no unresolved reference markers. Pages 1 and 9 were
  visually inspected for contribution wording, the comparison table and
  the revised conclusion.

The editorial change adds no new experiment or effectiveness claim.
