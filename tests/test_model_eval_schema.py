import json
import unittest
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / ".agents/skills/software-factory/proxy/templates"

ORIGINAL_REQUIRED = ["timestamp", "task_id", "task_type", "model_used", "tier", "tokens", "qa_result"]


class TestModelEvalSchema(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads((TEMPLATES / "model-eval-schema.json").read_text(encoding="utf-8"))

    def test_required_fields_unchanged(self):
        self.assertEqual(self.schema["required"], ORIGINAL_REQUIRED)
        self.assertEqual(
            self.schema["properties"]["tokens"]["required"],
            ["prompt_tokens", "completion_tokens", "total_cost_usd"],
        )
        self.assertEqual(
            self.schema["properties"]["qa_result"]["required"],
            ["first_time_pass", "attempts_needed", "final_status"],
        )

    def test_local_tier_fields_are_optional(self):
        props = self.schema["properties"]
        for name in ("runtime", "local_latency_ms", "escalated_from_local", "estimated_tokens_saved"):
            self.assertIn(name, props)
            self.assertNotIn(name, self.schema["required"])
        self.assertEqual(props["runtime"]["enum"], ["local", "cloud"])

    def test_tier_keeps_1_to_3_and_allows_local(self):
        options = self.schema["properties"]["tier"]["oneOf"]
        self.assertIn({"type": "integer", "enum": [1, 2, 3]}, options)
        self.assertIn({"type": "string", "enum": ["L"]}, options)


class TestRoutingLocalExample(unittest.TestCase):
    def setUp(self):
        self.text = (TEMPLATES / "routing-local.example.yaml").read_text(encoding="utf-8")

    def test_endpoint_is_localhost_only(self):
        self.assertIn('endpoint: "http://127.0.0.1:11434"', self.text)
        urls = [w for w in self.text.replace('"', " ").split() if w.startswith("http")]
        self.assertTrue(all(u.startswith("http://127.0.0.1") for u in urls))

    def test_single_attempt_and_exclusions(self):
        self.assertIn("max_attempts: 1", self.text)
        for task in ("QA_GATEKEEPER_VERDICT", "SECRET_SCAN", "DUPLICATE_CHECK",
                     "RED_GREEN_CERTIFICATION", "SECURITY_REVIEW"):
            self.assertIn(f"- {task}", self.text)


if __name__ == "__main__":
    unittest.main()
