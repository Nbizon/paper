---
{
  "schema_version": "1.0",
  "id": "SPEC-20261012-design",
  "record_type": "requirement",
  "title": "Source-verified construction design and generated illustration",
  "source": {
    "actor": "user",
    "mode": "explicit",
    "reference": "Author request to verify code_generation and revise Section IV and Figure 1"
  },
  "intent_status": "active",
  "delivery_status": "implemented",
  "verification_status": "verified",
  "priority": "high",
  "risk": "medium",
  "relations": {
    "depends_on": [
      "SPEC-20261012"
    ],
    "conflicts_with": [],
    "derived_from": [],
    "supersedes": [],
    "superseded_by": [],
    "related_to": []
  },
  "traceability": {
    "code": [
      "examples/design/TheClass.java",
      "examples/design/Main.java",
      "scripts/render_design_example.py"
    ],
    "tests": [
      "scripts/check_knowledge.py",
      "scripts/render_design_example.py"
    ],
    "docs": [
      "sections/04_benchmark_design.tex",
      "sections/02_background.tex",
      "data/design/VALIDATION.md"
    ],
    "adrs": [],
    "commits": [
      "1ecad1ab212fcc18ba68f54fde5eafca74277deb"
    ]
  },
  "introduced_by": "CHG-20261012-design",
  "verification_evidence": {
    "method": "other",
    "confidence": "high",
    "verified_at": "2026-10-12",
    "evidence": [
      "data/design/VALIDATION.md",
      "data/design/semantic_validation_summary.json",
      "data/design/example_validation_summary.json"
    ]
  }
}
---

# Source-verified benchmark design

The author requests a construction audit against the supplied versioned generator,
a revised Section IV suitable for a research paper, and a correct Figure 1,
while retaining the existing prose style and ten-page limit.

- AC-01: Design explains structural generation, typed value propagation, guard
  construction, executable metadata, query selection and scoring from inspected
  source. Configured counts are per method, with root/helper exceptions explicit.
- AC-02: Maintained generator formats/prompts are distinguished from the measured
  archive; study families retain nb_if=0 / nb_if>0. Distance definitions and the
  associated results interpretation agree with the archived questions.
- AC-03: Figure 1 preserves all executable and disabled calls in a complete small
  generated class, with a separate Main and truthful provenance; compilation,
  rooted execution and both query polarities are checked.
- AC-04: Oracle validation evidence and its concrete-entry scope are explained;
  figure/source references resolve and the PDF remains at most ten pages.
