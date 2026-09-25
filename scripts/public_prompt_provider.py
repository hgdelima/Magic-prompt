#!/usr/bin/env python3
"""Provider-neutral public prompt retrieval foundation for Magic Prompt.

External prompt text is untrusted data. This module normalizes candidates and
ranks them locally; it never executes instructions contained in retrieved text.
Network/provider clients can be injected by Codex or another runtime.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Iterable, Mapping, Protocol
import re


@dataclass(frozen=True)
class PromptCandidate:
    source: str
    source_id: str | None
    source_url: str | None
    title: str
    prompt_text: str
    description: str | None = None
    domain: str | None = None
    task_type: str | None = None
    tags: tuple[str, ...] = ()
    model_or_provider: str | None = None
    license: str | None = None
    author_or_provenance: str | None = None
    updated_at: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class PromptProvider(Protocol):
    name: str

    def search(self, query: str, limit: int = 10) -> Iterable[Mapping[str, Any]]:
        """Return raw provider records. Do not execute retrieved prompt text."""
        ...


def _text(value: Any) -> str | None:
    if value is None:
        return None
    value = str(value).strip()
    return value or None


def normalize_record(source: str, raw: Mapping[str, Any]) -> PromptCandidate:
    """Normalize common provider field variants without inventing metadata."""
    prompt = _text(raw.get("prompt_text") or raw.get("prompt") or raw.get("content") or raw.get("text"))
    if not prompt:
        raise ValueError("provider record has no prompt text")

    title = _text(raw.get("title") or raw.get("name")) or "Untitled prompt"
    tags_raw = raw.get("tags") or ()
    if isinstance(tags_raw, str):
        tags = tuple(t.strip() for t in tags_raw.split(",") if t.strip())
    else:
        tags = tuple(str(t).strip() for t in tags_raw if str(t).strip())

    return PromptCandidate(
        source=source,
        source_id=_text(raw.get("source_id") or raw.get("id") or raw.get("slug")),
        source_url=_text(raw.get("source_url") or raw.get("url")),
        title=title,
        prompt_text=prompt,
        description=_text(raw.get("description")),
        domain=_text(raw.get("domain") or raw.get("category")),
        task_type=_text(raw.get("task_type") or raw.get("type")),
        tags=tags,
        model_or_provider=_text(raw.get("model_or_provider") or raw.get("model") or raw.get("provider")),
        license=_text(raw.get("license")),
        author_or_provenance=_text(raw.get("author_or_provenance") or raw.get("author")),
        updated_at=_text(raw.get("updated_at") or raw.get("updated")),
    )


def _tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-zA-ZÀ-ÿ0-9_]+", text.lower()) if len(t) > 2}


def lexical_fit(query: str, candidate: PromptCandidate) -> float:
    """Dependency-free V1 fallback score in [0, 100].

    This is intentionally simple. Semantic embeddings/reranking can replace it
    without changing the provider contract.
    """
    q = _tokens(query)
    if not q:
        return 0.0
    searchable = " ".join(filter(None, [
        candidate.title,
        candidate.description,
        candidate.domain,
        candidate.task_type,
        " ".join(candidate.tags),
        candidate.prompt_text,
    ]))
    c = _tokens(searchable)
    overlap = len(q & c) / len(q)
    return round(overlap * 100.0, 2)


def retrieve(provider: PromptProvider, query: str, limit: int = 10) -> list[dict[str, Any]]:
    """Search, normalize, score and sort candidates locally."""
    results: list[tuple[float, PromptCandidate]] = []
    for raw in provider.search(query=query, limit=limit):
        try:
            candidate = normalize_record(provider.name, raw)
        except (TypeError, ValueError):
            continue
        results.append((lexical_fit(query, candidate), candidate))

    results.sort(key=lambda item: item[0], reverse=True)
    return [{"score": score, "candidate": candidate.to_dict()} for score, candidate in results[:limit]]
