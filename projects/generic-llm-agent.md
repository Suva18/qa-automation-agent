# Generic LLM Agent Project Adapter

## Apply When

The target is an LLM assistant or agent without a more specific adapter.

## Extend the Core With

- Map the runtime contract: input, system constraints, context sources, memory, tools, confirmation gates, output schema, and user-visible failure handling.
- Separate conversational quality from deterministic agent behavior. Tool authorization, arguments, state transitions, isolation, and structured output are hard contracts when defined as such.
- Test direct and indirect prompt injection, conflicting instructions, unsupported requests, sensitive-data requests, malformed tool results, timeouts, and partial failures.
- Verify tenant/session isolation, memory lifecycle, citation grounding, and that untrusted tool/model errors are sanitized before display.
- Compare model or prompt changes on a frozen, versioned dataset with repeated trials.

## Project Questions

Resolve from the implementation or authoritative documentation:

- Enabled models, tools, skills, providers, and runtime configuration
- Confirmation requirements and side-effect boundaries
- Memory sources, lifetime, deletion, and visibility
- Output schema and safe error contract
- Evaluation thresholds, cost budget, and latency objectives

## Critical Journeys

1. Correct intent handling and tool selection for supported requests.
2. Explicit confirmation and truthful reporting for side effects.
3. Safe refusal or clear failure for unsupported, unauthorized, or unavailable operations.
4. Grounded output with no cross-user leakage or raw internal/provider error disclosure.
