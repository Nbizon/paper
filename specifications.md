# Specifications

## Metadata
- Project: ReachabilityBench ICSE 2027 paper draft
- Repository: /home/nbizon/Thèse/Projects/paper
- Main branch: icse2027-paper-revision
- Last updated: 2026-06-15
- Status: active draft

## Scope
- In scope: LaTeX paper structure, benchmark terminology, methodology, metrics, TODO visibility, and traceability for the ICSE 2027 draft.
- Out of scope: Running final experiments, verifying external web claims, or changing benchmark-generation code.

## Explicit Requirements

### REQ-0001
- Status: replaced
- Source: User request and codex_icse2027_reachabilitybench_spec_v1.txt
- Description: Apply the ReachabilityBench paper specification on a new branch after committing the current draft state.
- Acceptance criteria: Replaced by REQ-0012 and REQ-0013, because the current ICSE 2027 instructions require the IEEE wrapper, unguarded and condition-aware task-family wording, and four research questions.
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

### REQ-0006
- Status: implemented
- Source: User request and codex_icse2027_reachabilitybench_icse_research_v2.txt
- Description: Reframe the draft as an ICSE Research Track empirical software-engineering benchmark paper with explicit novelty, rigor, relevance, verifiability/transparency, and presentation concerns.
- Acceptance criteria: Introduction and methodology explicitly address ICSE-facing evaluation criteria, avoid broad "first benchmark" claims, keep uncertain claims as visible red TODOs, and add an artifact/reproducibility paragraph.
- Traceability:
  - Code: sections/01_introduction.tex; sections/05_methodology.tex; README.md; bibliography/references.bib
  - Tests: manual::latexmk build; rg::first benchmark
  - Docs: README.md
  - ADR:
  - Commits:

### REQ-0007
- Status: replaced
- Source: codex_icse2027_reachabilitybench_icse_research_v2.txt
- Description: Keep research-question wording provisional until author confirmation.
- Acceptance criteria: Replaced by REQ-0013, because codex_instructions_reachabilitybench_icse2027.md provides a four-RQ framing to use unless the author requests another framing.
- Traceability:
  - Code: sections/01_introduction.tex; sections/04_research_questions.tex; sections/06_results.tex; tables/research_questions.tex
  - Tests: rg::Finalize RQ wording
  - Docs:
  - ADR:
  - Commits:

### REQ-0008
- Status: implemented
- Source: codex_icse2027_reachabilitybench_icse_research_v2.txt
- Description: Revise related work and novelty positioning around end-to-end code benchmarks, semantic-structure benchmarks, and call-graph/program-analysis work.
- Acceptance criteria: Related work discusses MBPP, CRUXEval, REval, CORE, and TraceEval; Defects4J is positioned as a classic testing/bug dataset; TraceEval and CORE are explicitly treated as close novelty threats.
- Traceability:
  - Code: sections/02_background.tex; bibliography/references.bib
  - Tests: rg::TraceEval; rg::CORE; rg::CRUXEval; rg::REval
  - Docs:
  - ADR:
  - Commits:

### REQ-0009
- Status: implemented
- Source: codex_icse2027_reachabilitybench_icse_research_v2.txt
- Description: Separate model identity from deployed inference mode and avoid a simplistic reasoning versus non-reasoning taxonomy.
- Acceptance criteria: Methodology and model table use intended role and inference-mode wording, replace "Jean" with "Jean Zay (IDRIS)" wording, and keep model metadata/local execution details as visible red TODOs.
- Traceability:
  - Code: sections/05_methodology.tex; sections/06_results.tex; tables/models.tex; sections/00_abstract.tex; sections/10_conclusion.tex
  - Tests: rg::Jean; rg::non-reasoning
  - Docs:
  - ADR:
  - Commits:

### REQ-0010
- Status: implemented
- Source: codex_icse2027_reachabilitybench_icse_research_v2.txt
- Description: Structure limitations as empirical-software-engineering threats to validity.
- Acceptance criteria: The limitations section is renamed to Discussion and Threats to Validity and includes construct, internal, external, conclusion, and reproducibility/artifact validity discussion.
- Traceability:
  - Code: sections/08_threats.tex
  - Tests: rg::Construct Validity; rg::Conclusion Validity
  - Docs:
  - ADR:
  - Commits:

