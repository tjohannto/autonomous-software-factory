import unittest
import subprocess
import json
import io
import sys
import tempfile
from contextlib import redirect_stderr
from pathlib import Path
from unittest.mock import patch

from src.task_extractor.extractor import extract_tasks
from src.task_extractor.cli import main as cli_main

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

    def test_stdin_input_numbered_text_output(self):
        result = subprocess.run(
            [sys.executable, "-m", "src.task_extractor.cli"],
            input="- [ ] Learn Antigravity\n- [x] Installed\n* [ ] Write tests\n",
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "1. Learn Antigravity\n2. Write tests\n")

    def test_stdin_input_json_output(self):
        result = subprocess.run(
            [sys.executable, "-m", "src.task_extractor.cli", "--json"],
            input="- [ ] Task Alpha\n- [x] Task Done\n- [ ] Task Beta\n",
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), ["Task Alpha", "Task Beta"])

    def test_req2_file_not_found(self):
        result = subprocess.run(
            [sys.executable, "-m", "src.task_extractor.cli", "non_existent_file.md"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 1)
        self.assertTrue("Error" in result.stderr or "not found" in result.stderr.lower())
        self.assertNotIn("Traceback", result.stderr)

    def test_req2_permission_error_is_reported_without_traceback(self):
        stderr = io.StringIO()
        with (
            patch("sys.argv", ["cli", "unreadable.md"]),
            patch("src.task_extractor.cli.Path.exists", return_value=True),
            patch("src.task_extractor.cli.Path.is_file", return_value=True),
            patch(
                "src.task_extractor.cli.Path.read_text",
                side_effect=PermissionError("permission denied"),
            ),
            redirect_stderr(stderr),
        ):
            try:
                exit_code = cli_main()
            except PermissionError:
                exit_code = None

        with self.subTest("exit code"):
            self.assertEqual(exit_code, 1, "A file read error must return exit code 1")
        with self.subTest("readable error message"):
            self.assertIn("unreadable.md", stderr.getvalue())
            self.assertIn("error", stderr.getvalue().lower())
        with self.subTest("no traceback"):
            self.assertNotIn("Traceback", stderr.getvalue())

    def test_req2_invalid_utf8_is_reported_without_traceback(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as tmp:
            tmp.write(b"- [ ] Valid task\n\xff")
            tmp_path = tmp.name

        try:
            result = subprocess.run(
                [sys.executable, "-m", "src.task_extractor.cli", tmp_path],
                capture_output=True,
                text=True
            )
            self.assertEqual(
                result.returncode, 1, "Invalid UTF-8 must return exit code 1"
            )
            self.assertNotIn("Traceback", result.stderr)
            self.assertIn(tmp_path, result.stderr)
            self.assertIn("error", result.stderr.lower())
        finally:
            Path(tmp_path).unlink(missing_ok=True)

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
