---
{
  "schema_version": "1.0",
  "id": "CHG-20261012-design",
  "title": "Audit and revise construction design and Figure 1",
  "status": "completed",
  "risk": "L2",
  "created_at": "2026-10-12",
  "updated_at": "2026-10-12",
  "source": {
    "type": "user",
    "reference": "Author request to verify the supplied code_generation directory"
  },
  "related_specs": [
    "SPEC-20261012-design"
  ],
  "related_adrs": [],
  "related_issues": [],
  "related_prs": [],
  "commits": [
    "1ecad1ab212fcc18ba68f54fde5eafca74277deb"
  ]
}
---

# Construction audit and manuscript revision

## Outcome and scope
Revise Section IV and its pipeline/local-rule figures from the inspected generator;
replace the adapted Figure 1 with a complete generated illustration. Correct the
necessary distance interpretation in Results and oracle-validation statement in
Threats. Preserve all numerical scores, task families, prompts v1/v4, the author's
style, and the maximum ten-page manuscript.

## Evidence, assumptions and decisions
The supplied generator is revision b412bd7; its schema 3.0 and current prompt are
not the exact historical archive version. Distinguish their shared mechanism from
unknown historical seed/revision. Configured locals exclude additional argument
helpers; loop blocks contain no benchmark calls. Recorded executable children
are collected during Java emission, not inferred from all visible calls.
All 46,656 archived distances match source-first DFS target position (positive)
or source-reachable size minus one (negative). Remove the incorrect shortcut
explanation. Rerun the independent rooted semantic audit on read-only archives.
Generate a four-method illustration with seed 192, preserving source tokens and
all calls/guards; this small program is not added to the experimental corpus.

## Invariants and non-goals
External generator and archives are read-only. Do not modify raw scores, run LLM
inference, alter the generator, or publish. Pre-existing main.tex/introduction
edits and untracked analyse.md/t.txt stay outside task commits.

## Proof obligations
Source-to-prose mapping with hashes; generator checks; archived distance audit;
independent corpus compilation/instrumented execution; figure token identity,
compilation and reachable/unreachable labels; LaTeX build/page count/references;
layout and task-only diff inspection; knowledge relationship checks.

## Verification and recovery
Executed checks and limits are recorded in data/design/VALIDATION.md: 13 generator
tests, 32 scoring tests and six audit fixtures passed; the full rooted audit
verified 1,232 classes, 337,200 invocations and all 46,656 question labels. All
archived distance definitions match. The complete generated illustration and its
two polarities validate independently; original scores remain unchanged. The
nine-page PDF has resolved references and no overfull boxes, and pages 2–4 were
visually inspected. Generator hashes and its clean worktree are unchanged.
Revert task-owned commits to recover the prior draft. Rooted runtime agreement
cannot establish behavior for arbitrary arguments or model understanding.

## Completion

Completed. The implementation/evidence commit is recorded above. All acceptance
criteria are supported by data/design/VALIDATION.md; knowledge references and
statuses are closed without changing the source generator or experiments.
