---
{
  "schema_version": "1.0",
  "id": "CHG-20261012",
  "title": "Revise prompt design, RQ3 and concise results",
  "status": "verifying",
  "risk": "L2",
  "created_at": "2026-10-12",
  "updated_at": "2026-10-12",
  "source": {
    "type": "user",
    "reference": "Author request of 2026-10-12"
  },
  "related_specs": [
    "SPEC-20261012"
  ],
  "related_adrs": [],
  "related_issues": [],
  "related_prs": [],
  "commits": []
}
---

# Prompt comparison and manuscript compression

## Outcome and scope
Replace external-benchmark RQ3, explain prompt structure in Design, distinguish
benchmark instances/evaluation from their generator, report the archived prompt
comparisons, and retain essentials within ten pages including references.

## Invariants and non-goals
Keep the original RQ1/RQ2 scores, independent answer/path scoring, task-family
partition and author's style. Raw experiment directories remain read-only.
Preserve the existing main.tex edit and untracked analyse.md/t.txt. No new runs,
external publication, invented scores or changes to the benchmark algorithm.

## Assumptions, risks and decisions
Gemma v4 is incomplete: use the 11,824-question common support as marked
provisional values in an otherwise completed comparison narrative. Qwen3.6
compares 46,656 identical questions but simultaneously doubles the budget.
Qwen3.8 v1/v4 compares 216 difficult questions at budget 16,384. Scores retain
non-responses; do not claim a causal prompt effect or generalized model ranking.
Remove bulky appendices from the ten-page build but retain their source files
and machine-readable diagnostic exports. Preserve concise definitions in prose.

## Proof obligations and verification
Recompute primary counts from embedded dashboard data, check common support
and Java/question identity, retain source hashes, regenerate comparison table,
compile LaTeX, check page count and references, inspect layout and task-only diff,
validate knowledge records. Executed evidence is recorded in
`data/prompt_comparison/VALIDATION.md`: three common-support comparisons
reproduce the archived counts, all 1,232 Java classes and question files match,
the original 12 generated tables/figures are unchanged, and the eight-page PDF
compiles with resolved references and no overfull boxes. Prompt and RQ3 pages
were inspected visually. Current knowledge records and whitespace checks pass.

## Rollback and residual work
Revert task-owned commits to restore the prior manuscript. Replace provisional
Gemma figures once the full run is available; that future experiment is outside
this editorial revision. Completion and commit evidence will be recorded below.
