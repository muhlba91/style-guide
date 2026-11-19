import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import build_digest  # noqa: E402

TEXT = """# Sample

## PRIN-01 · must · common · stated

- Rule: Keep text short.
- Why: reader time.
- Good: `done`
- Bad: `done, as requested`
- Source: stated 2026-11-18, sample.
- Check: tool:ruff (`E501`)

## PRIN-02 · prefer · common · observed

- Rule: Name things.
- Good: `x`
- Source: seen.
- Check: judgment

## Avoid (AI-Era Artifacts)

- Banners.
"""


class DigestTest(unittest.TestCase):
    def test_parse_reads_rules_and_avoid_list(self):
        title, rules, avoid = build_digest.parse(TEXT)
        self.assertEqual(title, "Sample")
        self.assertEqual([r["id"] for r in rules], ["PRIN-01", "PRIN-02"])
        self.assertEqual(avoid, ["Banners."])

    def test_must_rule_keeps_examples_and_tool_check_only(self):
        _, rules, _ = build_digest.parse(TEXT)
        text = build_digest.render_rule(rules[0], True)
        self.assertIn("PRIN-01 must: Keep text short. [tool:ruff]", text)
        self.assertIn("Good: `done`", text)
        self.assertNotIn("reader time", text)

    def test_prefer_rule_has_no_examples(self):
        _, rules, _ = build_digest.parse(TEXT)
        self.assertNotIn("Good:", build_digest.render_rule(rules[1], True))

    def test_tokens_estimate_is_proportional(self):
        self.assertEqual(build_digest.tokens("a" * 360), 100)

    def test_repo_setup_digest_lists_the_new_repository_checklist(self):
        bullets = build_digest.checklist_bullets()
        self.assertTrue(bullets)
        self.assertTrue(all(bullet.startswith("- ") for bullet in bullets))
        rules, _ = build_digest.all_rules(path for _, path in build_digest.rule_files())
        text = build_digest.repo_setup_digest(rules)
        self.assertIn("not a rule", text)
        for bullet in bullets:
            self.assertIn(bullet, text)

    def test_committed_digests_are_current(self):
        self.assertEqual(build_digest.main(["--check"]), 0)


if __name__ == "__main__":
    unittest.main()
