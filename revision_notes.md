# Current results revision — 2026-10-06

- Branch: `paper/reachability-results-analysis`.
- Author instruction: unguarded is `nb_if=0`; condition-aware is `nb_if>0`.
  This supersedes the historical mode-based interpretation described below.
- Recomputed the supplied dashboard and verified primary scores against the
  corrected executable-graph CSVs for both models and every joint stratum.
- Rewrote Results around the three active RQs, explaining guard/parameter
  interactions, target-directed errors, origin difficulty, exhaustive negative
  exploration, and opposing context/polarity effects.
- Added generated tables, appendix curves, eligibility counts, and source hashes.
- Verified scholarly references and official checkpoint comparisons; distinguish
  venue publications from preprints and vendor scores from our experiments.
- Existing local edits in `main.tex` and the untracked `t.txt` are preserved and
  excluded from task commits. Existing section-inclusion switches are retained.
- Commands and final evidence: `data/results/VALIDATION.md`.

The remainder records earlier revisions and is historical, not the current
source of family semantics or empirical claims.

# Revision Notes

## Scope

Applied `codex_instructions_reachabilitybench_icse2027.md` and `instructions_codex_revision_reachabilitybench.md` on branch `icse2027-paper-revision`.

## Main Edits

- Migrated the draft wrapper from ACM `acmart` to ICSE 2027's required IEEE conference format.
- Updated the title to `ReachabilityBench: Diagnosing LLMs on Controlled Java Method-Reachability Tasks`.
- Rewrote the abstract, introduction, contributions, and RQs around a controlled diagnostic benchmark framing.
- Split the study into four RQs, with reasoning-budget analysis as a secondary RQ4.
- Strengthened related work positioning around end-to-end code benchmarks, CRUXEval, REval, CORE/CoRe, TraceEval, and RE2-Bench.
- Formalized the methodology: instance tuple, syntactic/executable call graphs, graph-valid path, signed distance, parsing, metrics, statistics, and oracle validation.
- Added planned dataset specification, model, metrics, result, and error-taxonomy tables with explicit TODO placeholders.
- Added a Data Availability section after the conclusion.
- Preserved result-dependent TODOs rather than inventing results.
- Removed paper-body prose that explicitly described ICSE review criteria or artifact policy instructions.
- Recentered the argument on \benchmark as a controlled and parameterized diagnostic benchmark.
- Added Experimental Factors, Baselines and Sanity Checks, and path-evaluation subsections.
- Performed a prose cleanup pass across the abstract, introduction, background, design, methodology, results scaffold, error analysis, threats, conclusion, and data-availability text to remove unnecessary repetition and vary recurring formulations.

## Script-Backed Clarifications

- Generator defaults inspected in `multi_language_experiment_generator.py`: tree-only Java sweep, context sizes 100/250/500, depths 1--25, default `n_questions=4`, and positive/negative balancing at retained depths.
- Tree construction inspected in `method_tree.py` and `tree_chain_generator.py`: pseudo-binary BFS generation with default `p=0.65`; method declarations are shuffled after tree materialization.
- Condition-aware generation inspected in `tree_chain_generator.py` and `control_flow_generator.py`: executable generated calls may be placed in true guards, false guards may contain visible non-executable calls, and loops are generated as surface code rather than reachability-changing calls in the inspected tree configuration.
- Evaluator inspected in `evaluate_results.py`: the parser uses the last parsable JSON object; final-answer correctness and path correctness are independent; no canonical-trace or completeness metric is reported.
- Generator modes rechecked: `c` names the unguarded/control-flow family and `d` names the condition-aware/data-flow family. `n_if` is a factor within either mode, not the family selector. The reported `last_exp` configurations use mode `d`, including their `n_if=0` stratum.

## Known Risks

- The IEEE migration compiles only if the local TeX install provides `IEEEtran` and `IEEEtran.bst`.
- Several final definitions still need author-level confirmation for the frozen artifact: exact metric names, implemented non-LLM baselines, final model list, and final dataset generation command.
- The page budget should be rechecked after final results, figures, and IEEE formatting are stable.
- Some bibliography entries remain arXiv/preprint entries and should be checked before submission.

## Validation

- `latexmk -g -pdf main.tex` completed successfully with IEEEtran.
- `main.pdf` is 10 pages after the editorial compression pass.
- Remaining LaTeX warnings are layout-quality warnings, mostly `Underfull \hbox` in compact tables and TODO-heavy cells; no overfull boxes, unresolved citations, unresolved references, or LaTeX errors were reported in the final build.
