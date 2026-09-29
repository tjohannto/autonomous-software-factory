import unittest
import subprocess
import json
import sys
import tempfile
from pathlib import Path

from src.task_extractor.extractor import extract_tasks

class TestTaskExtractorUnit(unittest.TestCase):
    """SDET Tests gegen REQ-1 & ACs"""
    
    def test_req1_extract_open_tasks_standard(self):
        content = """
        # My Document
        - [ ] Task 1: Buy milk
        * [ ] Task 2: Call Alice
        - [x] Task 3: Already done
        * [X] Task 4: Also done
        Just some regular text.
        """
        tasks = extract_tasks(content)
        self.assertEqual(tasks, ["Task 1: Buy milk", "Task 2: Call Alice"])

    def test_req1_handles_indented_and_whitespace(self):
        content = """
          - [ ]   Indented task with extra spaces   
            * [ ] Subtask indented
        """
        tasks = extract_tasks(content)
        self.assertEqual(tasks, ["Indented task with extra spaces", "Subtask indented"])

    def test_req1_edge_case_empty_input(self):
        self.assertEqual(extract_tasks(""), [])
        self.assertEqual(extract_tasks("No tasks here at all"), [])

    def test_req1_edge_case_malformed_checkboxes(self):
        content = """
        - [] Missing space
        -[ ] Missing space before bracket
        - [ ]
        """
        tasks = extract_tasks(content)
        self.assertEqual(tasks, [])


class TestTaskExtractorCLI(unittest.TestCase):
    """SDET Tests gegen REQ-2, REQ-3 & CLI"""

    def test_req2_file_input(self):
        with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".md") as tmp:
            tmp.write("- [ ] Learn Antigravity\n- [x] Installed\n")
            tmp_path = tmp.name

        try:
            result = subprocess.run(
                [sys.executable, "-m", "src.task_extractor.cli", tmp_path],
                capture_output=True,
                text=True
            )
            self.assertEqual(result.returncode, 0)
            self.assertIn("1. Learn Antigravity", result.stdout)
            self.assertNotIn("Installed", result.stdout)
        finally:
            Path(tmp_path).unlink(missing_ok=True)

    def test_req2_file_not_found(self):
        result = subprocess.run(
            [sys.executable, "-m", "src.task_extractor.cli", "non_existent_file.md"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 1)
        self.assertTrue("Error" in result.stderr or "not found" in result.stderr.lower())

    def test_req3_json_output(self):
        with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".md") as tmp:
            tmp.write("- [ ] Task Alpha\n- [ ] Task Beta\n")
            tmp_path = tmp.name

        try:
            result = subprocess.run(
                [sys.executable, "-m", "src.task_extractor.cli", tmp_path, "--json"],
                capture_output=True,
                text=True
            )
            self.assertEqual(result.returncode, 0)
            parsed = json.loads(result.stdout)
            self.assertEqual(parsed, ["Task Alpha", "Task Beta"])
        finally:
            Path(tmp_path).unlink(missing_ok=True)

if __name__ == "__main__":
    unittest.main()
