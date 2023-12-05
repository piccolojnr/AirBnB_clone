"""
    test_console
"""
from io import StringIO
import os
import unittest

from unittest.mock import patch
import console
import pep8
from models.engine.file_storage import FileStorage


class test_console_prompt(unittest.TestCase):
    """
    test console prompt
    """

    @classmethod
    def setUpClass(self):
        """Set up test"""
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = ["console.py"]
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, "Need to fix Pep8")

    def test_docstrings_in_console(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", console.HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(console.HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
