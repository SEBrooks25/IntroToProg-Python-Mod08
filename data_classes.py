# ------------------------------------------------------------------------------------------ #
# Title: data_classes.py
# Description: A module for managing Person and Employee data classes
# ChangeLog:
#   Sophia Brooks, 06/17/2025, Created script based on Assignment08-Starter.py
# ------------------------------------------------------------------------------------------ #

#Defining "Person" and "Employee" classes

from datetime import date

class Person:
    """
    A class representing person data.

    Properties:
        first_name (str): The person's first name.
        last_name (str): The person's last name.

    ChangeLog:
        RRoot, 1.1.2030: Created the class.
        Sophia Brooks, 06/17/2025: Edited for assignment criteria.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self) -> str:
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers or special characters.")

    @property
    def last_name(self) -> str:
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers or special characters.")

    def __str__(self) -> str:
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """
    A class representing employee data.

    Properties:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        review_date (str): The date of the employee review in YYYY-MM-DD.
        review_rating (int): The performance review rating (1-5).

    ChangeLog:
        RRoot, 1.1.2030: Created the class.
        Sophia Brooks, 06/17/2025: Edited for assignment criteria.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):
        super().__init__(first_name, last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self) -> str:
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Review date must be in YYYY-MM-DD format.")

    @property
    def review_rating(self) -> int:
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        if isinstance(value, int) and value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Review rating must be an integer between 1 and 5.")

    def __str__(self) -> str:
        return f"{self.first_name},{self.last_name},{self.review_date},{self.review_rating}"
