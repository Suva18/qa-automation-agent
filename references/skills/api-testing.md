# API Testing Reference

Load this only for comprehensive API planning or execution.

## Coverage

- Contract: method, path, headers, schema, types, required fields, and status codes.
- Behavior: boundaries, transitions, idempotency, pagination, filtering, and ordering.
- Failure: malformed input, missing resources, conflicts, dependencies, timeout, and rate limits.
- Access: unauthenticated, expired, wrong tenant/role, and object-level authorization.
- Effects: commits, rollback, duplicate suppression, audit events, and downstream calls.
- Operations: latency budget, correlation identifiers, safe errors, and structured logs.

## Execution

Capture sanitized request, response, timing, and resulting state. Validate forbidden requests produce no state change. For asynchronous work, verify accepted, processing, success, and failure states independently.

## Output

Produce a contract-coverage matrix or test cases. A defect includes the minimal sanitized request, actual response shape, expected contract, and verified side effects.
