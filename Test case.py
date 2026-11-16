"""Test cases for Duplicate Data Finder (one.py)

Run with:  python test_cases.py
"""

import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import one


def run_program(file_content, inputs, filename="data.txt"):
    """Run one.main() inside a temp folder with fake keyboard input.
    Returns (console_output, unique_file_text_or_None)."""
    old_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        try:
            if file_content is not None:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(file_content)
            buf = io.StringIO()
            with patch("builtins.input", side_effect=inputs), redirect_stdout(buf):
                one.main()
            unique_text = None
            if os.path.exists("unique.txt"):
                with open("unique.txt", encoding="utf-8") as f:
                    unique_text = f.read()
            return buf.getvalue(), unique_text
        finally:
            os.chdir(old_cwd)


class TestDuplicateDataFinder(unittest.TestCase):

    def test_case_1_normal_input(self):
        data = "apple\nbanana\napple\norange\nbanana\napple\n"
        out, unique = run_program(data, ["data.txt", "1"])
        self.assertIn("Total items: 6 | Unique items: 3", out)
        self.assertIn("Duplicates: apple (3 times) | banana (2 times)", out)
        self.assertIn("Unique list saved to unique.txt", out)
        self.assertEqual(unique.split(), ["apple", "banana", "orange"])

    def test_case_2_boundary_minimum_input(self):
        out, unique = run_program("apple\n", ["data.txt", "1"])
        self.assertIn("Total items: 1 | Unique items: 1", out)
        self.assertIn("No duplicates found.", out)
        self.assertEqual(unique.split(), ["apple"])

    def test_case_3a_invalid_file_not_found(self):
        out, unique = run_program("apple\n", ["dta.txt"])
        self.assertIn("File 'dta.txt' not found. Please enter a valid file name.", out)
        self.assertIsNone(unique)

    def test_case_3b_invalid_empty_file(self):
        out, unique = run_program("", ["data.txt"])
        self.assertIn("File is empty. Nothing to check.", out)
        self.assertIsNone(unique)

    def test_case_4_ignore_case_and_spaces(self):
        data = "Apple\napple\nbanana\nAPPLE\n"
        out, unique = run_program(data, ["data.txt", "2"])
        self.assertIn("Total items: 4 | Unique items: 2", out)
        self.assertIn("Duplicates: apple (3 times)", out)
        self.assertIn("Unique list saved to unique.txt", out)
        self.assertEqual(unique.split(), ["apple", "banana"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
