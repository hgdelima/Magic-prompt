# Prompt Library

This directory is the canonical library of reusable prompts managed by Magic Prompt.

## Storage rule

Store one prompt per Markdown file. Use YAML front matter compatible with `assets/prompt-metadata-template.yaml`, followed by the prompt body.

Suggested organization:

```text
prompts/
  analysis/
  coding/
  communication/
  research/
  strategy/
  misc/
```

Folders are organizational only. Retrieval should be semantic and metadata-aware rather than depending on folder names.

## Persistence

- `EPHEMERAL`: do not store.
- `REUSABLE`: create a library item if it adds durable value.
- `UPDATE`: improve the existing item rather than creating a near-duplicate.

## Public-repository rule

Do not persist secrets, credentials, personal/confidential data, private company information, or prompts whose examples/context reveal sensitive information.
