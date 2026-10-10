# Elisa Project Adapter

## Apply When

The target is the Elisa meeting-assistant product or a feature explicitly identified as part of Elisa.

## Extend the Core With

- Prioritize meeting lifecycle, participant consent, recording/transcription state, speaker attribution, summaries, decisions, action items, search, and sharing.
- Treat transcripts, recordings, summaries, participant identities, and calendar context as restricted unless the project's documented policy classifies them otherwise.
- Verify that derived artifacts never gain broader visibility than their source meeting without an explicit, tested policy.
- Test organizer, member, guest, removed participant, and unauthorized user paths when those roles exist.
- For integrations, verify token expiry, revocation, duplicate events, reordered webhooks, retries, and partial provider failure without exposing provider payloads.
- Apply meeting-AI testing plus LLM evaluation for transcript-derived content.

## Project Questions

Resolve from authoritative product documentation; do not guess:

- Supported meeting providers, languages, clients, and retention rules
- Consent and bot-admission behavior
- Processing-state contract and retry ownership
- Visibility inheritance for transcript, summary, actions, exports, and shared links
- Quality thresholds for transcript facts, summaries, and action items

## Critical Journeys

1. Authorized scheduling/admission through successful artifact publication.
2. Partial capture or processing failure with accurate status and recovery.
3. Correct participant and workspace visibility, including revocation/deletion.
4. Grounded summary, decisions, and action items with names, dates, and numbers preserved.

If the repository or product documentation defines Elisa differently, follow that source and record the discrepancy.
