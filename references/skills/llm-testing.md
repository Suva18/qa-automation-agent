# LLM Testing Reference

Load this only for designing or executing a comprehensive model/agent evaluation.

## Evaluation Dimensions

Correctness, completeness, grounding, instruction following, tool choice/arguments/order, confirmation, privacy, safety, injection resistance, consistency, latency, cost, refusal quality, and graceful failure.

## Procedure

1. Version an evaluation set with normal, boundary, adversarial, multilingual, and out-of-scope examples relevant to the product.
2. Define objective checks before subjective rubrics and isolate must-not-fail invariants.
3. Freeze and record runtime configuration without secrets.
4. Repeat enough trials to expose meaningful variability.
5. Evaluate observable intermediate actions, retrieved sources, and state transitions.
6. Compare with a named baseline by scenario slice, not only aggregate score.

## Output

Report configuration, dataset version, trial count, dimension results, hard failures, redacted examples, baseline comparison, and confidence limits.
