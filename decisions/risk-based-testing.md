# Risk-Based Testing Decisions

## Risk Model

Score each test area on two independent axes from 1 to 5:

- **Impact:** consequence if the behavior fails, considering users, data, money, security, compliance, operations, and reversibility.
- **Likelihood:** probability of failure, considering change size, complexity, novelty, dependencies, historical defects, observability, and test gaps.

`Risk score = Impact × Likelihood`

| Score | Tier | Default response |
|---:|---|---|
| 20–25 | Critical | Test first; require direct evidence and explicit disposition before release. |
| 12–19 | High | Cover normal, boundary, negative, recovery, and permission behavior. |
| 6–11 | Medium | Cover representative behavior and the most likely failure mode. |
| 1–5 | Low | Use targeted checks or defer with rationale. |

## Decision Rules

- A single catastrophic outcome may remain critical even when likelihood is low.
- Increase likelihood for shared components, migrations, concurrency, weak contracts, or large dependency changes.
- Decrease neither impact nor likelihood merely because a test is expensive.
- Record uncertainty; when evidence is absent, do not assign false precision.
- Recalculate residual risk after mitigations and test results.

## Coverage Output

For each area record impact, likelihood, rationale, planned coverage, evidence, and residual risk. Use the score to order work, not as a substitute for judgment.
