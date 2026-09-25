import unittest

from scripts.public_prompt_provider import normalize_record, lexical_fit, retrieve


class FakeProvider:
    name = "fake-public-library"

    def search(self, query: str, limit: int = 10):
        return [
            {
                "id": "research",
                "title": "Research with sources",
                "prompt": "Research a topic using reliable sources and cite every factual claim.",
                "tags": ["research", "sources", "citations"],
                "license": "CC0",
            },
            {
                "id": "poem",
                "title": "Write a poem",
                "prompt": "Write a short lyrical poem about the moon.",
                "tags": ["creative-writing"],
            },
            {"id": "broken", "title": "Missing prompt body"},
        ][:limit]


class PublicPromptProviderTests(unittest.TestCase):
    def test_normalizes_common_fields(self):
        candidate = normalize_record("demo", {
            "id": 42,
            "name": "Example",
            "content": "Do the task carefully",
            "tags": "analysis, quality",
        })
        self.assertEqual(candidate.source, "demo")
        self.assertEqual(candidate.source_id, "42")
        self.assertEqual(candidate.title, "Example")
        self.assertEqual(candidate.tags, ("analysis", "quality"))

    def test_missing_metadata_remains_unknown(self):
        candidate = normalize_record("demo", {"prompt": "Do something"})
        self.assertIsNone(candidate.license)
        self.assertIsNone(candidate.author_or_provenance)
        self.assertIsNone(candidate.source_url)

    def test_rejects_records_without_prompt_text(self):
        with self.assertRaises(ValueError):
            normalize_record("demo", {"title": "No body"})

    def test_relevant_candidate_ranks_first(self):
        ranked = retrieve(FakeProvider(), "research reliable sources citations", limit=10)
        self.assertEqual(ranked[0]["candidate"]["source_id"], "research")
        self.assertGreater(ranked[0]["score"], ranked[1]["score"])

    def test_lexical_score_is_bounded(self):
        candidate = normalize_record("demo", {"prompt": "research sources citations"})
        score = lexical_fit("research sources", candidate)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)


if __name__ == "__main__":
    unittest.main()
