import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import check_rules  # noqa: E402

VALID = """## PRIN-01 · must · common · stated

- Rule: Keep text short.
- Why: The reader's time matters.
- Source: stated by the owner in the project kickoff.
- Check: judgment
"""


class ParseTest(unittest.TestCase):
    def test_valid_rule_has_no_errors(self):
        self.assertEqual(check_rules.check_rule_text("a.md", VALID, set(), {}), [])

    def test_duplicate_id_is_reported(self):
        seen = {}
        check_rules.check_rule_text("a.md", VALID, set(), seen)
        errors = check_rules.check_rule_text("b.md", VALID, set(), seen)
        self.assertTrue(any("duplicate" in e for e in errors))

    def test_missing_field_is_reported(self):
        text = VALID.replace("- Check: judgment\n", "")
        errors = check_rules.check_rule_text("a.md", text, set(), {})
        self.assertTrue(any("missing field Check" in e for e in errors))

    def test_fields_out_of_order_are_reported(self):
        lines = VALID.split("\n")
        rule = next(i for i, line in enumerate(lines) if line.startswith("- Rule:"))
        check = next(i for i, line in enumerate(lines) if line.startswith("- Check:"))
        lines[rule], lines[check] = lines[check], lines[rule]
        errors = check_rules.check_rule_text("a.md", "\n".join(lines), set(), {})
        self.assertTrue(any("fields out of order" in e for e in errors))

    def test_open_rule_needs_defined_oq(self):
        text = VALID.replace("stated", "open").replace("must", "prefer") + "- See OQ-07.\n"
        self.assertTrue(any("not defined" in e for e in check_rules.check_rule_text("a.md", text, set(), {})))
        self.assertEqual(check_rules.check_rule_text("a.md", text, {"OQ-07"}, {}), [])

    def test_open_rule_without_reference_is_reported(self):
        text = VALID.replace("stated", "open").replace("must", "prefer")
        errors = check_rules.check_rule_text("a.md", text, {"OQ-07"}, {})
        self.assertTrue(any("without an OQ reference" in e for e in errors))

    def test_malformed_header_is_reported(self):
        errors = check_rules.check_rule_text("a.md", "## PRIN-1 · must\n\n- Rule: x\n", set(), {})
        self.assertTrue(any("malformed" in e for e in errors))

    def test_bad_check_value_is_reported(self):
        text = VALID.replace("- Check: judgment", "- Check: maybe")
        self.assertTrue(any("Check must start with" in e for e in check_rules.check_rule_text("a.md", text, set(), {})))

    def test_check_with_note_is_accepted(self):
        text = VALID.replace("- Check: judgment", "- Check: tool:ruff (`E501`), judgment")
        self.assertEqual(check_rules.check_rule_text("a.md", text, set(), {}), [])

    def test_family_with_digit_is_parsed(self):
        text = VALID.replace("PRIN-01", "K8S-01")
        self.assertEqual(check_rules.check_rule_text("a.md", text, set(), {}), [])
        self.assertEqual(len(check_rules.parse_rules(text)), 1)

    def test_unknown_family_is_reported(self):
        text = VALID.replace("PRIN-01", "ZZZ-01")
        self.assertTrue(any("unknown family" in e for e in check_rules.check_rule_text("a.md", text, set(), {})))


