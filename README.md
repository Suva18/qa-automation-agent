# QA Agent

A prompt-and-reference package for generating QA test cases, investigating defects, planning regression coverage, evaluating APIs, UIs, LLM agents, meeting AI, security risks, and release readiness.

This package is not an executable application. Your AI client or internal application must load the Markdown files into the model context.

For a one-file version, use `qa-agent.yml`. It embeds the main prompt, routes, skills, detailed references, decisions, project adapters, and templates. Attach it with the instruction: `Read main_prompt first and use the route matching my QA task.` Direct attachment is convenient but may count the entire YAML toward the model context.

## How It Works

Load [agent.md](agent.md) first. It is the only permanent main prompt. It selects additional material progressively:

```text
agent.md
  -> one skills/*.md entry prompt
     -> optional references/skills/*.md detail
  -> optional decisions/*.md policy
  -> optional projects/*.md adapter
  -> one templates/*.md output format
```

Do not load this README or every package file into the model prompt. The README is for the human or application developer operating the package.

## Quick Start: Generate Test Cases

For a small, well-defined feature, give the model these files:

1. `agent.md`
2. `skills/test-case-design.md`
3. `templates/test-cases.md`

Then send a request such as:

```text
Generate functional and negative test cases for employee login.

Requirements:
- Email and password are required.
- Lock the account for 15 minutes after five consecutive failures.
- A successful login resets the failure count.

Return designed test cases only. Do not claim they were executed.
```

For a large or ambiguous feature, also load:

- `references/skills/test-case-design.md`
- `decisions/risk-based-testing.md` when prioritization is required
- One applicable file from `projects/`

## Common Workflows

| Task | Load after `agent.md` | Optional detail/policy | Output |
|---|---|---|---|
| Generate test cases | `skills/test-case-design.md` | `references/skills/test-case-design.md`, `decisions/risk-based-testing.md` | `templates/test-cases.md` |
| API test design | `skills/api-testing.md` | `references/skills/api-testing.md` | `templates/test-cases.md` |
| UI test design | `skills/ui-testing.md` | `references/skills/ui-testing.md` | `templates/test-cases.md` |
| Exploratory test charter | `skills/exploratory-testing.md` | `references/skills/exploratory-testing.md` | `templates/test-summary.md` |
| Defect investigation | `skills/defect-analysis.md` | `references/skills/defect-analysis.md`, `decisions/severity-priority.md` | `templates/bug-report.md` |
| Regression planning | `skills/regression-testing.md` | `references/skills/regression-testing.md`, `decisions/risk-based-testing.md` | `templates/test-summary.md` |
| LLM evaluation | `skills/llm-testing.md` | `references/skills/llm-testing.md`, `decisions/ai-output-evaluation.md` | `templates/test-summary.md` |
| Meeting-AI testing | `skills/meeting-ai-testing.md` | `references/skills/meeting-ai-testing.md`, AI/privacy policies | `templates/test-summary.md` |
| Authorized security review | `skills/security-testing.md` | `references/skills/security-testing.md`, privacy policy | `templates/bug-report.md` |
| Release recommendation | Relevant skill | `decisions/risk-based-testing.md` | `templates/release-gate.md` |

Load at most one project adapter:

- `projects/elisa.md` for Elisa-specific meeting-assistant work
- `projects/voice-agent.md` for real-time voice or telephony agents
- `projects/generic-llm-agent.md` for other tool-using LLM agents

Do not load an adapter when no project clearly matches.

## Example Requests

### API coverage

```text
Design API test cases for POST /employees.
Cover schema validation, duplicate email, authorization, tenant isolation,
database side effects, dependency failure, and idempotency.
Prioritize the cases by risk. Do not call the live API.
```

### UI coverage

```text
Create UI test cases for the employee onboarding wizard.
Cover keyboard accessibility, validation, refresh, session expiry,
double submission, mobile layout, errors, and recovery.
```

### Defect report

