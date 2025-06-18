# ------------------------------------------------------------------------------------------ #
# Title: processing_classes.py
# Description: A module for processing employee data to and from a JSON file
# ChangeLog:
#   Sophia Brooks, 06/17/2025, Created script based on Assignment08-Starter.py
# ------------------------------------------------------------------------------------------ #

#Handle file reading and writing

import json
from data_classes import Employee

class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    Methods:
        read_employee_data_from_file(file_name, employee_data, employee_type)
        write_employee_data_to_file(file_name, employee_data)

    ChangeLog:
        RRoot, 1.1.2030: Created class.
        Sophia Brooks, 06/17/2025: Modified for assignment criteria.
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object) -> list:
        """
        Reads employee data from a JSON file into a list of Employee objects.

        :param file_name: The name of the JSON file.
        :param employee_data: The list to populate with Employee objects.
        :param employee_type: A reference to the Employee class.

        :return: A list of Employee objects.
        """
        try:
            with open(file_name, "r") as file:
                list_of_dicts = json.load(file)
                for emp in list_of_dicts:
                    emp_obj = employee_type()
                    emp_obj.first_name = emp["FirstName"]
                    emp_obj.last_name = emp["LastName"]
                    emp_obj.review_date = emp["ReviewDate"]
                    emp_obj.review_rating = emp["ReviewRating"]
                    employee_data.append(emp_obj)
        except FileNotFoundError as e:
            from presentation_classes import IO
            IO.output_error_messages("File not found. Make sure the data file exists.", e)
        except Exception as e:
            from presentation_classes import IO
            IO.output_error_messages("An unexpected error occurred while reading the file.", e)
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list) -> None:
        """
        Writes employee data from a list of Employee objects to a JSON file.

        :param file_name: The name of the JSON file.
        :param employee_data: The list of Employee objects to write.

        :return: None
        """
        try:
            list_of_dicts = []
            for emp in employee_data:
                emp_dict = {
                    "FirstName": emp.first_name,
                    "LastName": emp.last_name,
                    "ReviewDate": emp.review_date,
                    "ReviewRating": emp.review_rating
                }
                list_of_dicts.append(emp_dict)

            with open(file_name, "w") as file:
                json.dump(list_of_dicts, file)

        except TypeError as e:
            from presentation_classes import IO
            IO.output_error_messages("Invalid data type encountered when saving to file.", e)
        except PermissionError as e:
            from presentation_classes import IO
            IO.output_error_messages("Permission denied when writing to file.", e)
        except Exception as e:
            from presentation_classes import IO
            IO.output_error_messages("An unexpected error occurred while writing to the file.", e)





