### REQ-0011
- Status: implemented
- Source: User request and /home/nbizon/Thèse/Projects/LLM_benchmark/paper/main.pdf
- Description: Refine the tree-only dataset-generation description using the earlier ReachabilityBench paper, while keeping the main draft oriented toward a software-engineering conference rather than low-level generator internals.
- Acceptance criteria: The benchmark design section describes the tree dataset generation pipeline, local pseudo-binary expansion rule, finite method-budget truncation, graph-to-Java materialization, and dataset output files; it does not reintroduce linear graphs as a main-paper focus.
- Traceability:
  - Code: sections/03_benchmark_design.tex
  - Tests: manual::latexmk build; rg::local-tree-rule; rg::Linear
  - Docs:
  - ADR:
  - Commits:

### REQ-0012
- Status: implemented
- Source: User request and codex_instructions_reachabilitybench_icse2027.md
- Description: Revise the draft as an ICSE 2027 Research Track paper using IEEE conference format and a controlled diagnostic benchmark framing.
- Acceptance criteria: The paper uses the required IEEE conference wrapper, a diagnostic ReachabilityBench title, a draft abstract with result TODOs, and a concise contribution list without invented results.
- Traceability:
  - Code: main.tex; macros.tex; sections/00_abstract.tex; sections/01_introduction.tex; sections/10_conclusion.tex
  - Tests: manual::latexmk build
  - Docs: revision_notes.md
  - ADR:
  - Commits:

### REQ-0013
- Status: replaced
- Source: codex_instructions_reachabilitybench_icse2027.md
- Description: Use four research questions covering reachability/trace accuracy, condition-aware degradation, structural/error factors, and requested reasoning-budget sensitivity.
- Acceptance criteria: Replaced by REQ-0018 after the author revised the paper to three research questions.
- Traceability:
  - Code: sections/04_research_questions.tex; tables/research_questions.tex; sections/06_results.tex; tables/analysis_roadmap.tex
  - Tests: rg::RQ4
  - Docs:
  - ADR:
  - Commits:

### REQ-0014
- Status: implemented
- Source: codex_instructions_reachabilitybench_icse2027.md
- Description: Make the experimental methodology reproducible except for final result-dependent values.
- Acceptance criteria: Methodology defines the benchmark instance, syntactic and executable call graphs, canonical trace, signed distance, model table, local inference TODOs, prompting, parsing, metrics, statistical analysis, oracle validation, and artifact plan.
- Traceability:
  - Code: sections/05_methodology.tex; tables/dataset_specification.tex; tables/models.tex; tables/metrics.tex
  - Tests: manual::latexmk build
  - Docs: missing_experimental_todos.md
  - ADR:
  - Commits:

### REQ-0015
- Status: implemented
- Source: codex_instructions_reachabilitybench_icse2027.md
- Description: Strengthen error analysis, threats to validity, related-work positioning, and data availability for ICSE review expectations.
- Acceptance criteria: Related work includes RE2-Bench and a positioning table; error analysis includes a taxonomy table; threats explicitly discuss construct/internal/external/conclusion/reproducibility risks; Data Availability appears after Conclusion.
- Traceability:
  - Code: sections/02_background.tex; sections/07_discussion.tex; tables/error_taxonomy.tex; sections/08_threats.tex; sections/11_data_availability.tex; bibliography/references.bib
  - Tests: manual::latexmk build
  - Docs: revision_notes.md; author_questions.md
  - ADR:
  - Commits:

