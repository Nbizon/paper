# Specifications

## Metadata
- Project: ReachabilityBench ICSE 2027 paper draft
- Repository: /home/nbizon/These/Projects/paper
- Main branch: plan
- Last updated: 2026-06-10
- Status: active draft

## Scope
- In scope: LaTeX paper structure, benchmark terminology, methodology, metrics, TODO visibility, and traceability for the ICSE 2027 draft.
- Out of scope: Running final experiments, verifying external web claims, or changing benchmark-generation code.

## Explicit Requirements

### REQ-0001
- Status: implemented
- Source: User request and codex_icse2027_reachabilitybench_spec_v1.txt
- Description: Apply the ReachabilityBench paper specification on a new branch after committing the current draft state.
- Acceptance criteria: The draft uses the ReachabilityBench title/framing, control-flow and condition-aware task families, three research questions, and visible red TODOs for unresolved claims or results.
- Traceability:
  - Code: main.tex; macros.tex; sections/00_abstract.tex; sections/01_introduction.tex; sections/02_background.tex; sections/03_benchmark_design.tex; sections/05_methodology.tex; sections/06_results.tex; sections/07_discussion.tex; sections/08_threats.tex; sections/10_conclusion.tex
  - Tests: manual::latexmk build
  - Docs: README.md
  - ADR:
  - Commits:

### REQ-0002
- Status: implemented
- Source: codex_icse2027_reachabilitybench_spec_v1.txt
- Description: Main-paper terminology must use "condition-aware reachability" instead of "data-flow reachability" as the task-family name.
- Acceptance criteria: Included sections and metadata avoid presenting "data-flow reachability" as the main term.
- Traceability:
  - Code: sections/01_introduction.tex; sections/03_benchmark_design.tex; sections/05_methodology.tex; sections/06_results.tex; sections/08_threats.tex; README.md
  - Tests: rg::data-flow
  - Docs:
  - ADR:
  - Commits:

### REQ-0003
- Status: implemented
- Source: codex_icse2027_reachabilitybench_spec_v1.txt
- Description: The main paper must focus on tree-shaped call graphs generated from randomized pseudo-binary trees and remove linear call graphs and p-extreme figures from the main-paper design section.
- Acceptance criteria: The included benchmark design section describes only tree-shaped call graphs, treats p = 0.65 as a fixed calibration parameter, and omits linear and p-extreme main-paper subsections.
- Traceability:
  - Code: sections/03_benchmark_design.tex; figures/pipeline.tex
  - Tests: rg::Linear; rg::p=0
  - Docs:
  - ADR:
  - Commits:

### REQ-0004
- Status: implemented
- Source: codex_icse2027_reachabilitybench_spec_v1.txt
- Description: The evaluation protocol must prioritize final-answer accuracy, canonical execution-trace accuracy, trace completeness, graph-valid exploration accuracy, and NO_RESPONSE rate.
- Acceptance criteria: Methodology and results tables define and report the required metrics with strict-score convention in the main paper.
- Traceability:
  - Code: sections/05_methodology.tex; sections/06_results.tex; tables/metrics.tex; tables/overall_performance.tex
  - Tests: manual::latexmk build
  - Docs:
  - ADR:
  - Commits:

### REQ-0005
- Status: implemented
- Source: codex_icse2027_reachabilitybench_spec_v1.txt
- Description: Add a dedicated error-analysis section that introduces syntactic-call bias and records TODOs for final taxonomy/dashboard figures.
- Acceptance criteria: The draft includes an Error Analysis section with a syntactic-call-bias schematic and visible red TODOs for final taxonomy and dashboard artifacts.
- Traceability:
  - Code: sections/07_discussion.tex
  - Tests: manual::latexmk build
  - Docs:
  - ADR:
  - Commits:

## Non-Functional Requirements

### NFR-0001
- Category: process
- Status: implemented
- Source: AGENTS.md
- Description: Substantive paper changes must preserve traceability and validation notes.
- Acceptance criteria: specifications.md records requirements, affected files, and validation commands.
- Traceability:
  - Code: specifications.md
  - Tests: git::status; manual::latexmk build
  - Docs:
  - ADR:
  - Commits:

## Assumptions

### ASM-0001
- Status: proposed
- Source: Codex
- Description: The user intended "applique le agent.md qu'a la nouvelle branche" to mean that AGENTS.md-governed edits should be applied only after creating the new branch, not on the original branch.
- Reason: The request explicitly asked to commit current changes first, then create a branch, then apply the specification.
- Risk if wrong: The user may have expected a different branch-local policy-file change.
- Validation plan: Report the branch and commit sequence in the final response.
- Traceability:
  - Code:
  - Tests: git::branch --show-current
  - Docs:
  - ADR:
  - Commits:

## Open Questions

### TBD-0001
- Status: open
- Description: Final experiment results, model metadata, related-work verification, p calibration evidence, signed-distance semantics, and prompt appendix content remain unresolved.
- Impact: The paper must retain visible red TODOs until these are verified or rerun.
- Resolution:

## Architecture Decisions
- None.

## Traceability Index
- REQ-0001 -> main.tex; sections/*.tex; README.md -> manual::latexmk build -> commit::pending
- REQ-0002 -> terminology replacements -> rg::data-flow -> commit::pending
- REQ-0003 -> sections/03_benchmark_design.tex -> rg::Linear; rg::p=0 -> commit::pending
- REQ-0004 -> tables/metrics.tex; tables/overall_performance.tex -> manual::latexmk build -> commit::pending
- REQ-0005 -> sections/07_discussion.tex -> manual::latexmk build -> commit::pending
- NFR-0001 -> specifications.md -> git::status -> commit::pending

## Change Log
- 2026-06-10 - Applied ReachabilityBench paper specification to the branch-local LaTeX draft.
