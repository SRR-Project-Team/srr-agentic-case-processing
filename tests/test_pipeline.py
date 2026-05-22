from __future__ import annotations

from pathlib import Path
import unittest

from srr_public import run_pipeline


ROOT = Path(__file__).resolve().parents[1]


class PipelineTest(unittest.TestCase):
    def test_full_synthetic_case(self) -> None:
        raw = (ROOT / "examples" / "synthetic_case.txt").read_text(encoding="utf-8")
        result = run_pipeline(raw)

        fields = result["fields"]
        self.assertEqual(fields["case_number"], "DEMO-2026-0001")
        self.assertEqual(fields["subject_matter"], "Fallen Tree")
        self.assertEqual(fields["ten_day_due"], "26-Jan-2026")
        self.assertEqual(fields["works_completion_due"], "20-Jan-2026")
        self.assertEqual(result["department_routing"]["department"], "Tree Management Team")
        self.assertGreaterEqual(result["quality"]["score"], 0.85)

    def test_minimal_case_gets_repaired(self) -> None:
        raw = (ROOT / "examples" / "synthetic_case_minimal.txt").read_text(encoding="utf-8")
        result = run_pipeline(raw)

        fields = result["fields"]
        self.assertEqual(fields["request_type"], "Urgent")
        self.assertEqual(fields["subject_matter"], "Hazardous Tree")
        self.assertTrue(result["repair_log"])
        self.assertEqual(result["department_routing"]["department"], "Tree Management Team")


if __name__ == "__main__":
    unittest.main()

