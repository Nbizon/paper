---
{
  "schema_version": "1.0",
  "id": "SPEC-20261012",
  "record_type": "requirement",
  "title": "Prompt-context comparison and ten-page manuscript",
  "source": {
    "actor": "user",
    "mode": "explicit",
    "reference": "Author request of 2026-10-12"
  },
  "intent_status": "active",
  "delivery_status": "in_progress",
  "verification_status": "unverified",
  "priority": "high",
  "risk": "medium",
  "relations": {
    "depends_on": [
      "SPEC-20261006"
    ],
    "conflicts_with": [],
    "derived_from": [],
    "supersedes": [],
    "superseded_by": [],
    "related_to": []
  },
  "traceability": {
    "code": [
      "scripts/aggregate_prompt_comparison.py"
    ],
    "tests": [
      "scripts/aggregate_prompt_comparison.py",
      "scripts/check_knowledge.py"
    ],
    "docs": [
      "sections/03_research_questions.tex",
      "sections/04_benchmark_design.tex",
      "sections/05_experimental_setup.tex",
      "sections/06_results.tex",
      "data/prompt_comparison/VALIDATION.md"
    ],
    "adrs": [],
    "commits": []
  },
  "introduced_by": "CHG-20261012"
}
---

# Prompt comparison revision

The author replaces the external-score RQ3 with the comparison of last_exp and
last_exp_7, moves prompt design into Section IV, distinguishes the benchmark
from its construction algorithm, and requests Qwen3.8-Flash-Next v1/v4 results.
The prose must retain the manuscript's style and the compiled paper must fit
within ten pages including references. This supersedes AC-04 of SPEC-20261006;
its task-family and original-score requirements remain applicable.

- AC-01: RQ3 and its answer concern explicit entry context and determinism;
  prompt structure specifies a Java class containing multiple methods and the
  cases with and without Main, in Design rather than Experimental Setup.
- AC-02: Comparisons retain common-question denominators, non-responses, and
  the 16,384 versus 32,768 budget difference. Qwen3.8 v1/v4 uses its 216-question
  fixed-budget subset, with polarity-specific results.
- AC-03: Gemma comparison prose is ready for the final dataset; provisional
  measured values remain explicitly identifiable and replaceable, with no
  fabricated full-corpus results.
- AC-04: Essential results, concise validity limits, related work and conclusion
  fit in a compiled manuscript of at most ten pages with resolved references.
