# Severity and Priority Decisions

Severity describes observed product impact. Priority describes remediation order and is set with product/engineering context.

## Severity

| Level | Definition | Typical evidence |
|---|---|---|
| S0 Critical | Active security/privacy breach, irreversible widespread data loss, or safety-critical harm. | Confirmed exposure or destructive impact requiring incident response. |
| S1 High | Core workflow unavailable, unauthorized access, material corruption, or no reasonable workaround for many users. | Reproducible failure on a supported path with broad/material impact. |
| S2 Medium | Important behavior is wrong or degraded, but scope is limited or a reasonable workaround exists. | Functional failure with bounded impact. |
| S3 Low | Minor functional, accessibility, content, or visual issue with limited user impact. | Localized deviation that does not block the task. |

## Priority

| Level | Meaning |
|---|---|
| P0 | Act immediately; incident or release stop. |
| P1 | Fix before the target release unless an accountable owner accepts the risk. |
| P2 | Plan into the next suitable iteration. |
| P3 | Backlog; address when cost and opportunity align. |

## Modifiers

Consider prevalence, affected roles, data sensitivity, exploitability, workaround quality, regression status, strategic importance, deadline, and fix risk. Do not lower severity because a workaround exists without stating its availability and cost. Do not equate cosmetic appearance with low impact when accessibility or trust is affected.

## Output

Record severity with evidence, suggested priority with rationale, and the accountable person who confirms priority when known.