class NewChecksTest(unittest.TestCase):
    def test_must_with_open_is_an_error(self):
        text = VALID.replace("stated", "open") + "- See OQ-07.\n"
        errors = check_rules.check_rule_text("a.md", text, {"OQ-07"}, {})
        self.assertTrue(any("must and open" in e for e in errors))
        text = text.replace("must", "prefer")
        self.assertEqual(check_rules.check_rule_text("a.md", text, {"OQ-07"}, {}), [])

    def test_unknown_tool_is_an_error(self):
        text = VALID.replace("- Check: judgment", "- Check: tool:nonexistent")
        self.assertTrue(any("ALLOWED_TOOLS" in e for e in check_rules.check_rule_text("a.md", text, set(), {})))
        text = VALID.replace("- Check: judgment", "- Check: tool:conform")
        self.assertEqual(check_rules.check_rule_text("a.md", text, set(), {}), [])

    def test_family_must_match_file(self):
        text = VALID.replace("PRIN-01", "GO-01")
        errors = check_rules.check_rule_text("common/principles/a.md", text, set(), {})
        self.assertTrue(any("does not belong" in e for e in errors))
        self.assertEqual(check_rules.check_rule_text("common/languages/go.md", text, set(), {}), [])
        self.assertTrue(check_rules.check_rule_text("common/languages/pulumi.md", text, set(), {}))
        pulumi = VALID.replace("PRIN-01", "PULUMI-01")
        self.assertEqual(check_rules.check_rule_text("common/languages/pulumi.md", pulumi, set(), {}), [])
        self.assertTrue(check_rules.check_rule_text("common/languages/python.md", text, set(), {}))

    def test_stated_source_format_is_a_warning(self):
        warnings = []
        errors = check_rules.check_rule_text("a.md", VALID, set(), {}, warnings)
        self.assertEqual(errors, [])
        self.assertTrue(any("YYYY-MM-DD" in w for w in warnings))
        warnings = []
        text = VALID.replace(
            "stated by the owner in the project kickoff.",
            "stated 2026-11-18, weighting",
        )
        check_rules.check_rule_text("a.md", text, set(), {}, warnings)
        self.assertFalse(any("YYYY-MM-DD" in w for w in warnings))

    def test_must_without_good_is_a_warning(self):
        warnings = []
        self.assertEqual(check_rules.check_rule_text("a.md", VALID, set(), {}, warnings), [])
        self.assertTrue(any("without a Good" in w for w in warnings))
        warnings = []
        check_rules.check_rule_text("a.md", VALID + "- Good: `x`\n", set(), {}, warnings)
        self.assertFalse(any("without a Good" in w for w in warnings))

    def test_expand_ids(self):
        self.assertEqual(
            check_rules.expand_ids("PRIN-01 to 03, PRIN-50"),
            {"PRIN-01", "PRIN-02", "PRIN-03", "PRIN-50"},
        )

    def test_index_range_must_match_file(self):
        readme = "| [a.md](a.md) | PRIN-01 to 03 | x |\n"
        self.assertEqual(
            check_rules.index_errors("r", readme, {"a.md": {"PRIN-01", "PRIN-02", "PRIN-03"}}),
            [],
        )
        errors = check_rules.index_errors("r", readme, {"a.md": {"PRIN-01", "PRIN-02", "PRIN-04"}})
        self.assertEqual(len(errors), 1)

    def test_oq_affects_both_directions(self):
        oq = "### OQ-01 Title\n\n- Affects: PRIN-01, PRIN-02.\n"
        warnings = check_rules.oq_warnings(oq, {"PRIN-01": {"OQ-01"}, "PRIN-03": {"OQ-01"}})
        self.assertTrue(any("PRIN-02" in w and "does not cite" in w for w in warnings))
        self.assertTrue(any("PRIN-03" in w and "not in Affects" in w for w in warnings))
        self.assertEqual(
            check_rules.oq_warnings(oq, {"PRIN-01": {"OQ-01"}, "PRIN-02": {"OQ-01"}}),
            [],
        )


class RetiredTest(unittest.TestCase):
    def test_load_ignores_comments_and_blank_lines(self):
        self.assertEqual(check_rules.load_retired("# note\n\nGO-30 PULUMI-01\nDOC-07 -\n"), {"GO-30", "DOC-07"})

    def test_reused_id_is_an_error(self):
        errors = check_rules.check_retired({"GO-30": "go.md", "GO-01": "go.md"}, {"GO-30"})
        self.assertEqual(len(errors), 1)
        self.assertIn("GO-30", errors[0])


class BudgetTest(unittest.TestCase):
    def test_repo_files_are_within_budget(self):
        self.assertEqual(check_rules.check_budgets(), [])

    def test_oversized_file_is_reported(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENTS.md").write_text("x" * 5000, encoding="utf-8")
            errors = check_rules.check_budgets(root)
        self.assertEqual(len(errors), 1)
        self.assertIn("AGENTS.md", errors[0])


class PrivacyTest(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(check_rules.check_privacy("a.md", "Plain text."), [])

    def test_em_dash_email_path_emoji(self):
        text = "a — b, someone@example.com, /Users/someone/x, \U0001f600"
        self.assertEqual(len(check_rules.check_privacy("a.md", text)), 4)

    def test_gendered_pronoun_is_reported(self):
        self.assertEqual(len(check_rules.check_privacy("a.md", "He kept it.")), 1)
        self.assertEqual(check_rules.check_privacy("a.md", "The owner kept it."), [])


if __name__ == "__main__":
    unittest.main()
