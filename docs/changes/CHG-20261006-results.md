---
{
  "schema_version": "1.0",
  "id": "CHG-20261006",
  "title": "Reproduce and explain the updated reachability results",
  "status": "verifying",
  "risk": "L2",
  "created_at": "2026-10-06",
  "updated_at": "2026-10-06",
  "source": {
    "type": "user",
    "reference": "Author request of 2026-10-06"
  },
  "related_specs": [
    "SPEC-20261006"
  ],
  "related_adrs": [],
  "related_issues": [],
  "related_prs": [],
  "commits": []
}
---

# Updated reachability results

## Outcome and current observation
The manuscript and its reproducible aggregates must follow the author's revised
family definition and explain the two models' results using executable-graph
scores and eligible trace diagnostics. The previous draft groups all records
as condition-aware and does not examine value-origin distance.

## Scope, invariants and non-goals
- Revise definitions, setup, results, supporting tables/appendix, and references.
- Add a standard-library-only aggregation script and source hashes.
- Keep raw results and the presentation read-only; never rescore or invent runs.
- Preserve pre-existing edits in main.tex and the untracked t.txt.
- Do not push, publish, change benchmark generation, or claim causal identification.

## Assumptions and risks
The supplied dashboard is a diagnostic export, not an independent experiment.
Primary scores must agree with the corrected CSVs. Diagnostics have different
eligible populations and aggregation units; treating them as interchangeable
would misstate the explanation. Generated questions share Java classes.

## Decisions and change summary
Use nb_if=0 for unguarded and nb_if>0 for condition-aware. Preserve historical
mode metadata only as provenance. Compare D3/D5 against observed exposure D1;
D9 is a question-weighted reference, not the same estimand. Distinguish measured
trace errors from hypotheses about model computation. Verify external claims
against papers, proceedings, and official model cards.

## Proof obligations
- Recomputed scores and joint strata agree with executable-graph CSVs.
- Counts, balance, units, exclusions, and source hashes are retained.
- Tables and appendix figures reproduce the exported aggregates.
- Citations resolve and source-backed claims match the cited documents.
- LaTeX compiles; no missing reference or citation remains.

## Verification executed
Aggregation reproduced 5,676 rows and matched corrected scores in every
joint factor/polarity cell; an independent output directory matched byte for
byte. Generated tables/figures, all 18 cited entries, LaTeX compilation, visual
layout, whitespace and current knowledge/index checks passed. Details and
limits are recorded in data/results/VALIDATION.md and bibliography/verification.md.

## Rollback and residual uncertainty
Revert task-owned local commits to restore the previous manuscript. Results
remain specific to two checkpoints, one dataset and one inference configuration;
trace diagnostics cannot identify private reasoning or causal mechanisms.

## Completion
Verified before implementation commit. Implementation/evidence SHA and final
traceability closure are pending.
