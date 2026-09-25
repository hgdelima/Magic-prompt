# Public Prompt Sources

Keep external sources configurable rather than hard-coding the skill to one provider.

For each configured source record:
- name;
- access method;
- scope/domain strengths;
- search capability;
- provenance fields;
- license/usage considerations;
- trust notes;
- freshness/maintenance signal when available.

## Source policy
Use public sources for discovery and reference, not authority. Prefer sources with clear provenance, active maintenance, transparent licensing, and prompts that can be inspected before use.

The retrieval implementation may add or remove providers without changing the core six-dimension framework or REUSE/ADAPT/COMPOSE/CREATE decision model.

## V1 status
No public provider is hard-coded yet. This is deliberate: provider selection and API/search implementation should be added independently so the core skill remains portable across Codex and ChatGPT-compatible environments.
