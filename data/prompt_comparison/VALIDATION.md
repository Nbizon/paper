# Prompt comparison validation

Verified on 2026-10-12. Raw experiment archives were read-only inputs.

## Scope and provenance

`summary.json` records SHA-256 hashes of the three source dashboards, numerators,
denominators, class counts, requested budgets, and polarity/family summaries.
The extractor reads compressed columnar JSON; it executes no dashboard JavaScript.
It checks identical case/factor/distance/polarity support within each comparison,
executed status and score vocabulary, and retains non-responses as incorrect.
A separate byte/hash comparison confirmed identical `TheClass.java` and question
files in all 1,232 cases of `last_exp/dataset` and `last_exp_7/dataset`.
The instruction/code boundary and Main inclusion were inspected directly in
system.txt from both datasets and from last_exp_6.

## Executed checks

- `python3 scripts/aggregate_prompt_comparison.py --results-root /home/nbizon/Thèse/Projects/results`:
  extracted the Qwen3.6 full comparison (46,656 questions per version), Gemma
  common subset (11,824), and Qwen3.8 v1/v4 subset (216).
- The same command with `--check`: generated JSON and table match exactly.
- A separate calculation against `last_exp_7/dashboard/comparison_support.json`
  confirmed both answer/path percentages for Qwen3.6 and Gemma (tolerance 1e-10).
- Qwen3.8 v1/v4 answer counts: 124/216 and 138/216; path counts: 77/216 and
  101/216; non-responses: 23 and 42. Negative answer counts: 26/108 and 50/108;
  negative path counts: 0/108 and 19/108. Positive answer counts: 98/108 and
  88/108; positive path counts: 77/108 and 82/108.
- `python3 scripts/render_results.py --check`: all 12 original generated
  tables/figures match the preserved main experiment aggregates.
- `latexmk -pdf -outdir=/tmp/paper-review-build -interaction=nonstopmode -halt-on-error main.tex`:
  compiled successfully, including BibTeX. The final PDF has eight pages,
  references included; no undefined reference/citation or overfull box.
  Building in a separate directory avoids interference with editor builds.
- `pdfinfo` and `pdftotext -layout`: eight pages and no unresolved `??` markers.
  Rendered pages 4 and 6 were visually inspected for prompt prose, tables,
  RQ3, and column fit.
- `python3 scripts/check_knowledge.py --write-index` and the same command
  without the flag: current records and generated index validate.
- Task-owned diffs reviewed; pre-existing main.tex whitespace change and
  untracked analyse.md/t.txt preserved outside the task commits.

## Interpretation and pending experimental data

Qwen3.6 and Gemma compare v1/budget 16,384 with v4/budget 32,768. The difference
cannot be attributed solely to prompting. Gemma's provisional common subset is
unbalanced and cannot stand in for the full factorial grid. Its measured values
are marked in the manuscript and can be replaced when the complete run arrives;
no missing experiment results have been fabricated. The manuscript already has
complete comparison prose rather than an empty Results subsection.

Qwen3.8 uses 216 questions from six classes, all with five guards and two
parameters, at requested budget 16,384 for both prompts. Scores are descriptive
and specific to this difficult subset. The comparison changes entry context
and determinism together; it does not separate their effects. Repeated inference
variability and independent instrumented oracle validation were not evaluated.
