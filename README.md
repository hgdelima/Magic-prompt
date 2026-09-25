# Magic Prompt

Portable Agent Skill for prompt engineering, retrieval, evaluation, and prompt-library management across Codex and ChatGPT-compatible skill environments.

## Core flow

`understand → retrieve → decide → clarify only if needed → generate → evaluate → persist when useful`

The skill analyzes six dimensions: role/context, task, constraints, examples/references, output format, and success criteria. It searches the user's prompt library first, then configured public sources, and chooses among REUSE, ADAPT, COMPOSE, or CREATE.

## Structure

- `SKILL.md` — orchestration and behavior
- `references/prompt-framework.md` — six-dimension framework
- `references/retrieval-strategy.md` — retrieval and decision logic
- `references/evaluation-rubric.md` — quality gate
- `references/public-sources.md` — configurable external sources
- `references/security-rules.md` — untrusted-content and prompt-injection rules
- `assets/prompt-metadata-template.yaml` — metadata template for reusable prompts

## Persistence policy

Generated prompts are classified as `EPHEMERAL`, `REUSABLE`, or `UPDATE`. Only reusable prompts or meaningful updates should be proposed for versioning.
