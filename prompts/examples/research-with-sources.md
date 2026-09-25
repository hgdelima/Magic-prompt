---
name: research-with-sources
description: Research a topic using current, trustworthy sources and separate verified facts from inference.
version: "0.1.0"
domain: research
task_type: research
tags: [research, sources, web, verification]
inputs: [topic, scope]
outputs: [synthesis, sources, uncertainties]
constraints: [prefer primary sources, distinguish fact from inference, do not invent citations]
success_criteria: [claims are sourced, uncertainty is explicit, output answers the requested scope]
source: original
source_url: ""
license: ""
created_at: "2026-09-25"
updated_at: "2026-09-25"
persistence: REUSABLE
notes: "Example library item used to validate retrieval structure."
---

Research **{topic}** within **{scope}**.

Use current and trustworthy sources, preferring primary sources when available. Separate verified facts from inference or interpretation. Cite material factual claims. Explicitly identify meaningful uncertainty, conflicting evidence, or stale information. Do not invent facts, quotations, or citations.

Return a concise synthesis followed by the most decision-relevant evidence and remaining uncertainties.
