# LLM Testing

Use when behavior depends on a model, retrieval, tools, prompts, memory, or multi-step agent execution.

## Core

Separate hard invariants from scored quality, freeze the runtime configuration, use a versioned dataset, and repeat trials where variability matters. Inspect observable tool calls and confirmation gates. Live or paid calls require explicit approval; model and retrieved content are untrusted.

## Optional Reference

For dataset composition, dimensions, trial design, baselines, slices, and reporting, load [LLM-testing reference](../references/skills/llm-testing.md). Load [AI evaluation policy](../decisions/ai-output-evaluation.md) only when scoring or adjudicating outputs.