### REQ-0016
- Status: implemented
- Source: instructions_codex_revision_reachabilitybench.md and user request
- Description: Recenter the draft on ReachabilityBench as a controlled and parameterized diagnostic benchmark, remove paper-body prose that explicitly states ICSE review instructions, and align generator/evaluator-dependent methodology with inspected scripts.
- Acceptance criteria: Abstract, introduction, RQs, methodology, results scaffolding, error analysis, threats, and data availability emphasize controlled factors, systems under evaluation, non-LLM baselines, canonical-trace rationale, strict scoring, and script-backed generation/evaluation details without inventing results.
- Traceability:
  - Code: sections/00_abstract.tex; sections/01_introduction.tex; sections/02_background.tex; sections/04_research_questions.tex; sections/05_methodology.tex; sections/06_results.tex; sections/07_discussion.tex; sections/08_threats.tex; sections/10_conclusion.tex; sections/11_data_availability.tex; tables/research_questions.tex; tables/metrics.tex; tables/dataset_specification.tex; tables/error_taxonomy.tex; tables/analysis_roadmap.tex
  - Tests: manual::latexmk build; rg::ICSE 2027 explicitly; rg::paired degradation; rg::conditional scores
  - Docs: revision_notes.md; missing_experimental_todos.md
  - ADR:
  - Commits:

### REQ-0017
- Status: implemented
- Source: User request
- Description: Remove unnecessary repetition and improve the paper's prose so that the draft reads clearly, naturally, and consistently with empirical software-engineering conference standards.
- Acceptance criteria: Abstract, introduction, background, benchmark design, methodology, results scaffold, error analysis, threats, conclusion, and data-availability text avoid redundant definitions, reduce repeated formulations, and keep result-dependent claims as visible TODOs rather than invented findings.
- Traceability:
  - Code: sections/00_abstract.tex; sections/01_introduction.tex; sections/02_background.tex; sections/03_benchmark_design.tex; sections/05_methodology.tex; sections/06_results.tex; sections/07_discussion.tex; sections/08_threats.tex; sections/10_conclusion.tex; sections/11_data_availability.tex
  - Tests: manual::latexmk build; rg::finalized rerun; rg::controlled and parameterized
  - Docs: revision_notes.md
  - ADR:
  - Commits:

### REQ-0018
- Status: implemented
- Source: User request
- Description: Align the paper sections after Research Questions with the author's revised three-RQ framing.
- Acceptance criteria: The RQ table, Results section, analysis roadmap, discussion/threats, and conclusion use three RQs: RQ1 for reachability accuracy and structural factors, RQ2 for model and inference-mode comparison including verified reasoning-budget analyses, and RQ3 for trace-level reasoning and error patterns.
- Traceability:
  - Code: sections/04_research_questions.tex; tables/research_questions.tex; sections/06_results.tex; tables/analysis_roadmap.tex; sections/07_discussion.tex; sections/08_threats.tex; sections/10_conclusion.tex
  - Tests: rg::RQ4; manual::latexmk build
  - Docs:
  - ADR:
  - Commits:

### REQ-0019
- Status: implemented
- Source: User request
- Description: Add page and line numbering to the draft for review and annotation.
- Acceptance criteria: The LaTeX preamble enables line numbering and the document uses visible page numbering.
- Traceability:
  - Code: main.tex
  - Tests: manual::latexmk build
  - Docs:
  - ADR:
  - Commits:

### REQ-0020
- Status: implemented
- Source: User request
- Description: Rework the paper figures so they share the visual direction of Figure 1 and remain readable in the IEEE draft.
- Acceptance criteria: TikZ-based figures use the same restrained blue/green/orange palette, light gray axes or panels, compact legends, and readable font sizing; placeholder figures use matching framed styling.
- Traceability:
  - Code: main.tex; figures/pipeline.tex; figures/latex_overall_metrics.tex; figures/latex_budget_scaling.tex; figures/latex_depth_context.tex; figures/latex_error_taxonomy.tex; figures/latex_used_reasoning_budget.tex; sections/03_benchmark_design.tex; sections/06_results.tex; sections/07_discussion.tex
  - Tests: manual::latexmk build
  - Docs:
  - ADR:
  - Commits:

### REQ-0021
- Status: implemented
- Source: User request
- Description: Rework Sections I, II, and III to reduce redundancy and make the paper's narrative thread progress naturally from motivation, to related-work positioning, to benchmark design.
- Acceptance criteria: The introduction states the attribution problem and \benchmark contribution without repeating related-work details; the background positions existing benchmarks without restating the full motivation; the design section focuses on task mechanics and oracle construction without rearguing the paper's motivation.
- Traceability:
  - Code: sections/01_introduction.tex; sections/02_background.tex; sections/03_benchmark_design.tex
  - Tests: manual::latexmk build
  - Docs:
  - ADR:
  - Commits:

