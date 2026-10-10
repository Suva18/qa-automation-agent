# Privacy and Visibility Decisions

## Classification

Classify data before testing:

- **Public:** approved for unrestricted disclosure.
- **Internal:** limited to authorized organization members.
- **Confidential:** business-sensitive or access-restricted.
- **Restricted:** credentials, regulated data, highly sensitive personal data, private recordings/transcripts, or security evidence.

Use the project's stricter classification when one exists.

## Decision Checks

For every artifact or operation determine:

1. Who is the subject, owner, viewer, editor, and administrator?
2. What purpose and authorization permit collection and use?
3. What is the minimum data needed?
4. Where is it stored, processed, cached, logged, exported, and backed up?
5. How are access changes, revocation, retention, deletion, and legal holds handled?
6. Can generated summaries, search indexes, notifications, or links reveal data beyond the source visibility?

## Rules

- Use synthetic data by default and consented fixtures when realism is essential.
- Do not copy restricted data into prompts, tickets, screenshots, logs, or test artifacts.
- A derived artifact inherits at least the strictest visibility of its sources unless an explicit policy says otherwise.
- Verify authorization with positive and negative identities; UI hiding alone is not access control.
- Stop on unexpected real data, cross-tenant access, or unclear consent and notify the authorized owner.

## Output

Record classification, lawful/authorized test basis, roles tested, data locations, visibility outcomes, retention/deletion results, redactions, and unresolved privacy risk.
