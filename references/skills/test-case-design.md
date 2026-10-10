# Test Case Design Reference

Load this only for designing a suite or choosing test-design techniques.

## Technique Selection

- Equivalence partitions and boundaries for input domains.
- Decision tables for interacting rules.
- State transitions for lifecycle behavior.
- Pairwise coverage for costly combinations.
- Negative and recovery cases for contract failures.

## Procedure

1. Extract testable conditions and unresolved ambiguity.
2. Model inputs, states, roles, integrations, and outputs.
3. Select the smallest set covering meaningful partitions and high-risk interactions.
4. Add relevant permission, empty, malformed, timeout, retry, and concurrency cases.
5. Assign priority from risk, not author preference.
6. Review traceability and objective expected results.

## Output Quality

Record ID, traceability, priority, preconditions, data, steps, expected result, automation suitability, and execution status. Another tester must be able to run the case without guessing.
