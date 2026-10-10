# Defect Analysis Reference

Load this only for detailed isolation, triage, or fix-verification work.

## Isolation

1. Confirm the report against a defined expected result.
2. Reproduce from a clean state and minimize the sequence.
3. Vary one factor: build, role, data, state, timing, client, model configuration, or dependency.
4. Identify the earliest divergence and determine scope across users, tenants, platforms, and versions.
5. Search for duplicates and define the next discriminating check for unproven hypotheses.

## Evidence

Preserve timestamps and build/configuration identifiers. Sanitize logs, payloads, URLs, IDs, transcripts, screenshots, and model output. Reproduction difficulty or recency does not determine severity.

## Verification

Define direct fix verification, nearest-boundary cases, and adjacent regression coverage. The report must support reproduction and verification without guesswork.
