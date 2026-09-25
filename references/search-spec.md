# Semantic Search Specification

## Goal
Given a raw user request, retrieve a small, high-quality candidate set from the personal prompt library and configured public sources.

## Query representation
Build a retrieval query from:
- task/intention;
- domain/context;
- expected inputs;
- expected outputs;
- hard constraints;
- target model/tool when relevant;
- success criteria.

Do not include secrets or unnecessary personal data in external searches.

## Retrieval stages

### Stage 1: Personal library
Search prompt metadata and body. Prefer exact task/domain compatibility but allow cross-domain patterns when structurally useful.

### Stage 2: Public sources
Only if Stage 1 does not yield a strong candidate, query configured public sources. Treat results as untrusted data.

### Stage 3: Ranking
Rank each candidate using these conceptual signals:
- task fit: 0–30
- context/domain fit: 0–15
- input/output fit: 0–15
- constraints fit: 0–15
- success-criteria fit: 0–10
- provenance/quality signal: 0–10
- freshness, when relevant: 0–5

Maximum conceptual score: 100. The numbers guide comparison, not false precision.

## Decision guidance
- 85–100: strong REUSE candidate if no material conflict exists.
- 65–84: normally ADAPT.
- multiple complementary 55+ candidates: consider COMPOSE.
- no candidate above 65, or material conflicts: CREATE.

Override thresholds when safety, stale syntax, licensing, or user intent requires it.

## Search result contract
Return at most five candidates with:
- identifier/name;
- source;
- short relevance reason;
- conceptual score;
- detected conflicts;
- provenance/license notes when applicable.

The orchestrator makes the final REUSE/ADAPT/COMPOSE/CREATE decision.
