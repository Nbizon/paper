# Manuscript writing style

Reference: `Nolan_Reachability-2.pdf`, supplied by the author on 2026-10-12.
The document is a stylistic reference only. Its facts, definitions, results,
research questions and experimental choices are not sources for the manuscript.

- Develop each paragraph progressively: introduce an idea, explain its mechanism,
  then explain what follows from it.
- Use complete explanatory sentences and familiar verbs such as provide, follow,
  compare, check and determine.
- Make connections explicit with transitions such as “This allows us to”,
  “As a consequence”, “However” and “For example”, where they serve the argument.
- Introduce notation through prose and explain its meaning before discussing
  its implications.
- Prefer explanations to compressed noun phrases and sequences of short claims.
- Explain findings through the distinction between the question, the final answer
  and the evidence returned by the model.
- Use a measured academic tone. Preserve qualifications and avoid adding practical
  application claims merely to connect the benchmark to software engineering.

The current paper is the factual source. Style revisions preserve its numbers,
formulas, citations, scoring rules and distinction between the final benchmark
and the construction algorithm.

## Verification of this transfer

The working manuscript before this revision was retained separately. Automated
comparisons confirm unchanged numbers, citation keys, section labels, figure/table
inputs and displayed formulas in every section. The results, generation and
scoring descriptions were also reviewed against that manuscript. The Research
Questions, tables, figures, scripts and aggregate data are unchanged.

The two result-rendering checks and the project-knowledge check pass. A complete
LaTeX/BibTeX build in a separate directory succeeds, producing ten pages with no
undefined references/citations or overfull boxes. Pages 1, 4 and 8 were inspected
for the introduction, construction/prompt explanations and discussion.
