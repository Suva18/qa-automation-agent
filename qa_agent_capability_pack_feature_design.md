# QA Agent Capability Pack — Feature Design

## 1. Summary

Create a reusable, Markdown-based QA agent package under `qa-agent/`. A compact main prompt routes each request section-by-section to testing capabilities, decision policies, output templates, and project-specific adapters without loading unrelated guidance.

## 2. Problem Statement

QA requests vary by surface, risk, and product domain, but ad hoc prompting often produces inconsistent coverage, severity, evidence, and release recommendations. Testers and engineering teams need a portable instruction set that makes scope, evidence, privacy, and release decisions explicit while remaining adaptable to different products.

## 3. Goals / Out of Scope

### Goals

- Route QA work to the smallest relevant set of capabilities.
- Produce reproducible test cases, defect reports, summaries, and release gates.
- Apply consistent risk, severity, AI-output, and privacy decisions.
- Support Elisa, voice-agent, and generic LLM-agent projects through adapters.
- Require authorization for destructive, privileged, costly, or live external testing.

### Out of Scope

- A new runtime, API, database model, UI, or automated test framework.
- Credentials, environment configuration, or live-system access.
- Product-specific test implementation inside the Easentic application.
- Replacing human approval for production release decisions.

## 4. Proposed Solution

`qa-agent/agent.md` is the low-token entry point. The user's prompt remains the primary instruction; the entry point derives task, surface, project, and output, then loads only the matching files. Each `skills/` file is itself a compact capability prompt and links to one optional detailed file under `references/skills/` for comprehensive planning or execution.

```text
user prompt -> main prompt router
            -> one compact primary capability
               -> optional detailed capability reference
            -> optional decision policy + at most one project adapter
            -> one output template at render time
```

## 5. Requirements

### Functional Requirements

- Cover exploratory, test-design, API, UI, LLM, security, regression, meeting-AI, and defect-analysis work.
- Distinguish observed facts from assumptions and unverified hypotheses.
- Avoid claiming execution when tests were only designed or reviewed.
- Prevent secrets and sensitive content from appearing in artifacts.
- Define objective release outcomes: `GO`, `GO WITH CONDITIONS`, `NO-GO`, or `NOT ASSESSED`.

### Non-Functional Requirements

- Markdown-only and tool-agnostic.
- Project adapters extend core instructions without duplicating them.
- The main prompt contains only shared invariants, routing, and the minimal workflow.
- Detailed material is loaded only when its capability, decision, project, or output is relevant.
- A narrow capability request must not require its detailed reference.
- Directories must not be preloaded wholesale.

## 6. Architecture / Changes Needed

- Keep `qa-agent/agent.md` as a compact section router and core contract.
- Add nine capability files under `qa-agent/skills/`.
- Add nine optional detailed capability references under `qa-agent/references/skills/`.
- Add four decision-policy files under `qa-agent/decisions/`.
- Add four reusable artifact templates under `qa-agent/templates/`.
- Add three project adapters under `qa-agent/projects/`.
- No application architecture, runtime flow, or source-of-truth ownership changes are required; `docs/SYSTEM_ARCHITECTURE.md` is therefore unchanged.

## 7. Risks / Considerations

- Generic guidance can overstate confidence; every artifact records execution status and evidence.
- Security and live integration testing can be disruptive; the orchestrator requires explicit scope and authorization.
- LLM outputs are probabilistic; evaluation uses repeated trials and separates hard failures from quality judgments.
- Project facts may drift; adapters mark assumptions and must not invent undocumented requirements.
- Over-routing increases token use and can introduce conflicting guidance; the main prompt limits each reference category and requires an explicit trigger.

## 8. Rollout Notes

- Use no project adapter when the project does not clearly match; do not load the generic adapter merely as a fallback.
- Add new adapters only for durable project-specific contracts.
- Keep this package version-controlled and review changes to decision thresholds with QA and product owners.

## 9. Test Plan

- Verify every requested path exists and contains no scaffold placeholders.
- Check all links in `agent.md` and cross-references resolve.
- Verify the main prompt does not instruct the runtime to preload any reference directory.
- Verify a narrow request can route to one capability and one output template without loading unrelated files.
- Verify every compact skill links to one existing detailed reference and does not duplicate its full procedure.
- Review that capability files define inputs, evidence, and outputs.
- Review that templates distinguish planned, executed, blocked, and not-run work.
- Validate security, privacy, external-service, and release-decision guardrails by inspection.
