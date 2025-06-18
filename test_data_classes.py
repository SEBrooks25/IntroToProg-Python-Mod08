# ------------------------------------------------------------------------------------------ #
# Title: test_data_classes.py
# Description: Unit tests for Person and Employee classes
# ChangeLog:
#   Sophia Brooks, 06/17/2025, Created test script for Assignment08
# ------------------------------------------------------------------------------------------ #

#Test "Person" and "Employee" classes from data_classes.py

import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):
    def test_valid_names(self):
        p = Person("Grace", "Johnson")
        self.assertEqual(p.first_name, "Grace")
        self.assertEqual(p.last_name, "Johnson")

    def test_invalid_first_name(self):
        with self.assertRaises(ValueError):
            Person("Gr@ce", "Smith")

    def test_invalid_last_name(self):
        with self.assertRaises(ValueError):
            Person("Bob", "Sm1th")

    def test_str_output(self):
        p = Person("Bob", "Smith")
        self.assertEqual(str(p), "Bob,Smith")


class TestEmployee(unittest.TestCase):
    def test_default_values(self):
        e = Employee()
        self.assertEqual(e.first_name, "")
        self.assertEqual(e.last_name, "")
        self.assertEqual(e.review_date, "1900-01-01")
        self.assertEqual(e.review_rating, 3)

    def test_valid_data(self):
        e = Employee("Charlie", "Brown", "2024-10-15", 5)
        self.assertEqual(e.review_date, "2024-10-15")
        self.assertEqual(e.review_rating, 5)

    def test_invalid_review_date(self):
        with self.assertRaises(ValueError):
            Employee("Dana", "White", "15-10-2024", 4)

    def test_invalid_review_rating(self):
        with self.assertRaises(ValueError):
            Employee("Eve", "Black", "2024-10-15", 6)

    def test_str_output(self):
        e = Employee("Alice", "Green", "2024-12-01", 4)
        self.assertEqual(str(e), "Alice,Green,2024-12-01,4")


if __name__ == "__main__":
    unittest.main()
