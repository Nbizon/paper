# Figure 1: complete generated illustration

This four-method program is a small illustration of the construction algorithm,
not an instance added to the 46,656-question model experiment. Every method,
variable declaration, executable call, inactive call and guard is retained.
`TheClass.java` and `Main.java` are distinct Java source files.

`selection.json` records the seed (192), factor configuration, source, targets
and value. Parameters omitted from that configuration have the inspected
`TreeCallExperimentConfig` defaults: no comments or loops, branch probability
0.65 and helper probability total 0.2. The root has no parameter; the other
methods have one. A helper declaration is generated even though n_vars=0.
`executable_graph.json` is the metadata recorded during Java emission.
The generator revision and module hashes appear in
[data/design/source_provenance.json](../../data/design/source_provenance.json).

Regenerate the exact Java, oracle and whitespace-compacted figure:

```bash
python3 scripts/render_design_example.py \
  --generator-root /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/code_generation
python3 scripts/render_design_example.py \
  --generator-root /home/nbizon/Thèse/Projects/versionning/LLM_benchmark/src/code_generation --check
```

The renderer disables bytecode writes to the external generator directory.
It verifies the example's source value and oracle relationships. All changes
in the displayed code are whitespace changes, including compact printing blocks.

In the rooted execution, copySessionFromFile invokes buildSessionToBuffer(4),
which invokes clearNotificationFromUrl(4), and then invokes sortJobForRequest(4)
itself. Both `<= -5` guards are false. From buildSessionToBuffer:

- clearNotificationFromUrl is reachable (+1);
- sortJobForRequest is unreachable (-1);
- the valid evidence for either query is
  [buildSessionToBuffer, clearNotificationFromUrl], with different Boolean answers.

Independent compilation/instrumented execution checked the recorded argument
values, direct calls, source region and both labels. See
[data/design/VALIDATION.md](../../data/design/VALIDATION.md) and the retained
[invocation events](../../data/design/example_runtime_events.tsv).