### REQ-0022
- Status: implemented
- Source: User request and /home/nbizon/.codex/attachments/8fdc50b5-f759-42ae-b3a7-d4509ca29faf/pasted-text.txt
- Description: Rewrite the Abstract, Introduction, Related Work, and ReachabilityBench Design sections in a mature ICSE Research Track style that frames ReachabilityBench as a controlled diagnostic benchmark for executable program-structure reasoning.
- Acceptance criteria: The abstract uses controlled bracketed placeholders instead of visible TODOs; the introduction follows the requested six-paragraph contribution structure; related work uses four analytical subsections; the design section formally defines instances, syntactic and executable graphs, generation, guards, canonical traces, signed canonical trace length, dataset placeholders, and oracle validation without unsupported empirical claims.
- Traceability:
  - Code: sections/00_abstract.tex; sections/01_introduction.tex; sections/02_background.tex; sections/03_benchmark_design.tex
  - Tests: rg::sections targeted TODO check; manual::latexmk build
  - Docs:
  - ADR:
  - Commits:

### REQ-0023
- Status: implemented
- Source: User request and inspected generator/inference scripts
- Description: Rewrite Section V so the methodology reads naturally, reflects the Java tree-generation and vLLM reasoning-budget inference scripts, and leaves unresolved dataset and serving parameters as controlled placeholders.
- Acceptance criteria: Section V is native LaTeX without Markdown fences; it describes dataset release, experimental factors, model serving, prompting, parsing, metrics, statistics, baselines, and reproducibility; dataset/model tables avoid final numeric claims and visible TODOs for parameters the author has not fixed.
- Traceability:
  - Code: sections/05_methodology.tex; tables/dataset_specification.tex; tables/models.tex; tables/metrics.tex
  - Tests: rg::methodology targeted TODO/fence check; manual::latexmk build
  - Docs:
  - ADR:
  - Commits:

