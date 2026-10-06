---
{
  "schema_version": "1.0",
  "id": "SPEC-20261006",
  "record_type": "requirement",
  "title": "Evidence-grounded manuscript results and task-family semantics",
  "source": {
    "actor": "user",
    "mode": "explicit",
    "reference": "Author request of 2026-10-06"
  },
  "intent_status": "active",
  "delivery_status": "in_progress",
  "verification_status": "unverified",
  "verification_evidence": {
    "method": "other",
    "confidence": "unknown",
    "verified_at": null,
    "evidence": []
  },
  "priority": "high",
  "risk": "medium",
  "relations": {
    "depends_on": [],
    "conflicts_with": [],
    "derived_from": [],
    "supersedes": [],
    "superseded_by": [],
    "related_to": []
  },
  "traceability": {
    "code": [
      "scripts/aggregate_results.py",
      "scripts/render_results.py",
      "scripts/check_knowledge.py"
    ],
    "tests": [
      "scripts/aggregate_results.py",
      "scripts/render_results.py",
      "scripts/check_knowledge.py"
    ],
    "docs": [
      "sections/04_benchmark_design.tex",
      "sections/05_experimental_setup.tex",
      "sections/06_results.tex",
      "bibliography/references.bib"
    ],
    "adrs": [],
    "commits": []
  },
  "introduced_by": "CHG-20261006"
}
---

# Evidence-grounded results

## Statement
The paper must define unguarded calls as nb_if=0, use the supplied last_exp
results for Qwen3.6-35B-A3B and Gemma-4-26B-A4B-it, explain the most informative
structural and trace diagnostics in the existing prose style, and cite verified
primary sources. This author instruction replaces the historical family
interpretation in specifications.md (REQ-0027), without changing raw metadata.

## Acceptance criteria
- AC-01: Included prose and tables consistently partition 11,664 unguarded and
  34,992 condition-aware questions per model, balanced by polarity.
- AC-02: Aggregates preserve non-responses, diagnostic eligibility and units,
  and match corrected executable-graph scores.
- AC-03: Results distinguish facts from proposed explanations, including
  value-origin difficulty and target-directed consequences of guard errors.
- AC-04: External comparisons identify their source and protocol; two models
  do not support a correlation claim.
- AC-05: Bibliographic entries and internal references resolve in a compiled
  manuscript; figures may be placed in the appendix.
