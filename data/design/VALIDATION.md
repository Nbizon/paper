# Construction and illustration validation

Verified on 2026-10-12. The supplied generator and experiment archives remained
read-only throughout. The rewritten Design describes the construction mechanism
and distinguishes the maintained implementation from the historical experiment.

## Source audit

Inspected all 13 Python modules and README in the supplied code_generation
folder, plus the dataset card, graph loader and scoring definitions. The clean
source revision and individual module hashes are in `source_provenance.json`.
No source hash or external Git worktree status changed during verification.

| Manuscript claim | Inspected implementation |
| --- | --- |
| Unique composed names, single queue-expanded tree and budget truncation | method_name_generator.py; method_tree.build_structured_execution_tree |
| Parameter-free root, inherited primitive parameter types, extra locals | method_tree.Node; _sample_transmitted_param_types |
| Compatible arguments, fresh helper locals, committed callee values | tree_chain_generator.generate_single_method_body / build_call |
| True guards for structural calls, false guards for compatible decoys | control_flow_generator.generate_method_body; _base_condition |
| No benchmark calls in loop blocks; 1–5 iterations | eligible_blocks excludes loops; random_loop |
| Block/method shuffling; emitted executable-callee lists | generate_method_body; ExperimentRunner.generate_case |
| Positive DFS positions; negative region size minus one | generate_execution_questions |
| Balanced per-distance/per-polarity sampling across classes | ExperimentRunner._select; generate_case; generate_experiment |
| Separate launcher and optional deterministic-execution instruction | java_entrypoint.py; reachability_prompts.py; dataset-copy helpers |
| Executable predecessor, no duplicates, target stop / exact closure | executable_graph.is_valid_exploration; metrics.is_path_correct |

The external dataset card identifies the archive's absent seed/schema/source
revision and its old executable-tree format. The current prompt adds a rooted
entry-context sentence that was not in the measured archived v1/v4 prompts;
the manuscript preserves that distinction. Study families remain nb_if=0 and
nb_if>0 rather than being reinterpreted as the generator's c/d modes.

## Checks actually executed

- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/tests -p test_code_generation_cleanup.py -v`:
  13 tests passed, including generated Java compilation, truth of generated
  conditions, mode placement, factor grids and deterministic regeneration.
- The corresponding `test_evaluate_results.py` command: 32 tests passed,
  including executable path scoring and independent answer/path evaluation.
- The six integration fixtures in `studies/semantic_validation/test_audit.py`
  passed, checking wrong edges/labels, argument contexts, absent callers,
  compilation failure, early return and unchanged program output.
- Full independent rooted audit rerun with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/studies/semantic_validation/run.py \
  --dataset /home/nbizon/Thèse/Projects/results/last_exp_7/dataset \
  --reference-dataset /home/nbizon/Thèse/Projects/results/last_exp/dataset \
  --output /tmp/paper-design-semantic-audit --workers 4
```

  All 1,232 classes and 46,656 questions verified. The 337,200 invocation
  records matched oracle edges and regions, with no absent callers or differing
  invocation regions. Original/instrumented exit status, stdout and stderr
  matched; both input hash inventories remained unchanged. The manifest hash
  equals the earlier archived audit. The new `semantic_validation_summary.json`
  retains versions, validator hashes, counts, manifest hash and evidence-file
  hashes; detailed new traces/CSVs are in the command's temporary output.
- Reconstructed ordered DFS explorations for every archived question:
  all 46,656 signed distances match target position (positive) or closure size
  minus one (negative). See `distance_check.json`. This replaces the incorrect
  interpretation of shorter positive routes as extra shortcut calls.
- Reproduced Figure 1 with seed 192 and the four-method configuration in
  `examples/design/selection.json`. `scripts/render_design_example.py --check`
  confirms exact Java, oracle and figure regeneration. The displayed code
  differs from generated source only in whitespace; no calls/guards are removed.
- Independently compiled/instrumented that complete illustration and verified
  both +1/-1 queries with the same source. Four runtime invocations verify
  parameter value 4 and the source region. In particular, sortJobForRequest is
  called by the root after the source returns, not by the source. Summary and
  raw invocation events are retained beside this document.
- `python3 scripts/render_results.py --check`: the 12 original generated
  tables/figures remain unchanged. The prompt comparison aggregator with
  `--check` also matches; no model score has been modified.
- `latexmk -pdf -outdir=/tmp/paper-design-build -interaction=nonstopmode -halt-on-error main.tex`:
  final manuscript compiled to nine pages including references, without undefined
  references/citations or overfull boxes. PDF text and rendered pages 2–4 were
  inspected for Figure 1, pipeline arrows, construction prose and validation.
- `git diff --check` passed. Knowledge records and the derived specification
  index are checked with `scripts/check_knowledge.py` before completion.

## Limits

The exhaustive runtime audit verifies the existing corpus under the explicit
root launchers. It is not a universal proof of the generator or Java behavior,
and it does not establish how models interpreted the historical prompts.
The small generated illustration is outside the 100/250/500-method experimental
grid and is not added to model results. The historical generator revision and
seed remain unknown. Decoding, prompt-budget confounding and provisional Gemma
comparison values are unchanged by this revision.

Pre-existing main.tex/introduction edits and analyse.md/t.txt are preserved
outside task commits. Raw data and the generator source are unchanged.
