# ------------------------------------------------------------------------------------------ #
# Title: test_processing_classes.py
# Description: Unit tests for FileProcessor methods
# ChangeLog:
#   Sophia Brooks, 06/17/2025, Created test script for Assignment08
# ------------------------------------------------------------------------------------------ #

#Testing FileProcessor methods

import unittest
import os
import json
from processing_classes import FileProcessor
from data_classes import Employee


class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        """Creates a temporary test file and sample employee list"""
        self.test_file = "test_employees.json"
        self.test_employees = [
            Employee("John", "Doe", "2023-05-01", 4),
            Employee("Jane", "Smith", "2023-06-15", 5)
        ]
        # Write initial data manually for read test
        with open(self.test_file, "w") as f:
            json.dump([
                {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2023-05-01", "ReviewRating": 4},
                {"FirstName": "Jane", "LastName": "Smith", "ReviewDate": "2023-06-15", "ReviewRating": 5}
            ], f)

    def tearDown(self):
        """Cleans up the temporary test file"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_employee_data_from_file(self):
        employee_list = []
        result = FileProcessor.read_employee_data_from_file(self.test_file, employee_list, Employee)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].first_name, "John")
        self.assertEqual(result[1].review_rating, 5)

    def test_write_employee_data_to_file(self):
        FileProcessor.write_employee_data_to_file(self.test_file, self.test_employees)
        with open(self.test_file, "r") as f:
            data = json.load(f)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["FirstName"], "John")
        self.assertEqual(data[1]["ReviewRating"], 5)


if __name__ == "__main__":
    unittest.main()
