# Bibliographic verification — 2026-10-06

Checked against primary papers, publisher proceedings, author-hosted papers, and
official model cards. The bibliography distinguishes conference publications
from preprints; citation keys for LiveCodeBench, BigCodeBench, and REval now use
their publication years. DOI-only publisher pages blocked by the browser were
cross-checked with author copies and publisher search metadata.

| Key | Primary source | Verified scope and correction |
|---|---|---|
| chen2021codex | [arXiv](https://arxiv.org/abs/2107.03374) | HumanEval and test-based functional correctness; title/year/DOI and lead authors. Long author list explicitly abbreviated with `and others`. |
| austin2021program | [arXiv](https://arxiv.org/abs/2108.07732) | MBPP program synthesis; complete authors, title, year, DOI. |
| hendrycks2021apps | [Proceedings](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c24cd76e1ce41366a4bbe8a49b02a028-Abstract-round2.html) | APPS, tested challenge solutions; replaced preprint-only entry with 2021 venue. |
| lu2021codexglue | [Proceedings](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c16a5320fa475530d9583c34fd356ef5-Abstract-round1.html) | Ten understanding/generation tasks; full authors and proceedings entry. |
| jain2025livecodebench | [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/94074dd5a072d28ff75a76dabed43767-Abstract-Conference.html) | 2025 publication; time-segmented generation, execution, test-output prediction. First name of Han cross-checked with the paper/arXiv, since the proceedings display omits it. |
| zhuo2025bigcodebench | [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a6a90bcc2aa470c3871b2d39a67d26e8-Abstract-Conference.html) | 2025 publication; library/API calls and complex instructions. Author names use the proceedings version, including James Hoang. |
| just2014defects4j | [Author PDF](https://homes.cs.washington.edu/~rjust/publ/defects4j_issta_2014.pdf) | Java faults and tests; authors, 2014 venue, pages 437–440 and DOI. |
| jimenez2024swebench | [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html) | Repository-level issue resolution; complete authors and 2024 venue. |
| grove2001framework | [Author PDF](https://projectsweb.cs.washington.edu/research/projects/cecil/pubs/cgc-toplas.pdf) | Call-graph construction; TOPLAS 23(6), 685–746, 2001. |
| tip2000scalable | [Author PDF](https://www.franktip.org/pubs/oopsla2000.pdf) | Propagation-based call graphs and unreachable-method analysis; 2000 venue and pages 281–293. |
| gu2024cruxeval | [PMLR](https://proceedings.mlr.press/v235/gu24c.html) | Generated short Python functions with input/output tasks; authors, volume 235 and pages 16568–16621. |
| chen2025reval | [Author citation](https://pan2013e.github.io/posts/icse25/) | Runtime paths/coverage/states/output and incremental consistency; replaced 2024 preprint entry with 2025 proceedings, pages and DOI. |
| xie2025core | [Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/896cbab7d54e3fb158c4980db83290c7-Abstract-Datasets_and_Benchmarks_Track.html) | Human-verified dependency/information-flow analysis; full authors, volume 38 and 2025 venue. This is Xie et al.'s CoRE, not the unrelated 2026 benchmark sharing that name. |
| li2026traceeval | [arXiv](https://arxiv.org/abs/2605.11006) | Execution-witnessed runtime call structure; full ten-author list, 2026 preprint and DOI. |
| liu2025re2bench | [arXiv v3](https://arxiv.org/abs/2512.14917v3) | Real-world input/output reasoning complexity; four authors, 2025 first submission, 2026 revision explicitly noted. No unverified conference venue is assigned. |
| qwen2026qwen36 | [Official Qwen card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | Named checkpoint and the five external comparison rows. SWE evaluations use a vendor scaffold; Pro uses a refined task set. Terminal-Bench uses Harbor/Terminus-2 and five runs. |
| google2026gemma4 | [Official Google card](https://huggingface.co/google/gemma-4-26B-A4B-it) | Named instruction-tuned checkpoint; independently confirms LiveCodeBench v6 = 77.1. |
| kwon2023vllm | [Paper](https://arxiv.org/abs/2309.06180) / [publisher DOI](https://doi.org/10.1145/3600006.3613165) | vLLM/PagedAttention; complete authors, 2023 proceedings, pages 611–626 and DOI. Serving version 0.24.0 comes from local logs, not this 2023 paper. |

Uncited conference-policy, supercomputer press-release, and chain-of-thought
entries were removed. The related-work table now describes task/evidence scope
instead of assigning unsupported realism/control ratings. It explicitly
acknowledges LiveCodeBench's tasks beyond generation.

Official card URLs are mutable. The access date identifies this verification,
not an immutable revision of model weights or benchmark implementations.

## Contribution-positioning review — 2026-10-12

Rechecked the closest primary sources before revising the introduction, Related
Work and the compact comparison table:

- [REval, author publication page](https://pan2013e.github.io/posts/icse25/):
  intermediate runtime behavior and consistency between predictions; existing
  code benchmarks adapted for evaluation.
- [CoRE, NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/896cbab7d54e3fb158c4980db83290c7-Abstract-Datasets_and_Benchmarks_Track.html):
  human-verified data/control dependency and information-flow tasks.
- [TraceEval, primary preprint](https://arxiv.org/abs/2605.11006):
  repository-derived runtime call structure with execution-witnessed edges.

The revised manuscript explicitly recognizes these existing semantic diagnostic
evaluations. ReachabilityBench is positioned through its combination of
controlled generated factors, labels/graphs validated on the final dataset,
and separate decision/exploration-trace scores. No first-of-its-kind claim or
unsupported claim about absent functionality in another benchmark is introduced.
The software-engineering implications are prospective evaluation criteria for
program understanding, debugging and change-impact inspection, not measured
developer benefits or a demonstration on repository-scale programs.
