# ReachabilityBench Paper

This directory contains an ACM/ICSE-style LaTeX draft for:

> Benchmarking Large Language Models on Controlled Java Reachability Tasks

The draft is being rewritten around ReachabilityBench, a controlled Java
benchmark for method-reachability questions with two task families:
control-flow reachability and condition-aware reachability. Existing results
are preliminary; final experiments must be rerun under the stabilized protocol
described in `codex_icse2027_reachabilitybench_spec_v1.txt`.

## Build

From this directory:

```bash
make
```

or directly:

```bash
latexmk -pdf main.tex
```

The manuscript uses the ACM `acmart` class with:

```latex
\documentclass[sigconf,review,anonymous]{acmart}
```

Main-paper claims should use visible red TODOs for any missing result,
unverified external claim, or unresolved experimental parameter.
