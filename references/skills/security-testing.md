# Security Testing Reference

Load this only after scope and authorization are established.

## Threat Coverage

Authentication/session handling; function/object authorization; tenant isolation; injection and file handling; secret exposure; SSRF, redirect, CORS, and CSRF; abuse, replay, rate limits, races, and exhaustion; LLM injection, tool overreach, exfiltration, and confirmation bypass.

## Safe Execution

1. Map assets, actors, entry points, trust boundaries, and abuse cases.
2. Start with non-destructive checks and synthetic data.
3. Prove only the minimum necessary impact; do not persist, escalate, or move laterally.
4. Stop on instability, real data, or boundary ambiguity.
5. Preserve sanitized evidence and notify the authorized owner through the agreed channel.

## Finding Output

Record asset, preconditions, minimal reproduction, impact, likelihood, evidence, containment, and remediation verification. Exclude exploit-ready secrets and unnecessary sensitive data.
