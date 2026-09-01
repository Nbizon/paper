# Missing Experimental TODOs

These TODOs depend on final reruns, finalized artifacts, or implementation verification.

## Results

- Insert final empirical abstract takeaway about the effects of distance, class size, and condition-aware guards.
- Insert final one-sentence empirical takeaway in the contributions.
- Insert final strict scores for all models and both task families.
- Insert matched factor-level degradation from unguarded to condition-aware reachability for each model.
- Insert final factor coefficients or effect estimates, confidence intervals, plots, and error-family counts.
- Insert budget-sensitivity results only for models and serving configurations with verified reasoning-budget controls.
- Replace the conclusion with final empirical insights after reruns.

## Dataset and Oracle

- Add calibration evidence or appendix pointer for `p = 0.65`.
- Confirm final `nb_questions_per_depth`.

## Metrics and Parsing

- Confirm final names for graph-valid/path/canonical-trace metrics in the paper and scripts.

## Models and Inference

- Verify model sizes, active parameters, context lengths, licenses, and source identifiers from official model cards.
- Verify local execution details not recoverable from the current logs: checkpoint revisions, request-level decoding parameters, stopping criteria, timeouts/retries, and model-specific reasoning-budget semantics.
- Verify which models expose reasoning-budget controls.

## Artifact

- Insert anonymized artifact URL for review.
- Verify model-output sharing constraints for each final checkpoint.
- Confirm whether a DOI-backed archival release will be prepared after acceptance.
- Add final dashboard appendix or artifact reference.