### REQ-0024
- Status: implemented
- Source: User request and /home/nbizon/.codex/attachments/43e9652a-532f-4689-abbd-aabff8916804/pasted-text.txt
- Description: Revise only Section V and its directly included methodology tables so the methodology follows the requested ICSE-style experimental-protocol outline while leaving all paper sections through Research Questions unchanged.
- Acceptance criteria: Section V uses subsections Evaluation Dataset, Experimental Factors, Model Configurations and Inference Protocol, Prompting and Output Parsing, Scoring and Analysis Plan, and Reproducibility; prompting and parsing are merged; metrics and statistical analysis are merged; baselines are removed; reasoning-budget controls are treated as configuration metadata; controlled placeholders remain for unresolved release constants.
- Traceability:
  - Code: sections/05_methodology.tex; tables/dataset_specification.tex; tables/models.tex; tables/metrics.tex
  - Tests: rg::methodology no-baseline/TODO/fence check; manual::latexmk build
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
- Description: Final experiment results, model metadata, related-work verification, p calibration evidence, signed-distance semantics, prompt appendix content, artifact links, AI-use disclosure decision, and IEEE page-budget compliance remain unresolved.
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
- REQ-0006 -> sections/01_introduction.tex; sections/05_methodology.tex; README.md -> manual::latexmk build -> commit::pending
- REQ-0007 -> sections/01_introduction.tex; sections/04_research_questions.tex; sections/06_results.tex; tables/research_questions.tex -> rg::Finalize RQ wording -> commit::pending
- REQ-0008 -> sections/02_background.tex; bibliography/references.bib -> rg::TraceEval -> commit::pending
- REQ-0009 -> sections/05_methodology.tex; tables/models.tex -> rg::Jean; rg::non-reasoning -> commit::pending
- REQ-0010 -> sections/08_threats.tex -> rg::Construct Validity -> commit::pending
- REQ-0011 -> sections/03_benchmark_design.tex -> manual::latexmk build; rg::local-tree-rule -> commit::pending
- REQ-0012 -> main.tex; sections/00_abstract.tex; sections/01_introduction.tex -> manual::latexmk build -> commit::pending
- REQ-0013 -> sections/04_research_questions.tex; sections/06_results.tex -> rg::RQ4 -> commit::pending
- REQ-0014 -> sections/05_methodology.tex; tables/dataset_specification.tex; tables/metrics.tex -> manual::latexmk build -> commit::pending
- REQ-0015 -> sections/02_background.tex; sections/07_discussion.tex; sections/08_threats.tex; sections/11_data_availability.tex -> manual::latexmk build -> commit::pending
- REQ-0016 -> sections/00_abstract.tex; sections/05_methodology.tex; sections/06_results.tex; tables/metrics.tex -> manual::latexmk build -> commit::pending
- REQ-0017 -> sections/00_abstract.tex; sections/01_introduction.tex; sections/02_background.tex; sections/03_benchmark_design.tex; sections/05_methodology.tex; sections/06_results.tex; sections/07_discussion.tex; sections/08_threats.tex; sections/10_conclusion.tex; sections/11_data_availability.tex -> manual::latexmk build -> commit::pending
- REQ-0018 -> sections/04_research_questions.tex; tables/research_questions.tex; sections/06_results.tex; tables/analysis_roadmap.tex -> rg::RQ4; manual::latexmk build -> commit::pending
- REQ-0019 -> main.tex -> manual::latexmk build -> commit::pending
- REQ-0020 -> figures/*.tex; sections/03_benchmark_design.tex; sections/06_results.tex; sections/07_discussion.tex -> manual::latexmk build -> commit::pending
- REQ-0021 -> sections/01_introduction.tex; sections/02_background.tex; sections/03_benchmark_design.tex -> manual::latexmk build -> commit::pending
- REQ-0022 -> sections/00_abstract.tex; sections/01_introduction.tex; sections/02_background.tex; sections/03_benchmark_design.tex -> rg::sections targeted TODO check; manual::latexmk build -> commit::pending
- REQ-0023 -> sections/05_methodology.tex; tables/dataset_specification.tex; tables/models.tex; tables/metrics.tex -> rg::methodology targeted TODO/fence check; manual::latexmk build -> commit::pending
- REQ-0024 -> sections/05_methodology.tex; tables/dataset_specification.tex; tables/models.tex; tables/metrics.tex -> rg::methodology no-baseline/TODO/fence check; manual::latexmk build -> commit::pending
- NFR-0001 -> specifications.md -> git::status -> commit::pending

## Change Log
- 2026-06-15 - Revised Section V to the requested ICSE experimental-protocol outline without changing sections through Research Questions.
- 2026-06-15 - Rewrote Section V around the inspected generation and inference scripts, keeping unresolved dataset and serving parameters as controlled placeholders.
- 2026-06-15 - Rewrote the abstract, introduction, related work, and benchmark design around the diagnostic benchmark framing requested for ICSE Research Track presentation.
- 2026-06-15 - Reworked Sections I, II, and III to reduce repetition and clarify the narrative progression from motivation to positioning to benchmark design.
- 2026-06-15 - Harmonized paper figures with the Figure 1 visual direction and improved readability of axes, panels, legends, bars, and placeholders.
- 2026-06-12 - Aligned the post-RQ manuscript structure with the author's revised three research questions and enabled page and line numbering for review.
- 2026-06-11 - Performed an editorial pass to reduce repeated phrasing, tighten duplicated definitions, and improve the ICSE-style narrative flow without adding unverified empirical claims.
- 2026-06-11 - Applied the second ReachabilityBench revision instructions: parameterized-benchmark thesis, script-backed methodology, non-LLM baselines, canonical-trace rationale, figure placeholders, and removal of explicit ICSE-instruction prose from the paper body.
- 2026-06-11 - Applied the ICSE 2027 revision instructions: IEEE wrapper, diagnostic title, four RQs, reproducibility-oriented methodology, error taxonomy, Data Availability, and revision tracking files.
- 2026-06-11 - Refined the tree-only dataset-generation description from the earlier ReachabilityBench paper while preserving the ICSE empirical-SE framing.
- 2026-06-11 - Applied ICSE Research Track alignment, related-work, provisional-RQ, model-taxonomy, artifact, and threats-to-validity revisions from the V2 Codex instructions.
- 2026-06-10 - Applied ReachabilityBench paper specification to the branch-local LaTeX draft.
