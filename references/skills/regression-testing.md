# Regression Testing Reference

Load this only for non-trivial change impact or release regression planning.

## Selection

Map changed code/configuration to callers, data, integrations, permissions, and journeys. Select changed behavior, adjacent contracts, historically fragile areas, and critical end-to-end paths.

## Order and Verification

1. Run fast deterministic checks before integration and end-to-end coverage.
2. Reproduce the original defect on an affected build when available.
3. Verify the fix, nearest boundaries, and a negative control.
4. Give flaky tests or environment failures an owner and follow-up; do not silently quarantine them.

## Output and Exit

Report build, scope, pass/fail/blocked/not-run counts, defects, environment issues, omissions, and residual risk. Exit only after required high-risk coverage ran, failures are dispositioned, and blockers are explicit.
