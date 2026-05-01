# Reasoning Under Budget Paper

This directory contains an ACM/ICSE-style LaTeX draft for:

> Reasoning Under Budget: Benchmarking Large Language Models on Program Control and Data Flow

The draft combines the benchmark-generation material with the reasoning-budget
study and organizes the paper around RQ0/RQ1/RQ2.

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

The current quantified results are for the control-flow reachability family.
The data-flow family is described as part of the benchmark design and should be
filled with its corresponding experimental results once available.