```text
Analyze the attached failed checkout evidence.
Separate facts from hypotheses, suggest severity and priority,
and produce a reproducible bug report. Redact customer identifiers.
```

### Regression plan

```text
Create a risk-based regression plan for the authentication change described below.
Identify affected components, adjacent contracts, critical journeys,
negative controls, and explicitly omitted coverage.
```

### LLM-agent evaluation

```text
Design an evaluation plan for our internal support agent.
Test grounding, unsupported claims, tool selection, confirmation before writes,
prompt injection, safe failure, and cross-user data isolation.
Do not run paid model calls.
```

### Release gate

```text
Using the supplied test results and unresolved defects, produce a release gate.
Return GO, GO WITH CONDITIONS, NO-GO, or NOT ASSESSED and cite the evidence
for every required criterion.
```

## Manual Use in an AI Chat

If the platform supports file attachments or project knowledge:

1. Add `agent.md` to the system or permanent instruction field.
2. Attach one matching file from `skills/`.
3. Attach its detailed reference only for comprehensive work.
4. Attach a decision policy or project adapter only when triggered.
5. Attach the desired output template.
6. Submit the company task, requirements, and sanitized evidence.

If the platform automatically injects every uploaded file into every conversation, create separate projects by QA task or use an application-side loader. Uploading the entire package on every call defeats the token-saving design.

## Programmatic Use

Store the package in a company-owned repository. Resolve file names from an allowlist; never accept an arbitrary path supplied by a user or model.

```python
from pathlib import Path

ROOT = Path("qa-agent")

ALLOWED = {
    "main": "agent.md",
    "test-design": "skills/test-case-design.md",
    "test-design-detail": "references/skills/test-case-design.md",
    "risk": "decisions/risk-based-testing.md",
    "test-cases": "templates/test-cases.md",
}


def load_sections(section_names: list[str]) -> str:
    sections = []
    for name in section_names:
        relative_path = ALLOWED[name]
        sections.append((ROOT / relative_path).read_text(encoding="utf-8"))
    return "\n\n".join(sections)


system_prompt = load_sections(
    ["main", "test-design", "test-design-detail", "risk", "test-cases"]
)
```

In production, choose sections through validated structured routing rather than keyword or regex matching. The selected values must be limited to known capability, decision, project, and template identifiers.

## Rebuild the Single YAML File

After changing any Markdown instruction, regenerate the bundle:

```bash
python3 scripts/build_yaml_bundle.py
```

The generated `qa-agent.yml` is self-contained. Only that file needs to be transferred when your company AI tool accepts a single attachment.

## Input Checklist

Provide as much of the following as the task requires:

- Product or feature name
- Requirement or acceptance criteria
- Changed behavior and known risks
- Build, environment, role, and supported platforms
- Test-data boundaries
- Explicitly excluded areas
- Whether the request is design-only or authorizes execution
- Desired output: cases, bug report, summary, or release gate

When an expected result is missing, the agent should report the ambiguity instead of inventing behavior.

## Company Use and Data Safety

- Move the package into an approved company-owned private repository.
- Follow company AI, privacy, security, open-source, and data-retention policies.
- Use synthetic or approved test data by default.
- Do not send credentials, production payloads, customer information, private recordings, or internal security evidence to an unapproved AI service.
- Active security testing, production testing, destructive actions, external side effects, and paid/live model calls require explicit authorization.
- Keep company-specific instructions in the company copy rather than the personal repository.

## Troubleshooting

**The response is too generic:** Load the detailed reference for the selected skill and provide clearer acceptance criteria.

**Token usage is high:** Confirm that only `agent.md`, one skill, required optional references, and one template are being sent.

**The model claims tests passed:** State that the task is design-only and require the `designed` execution status.

**The output format varies:** Load exactly one file from `templates/` and explicitly request that format.

**The wrong capability is selected:** Select the skill explicitly in the application or pass a validated structured routing decision.
