# ReachabilityBench Paper

This directory contains an ICSE/IEEE-style LaTeX draft for:

> ReachabilityBench: Diagnosing LLMs on Controlled Java Method-Reachability Tasks

The draft is being rewritten around ReachabilityBench, a controlled and parameterized Java
benchmark for method-reachability questions with two task families:
unguarded reachability and condition-aware reachability. Existing results
are preliminary; final experiments must be rerun under the stabilized protocol
tracked by the current revision notes and TODO inventory.

## Build

From this directory:

```bash
make
```

or directly:

```bash
latexmk -pdf main.tex
```

The current draft uses the ICSE 2027 IEEE conference format with:

```latex
\documentclass[10pt,conference]{IEEEtran}
```

Main-paper claims should use visible red TODOs for any missing result,
unverified external claim, or unresolved experimental parameter.

`codex_icse2027_reachabilitybench_icse_research_v2.txt` additionally requires
ICSE 2027 alignment, source-backed related work, model/inference-mode separation,
and explicit threats to validity. `codex_instructions_reachabilitybench_icse2027.md`
adds the current four-RQ framing, Data Availability section, reproducibility
TODO inventory, and IEEE page-budget constraints. `instructions_codex_revision_reachabilitybench.md`
adds the current parameterized-benchmark framing and script-backed methodology
alignment.
