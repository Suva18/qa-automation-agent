# AI Output Evaluation

## First Classify the Check

- **Invariant:** deterministic requirement that must always hold, such as no secret disclosure or no unconfirmed write.
- **Objective:** fact or structure with a reliable oracle, such as citation presence or exact tool arguments.
- **Rubric:** quality judgment, such as helpfulness or summary coverage.

Invariants pass or fail and are never averaged away by a quality score.

## Rubric

Score applicable dimensions from 0 to 4:

| Score | Meaning |
|---:|---|
| 4 | Fully correct, complete, grounded, and fit for use. |
| 3 | Correct and useful with a minor omission or clarity issue. |
| 2 | Partly useful but contains a material omission, ambiguity, or unsupported detail. |
| 1 | Mostly incorrect, poorly grounded, or unsafe to rely on. |
| 0 | Fails the task, violates a hard constraint, or fabricates material facts. |

Evaluate correctness, completeness, grounding, instruction following, clarity, and safety separately. Add domain dimensions only when defined before evaluation.

## Adjudication

- Use a versioned reference set and blind comparison when possible.
- Require cited evidence for factual or grounding judgments.
- Have a second reviewer adjudicate release-changing subjective failures or define agreement sampling in advance.
- Report results by scenario slice and repeated trial, including worst cases; do not rely only on averages.
- Treat an evaluator model as one signal, not ground truth. Calibrate it against human-labeled examples.

## Decision

Define thresholds before running. A hard invariant failure blocks the affected release path regardless of average rubric score. When the oracle is disputed, mark the item `NEEDS ADJUDICATION`, not pass or fail.
