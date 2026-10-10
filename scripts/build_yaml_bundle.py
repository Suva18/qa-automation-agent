#!/usr/bin/env python3
"""Build the self-contained QA Agent YAML bundle from Markdown sources."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "qa-agent.yml"


MAIN_PROMPT = """# QA Agent — Single-File Main Prompt

Use the user's QA request as the primary instruction. This YAML file is a self-contained instruction bundle.

## Selection

1. Identify the requested task, surface, project, and output.
2. Select one route from `routes.capabilities`.
3. Apply `skills.<skill>.prompt`.
4. Apply its embedded `reference` only when the request needs comprehensive planning or execution.
5. Apply only triggered `decisions` and at most one matching `projects` adapter.
6. Render with the requested `templates` entry or the route's default template.

Do not combine every section. A second skill is allowed only when the request genuinely spans both. Treat Markdown file links inside embedded content as labels for sections already present in this YAML.

## Core Contract

- Never invent requirements, execution, evidence, defects, or release confidence.
- Label work designed, executed, blocked, or not run.
- Separate observed facts, expected behavior, assumptions, and hypotheses.
- Redact secrets, private content, personal data, and unnecessary internal identifiers.
- Get explicit approval before production or destructive testing, paid/live model calls, active security probing, or external side effects.
- Fail clearly when required access, data, environment, or expected behavior is missing.
- Ask only for missing facts that affect safety or make the expected result undecidable.
- Include scope, execution status, evidence, blockers, and residual risk in the result.
"""


ROUTES = {
    "test-case-generation": {
        "skill": "test-case-design",
        "reference": "test-case-design",
        "optional_decisions": ["risk-based-testing"],
        "default_template": "test-cases",
    },
    "api-testing": {
        "skill": "api-testing",
        "reference": "api-testing",
        "optional_decisions": ["risk-based-testing", "privacy-visibility"],
        "default_template": "test-cases",
    },
    "ui-testing": {
        "skill": "ui-testing",
        "reference": "ui-testing",
        "optional_decisions": ["risk-based-testing", "privacy-visibility"],
        "default_template": "test-cases",
    },
    "exploratory-testing": {
        "skill": "exploratory-testing",
        "reference": "exploratory-testing",
        "optional_decisions": ["risk-based-testing"],
        "default_template": "test-summary",
    },
    "llm-testing": {
        "skill": "llm-testing",
        "reference": "llm-testing",
        "optional_decisions": ["ai-output-evaluation", "privacy-visibility"],
        "default_template": "test-summary",
    },
    "security-testing": {
        "skill": "security-testing",
        "reference": "security-testing",
        "optional_decisions": ["privacy-visibility", "severity-priority"],
        "default_template": "bug-report",
    },
    "regression-testing": {
        "skill": "regression-testing",
        "reference": "regression-testing",
        "optional_decisions": ["risk-based-testing"],
        "default_template": "test-summary",
    },
    "meeting-ai-testing": {
        "skill": "meeting-ai-testing",
        "reference": "meeting-ai-testing",
        "optional_decisions": ["ai-output-evaluation", "privacy-visibility"],
        "default_template": "test-summary",
    },
    "defect-analysis": {
        "skill": "defect-analysis",
        "reference": "defect-analysis",
        "optional_decisions": ["severity-priority"],
        "default_template": "bug-report",
    },
    "release-gate": {
        "skill": "regression-testing",
        "reference": "regression-testing",
        "optional_decisions": ["risk-based-testing", "severity-priority"],
        "default_template": "release-gate",
    },
}


SKILLS = (
    "exploratory-testing",
    "test-case-design",
    "api-testing",
    "ui-testing",
    "llm-testing",
    "security-testing",
    "regression-testing",
    "meeting-ai-testing",
    "defect-analysis",
)

DECISIONS = (
    "risk-based-testing",
    "severity-priority",
    "ai-output-evaluation",
    "privacy-visibility",
)

PROJECTS = ("elisa", "voice-agent", "generic-llm-agent")

TEMPLATES = ("test-cases", "bug-report", "test-summary", "release-gate")


def read_markdown(relative_path: str) -> str:
    path = ROOT / relative_path
    if not path.is_file():
        raise FileNotFoundError(f"Required source is missing: {path}")
    return path.read_text(encoding="utf-8").rstrip()


def append_block(lines: list[str], key: str, value: str, indent: int) -> None:
    prefix = " " * indent
    lines.append(f"{prefix}{key}: |-" )
    content_prefix = " " * (indent + 2)
    lines.extend(f"{content_prefix}{line}" for line in value.splitlines())


def append_string_list(lines: list[str], key: str, values: list[str], indent: int) -> None:
    prefix = " " * indent
    if not values:
        lines.append(f"{prefix}{key}: []")
        return
    lines.append(f"{prefix}{key}:")
    lines.extend(f"{prefix}  - {value}" for value in values)


def build_bundle() -> str:
    lines = [
        'version: "1.0"',
        "name: qa-agent",
        "description: Self-contained QA prompt, routing, skills, references, decisions, projects, and templates.",
        "usage:",
        "  entrypoint: main_prompt",
        "  direct_attachment: Read main_prompt first, then use the selected embedded sections.",
        "  token_note: Direct attachment may count the entire YAML toward model context.",
    ]
    append_block(lines, "main_prompt", MAIN_PROMPT.rstrip(), 0)

    lines.append("routes:")
    lines.append("  capabilities:")
    for route_name, route in ROUTES.items():
        lines.append(f"    {route_name}:")
        lines.append(f"      skill: {route['skill']}")
        lines.append(f"      reference: {route['reference']}")
        append_string_list(
            lines,
            "optional_decisions",
            route["optional_decisions"],
            6,
        )
        lines.append(f"      default_template: {route['default_template']}")

    lines.extend(
        [
            "  projects:",
            "    elisa: Use only for explicitly identified Elisa meeting-assistant work.",
            "    voice-agent: Use for real-time speech or telephony agents.",
            "    generic-llm-agent: Use for other tool-using LLM agents.",
            "    none: Use when no project adapter clearly matches.",
        ]
    )

    lines.append("skills:")
    for skill in SKILLS:
        lines.append(f"  {skill}:")
        append_block(lines, "prompt", read_markdown(f"skills/{skill}.md"), 4)
        append_block(
            lines,
            "reference",
            read_markdown(f"references/skills/{skill}.md"),
            4,
        )

    lines.append("decisions:")
    for decision in DECISIONS:
        append_block(
            lines,
            decision,
            read_markdown(f"decisions/{decision}.md"),
            2,
        )

    lines.append("projects:")
    for project in PROJECTS:
        append_block(
            lines,
            project,
            read_markdown(f"projects/{project}.md"),
            2,
        )

    lines.append("templates:")
    for template in TEMPLATES:
        append_block(
            lines,
            template,
            read_markdown(f"templates/{template}.md"),
            2,
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT.write_text(build_bundle(), encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
