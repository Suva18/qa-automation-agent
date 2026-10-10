# Voice Agent Project Adapter

## Apply When

The product accepts speech and responds through speech, telephony, or real-time audio.

## Extend the Core With

- Test the pipeline as separate observable stages: connection, capture, voice activity detection, transcription, reasoning/tool use, synthesis, playback, and teardown.
- Record latency to first acknowledgment, final transcript, first audio response, and completed response using the product's defined thresholds.
- Cover interruption/barge-in, silence, overlap, noise, packet loss, reconnect, echo, device changes, accents, code-switching, and long sessions.
- Verify confirmation before consequential actions and correct cancellation when the user interrupts or retracts intent.
- Use consented synthetic voices and non-sensitive conversations.
- Verify that transcripts, recordings, tool arguments, and generated audio follow privacy and retention rules.

## Project Questions

Resolve rather than infer:

- Supported channels, codecs, languages, devices, and network envelope
- Turn-taking and interruption contract
- Maximum latency and timeout budgets
- Recording/retention/consent behavior
- Tool-call confirmation and escalation rules
- Expected behavior for partial transcripts and mid-turn disconnects

## Critical Journeys

1. Connect, understand a normal request, respond, and terminate cleanly.
2. Interrupt an in-progress response without duplicated or stale actions.
3. Recover or fail clearly on connection, transcription, model, tool, and synthesis errors.
4. Prevent unconfirmed side effects, cross-session memory leakage, and sensitive-data playback.
