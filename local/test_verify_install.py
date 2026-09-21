import unittest

from verify_install import compare, files, sources


class VerificationTests(unittest.TestCase):
    def test_exact_snapshot_is_clean(self):
        self.assertFalse(any(compare({"SKILL.md": "abc"}, {"SKILL.md": "abc"}).values()))

    def test_changed_bytes_fail_even_with_same_file_names(self):
        self.assertEqual(compare({"SKILL.md": "abc"}, {"SKILL.md": "abd"})["changed"], ["SKILL.md"])

    def test_missing_reference_and_stale_file_are_both_detected(self):
        self.assertEqual(compare({"ref.md": "abc"}, {"old.md": "abc"}), {"missing": ["ref.md"], "extra": ["old.md"], "changed": []})

    def test_real_source_includes_metadata_and_references(self):
        snapshot = files(sources()["code-review"])
        self.assertIn("agents/openai.yaml", snapshot)
        self.assertIn("SMELLS.md", snapshot)
        self.assertIn("SKILL.md", snapshot)


if __name__ == "__main__":
    unittest.main()
