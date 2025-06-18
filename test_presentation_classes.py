# ------------------------------------------------------------------------------------------ #
# Title: test_presentation_classes.py
# Description: Unit tests for IO class methods
# ChangeLog:
#   Sophia Brooks, 06/17/2025, Created test script for Assignment08
# ------------------------------------------------------------------------------------------ #

#Testing key methods in IO class

import unittest
from unittest.mock import patch
from io import StringIO
from presentation_classes import IO
from data_classes import Employee


class TestIO(unittest.TestCase):

    def test_output_error_messages_with_exception(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            IO.output_error_messages("Something went wrong.", ValueError("Bad input"))
            output = fake_out.getvalue()
            self.assertIn("Something went wrong.", output)
            self.assertIn("Bad input", output)

    def test_output_menu(self):
        menu = "1. Option 1\n2. Option 2"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            IO.output_menu(menu)
            self.assertIn("1. Option 1", fake_out.getvalue())

    def test_input_menu_choice_valid(self):
        with patch('builtins.input', return_value="2"):
            result = IO.input_menu_choice()
            self.assertEqual(result, "2")

    def test_input_menu_choice_invalid(self):
        with patch('builtins.input', return_value="9"), patch('sys.stdout', new=StringIO()) as fake_out:
            IO.input_menu_choice()
            output = fake_out.getvalue()
            self.assertIn("Invalid menu choice", output)

    def test_output_employee_data(self):
        employees = [
            Employee("Alice", "Smith", "2024-01-01", 5),
            Employee("Bob", "Jones", "2024-02-15", 3)
        ]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            IO.output_employee_data(employees)
            output = fake_out.getvalue()
            self.assertIn("Alice Smith", output)
            self.assertIn("rated 3", output)


if __name__ == "__main__":
    unittest.main()
