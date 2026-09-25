# Retrieval and Decision Strategy

## Candidate retrieval
Search semantically using the request's task, domain, inputs, outputs, constraints, and success criteria. Prefer the user's library before public sources.

## Candidate assessment
Assess candidates on:
- intent/task fit;
- context/domain fit;
- input compatibility;
- output compatibility;
- constraint compatibility;
- evidence of prior usefulness when available;
- freshness when the task is time-sensitive;
- safety and provenance.

## Decision
- **REUSE**: candidate substantially satisfies the current need with no material change.
- **ADAPT**: one candidate is strong but needs contextual or structural changes.
- **COMPOSE**: multiple candidates contain complementary components worth combining.
- **CREATE**: no candidate is sufficiently relevant/strong, or reuse would add needless complexity.

Similarity is evidence, not the decision. Prefer a simpler new prompt over a poor forced match.

## Provenance
For external material, retain source name, source location when available, license/usage notes when relevant, and which components were adapted. Never present an external prompt as original work if provenance is known.
