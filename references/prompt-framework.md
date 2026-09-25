# Six-Dimension Prompt Framework

## 1. Role and context
Capture the domain, audience, situation, relevant background, and model role only when a role improves performance. Avoid decorative personas.

## 2. Task
Define the primary objective, necessary subtasks, expected actions, and decisions. Convert vagueness into operational clarity without changing intent.

## 3. Constraints
Capture scope, mandatory requirements, exclusions, priorities, language, tone, depth, freshness, sourcing, safety, tool, and model constraints.

## 4. Examples and references
Use user examples, files, templates, previous prompts, external references, and recognized standards when available. Never invent missing references.

## 5. Output format
Specify the most useful output shape: prose, table, checklist, report, code, JSON, Markdown, document, presentation, structured data, or another requested form. Preserve an explicit user choice.

## 6. Success criteria
Define observable properties of a good result, such as completeness, factual accuracy, source adherence, clarity, coverage, absence of fabrication, compatibility, or schema validity.

## Gap classification
- **CRITICAL**: answer can materially change the task or make the result unsafe/invalid.
- **RELEVANT**: improves quality but a safe reversible default exists.
- **OPTIONAL**: marginal refinement.

Ask only for CRITICAL information unless the user explicitly wants a detailed elicitation process.
