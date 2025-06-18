# ------------------------------------------------------------------------------------------ #
# Title: presentation_classes.py
# Description: A module for presenting user interface elements and handling user interaction
# ChangeLog:
#   Sophia Brooks, 06/17/2025, Created script based on Assignment08-Starter.py
# ------------------------------------------------------------------------------------------ #

class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    Methods:
        output_error_messages(message, error)
        output_menu(menu)
        input_menu_choice()
        output_employee_data(employee_data)
        input_employee_data(employee_data, employee_type)

    ChangeLog:
        RRoot, 1.1.2030: Created class.
        Sophia Brooks, 06/17/2025: Verified for assignment structure.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None) -> None:
        """Displays a custom error message, and optionally a technical one."""
        print("\n" + message)
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str) -> None:
        """Displays the main menu."""
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice() -> str:
        """Prompts the user to choose a menu option (1–4)."""
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ").strip()
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please choose only 1, 2, 3, or 4.")
        except Exception as e:
            IO.output_error_messages("Invalid menu choice.", e)
        return choice

    @staticmethod
    def output_employee_data(employee_data: list) -> None:
        """Displays the current list of employees and their ratings."""
        print()
        print("-" * 50)
        for emp in employee_data:
            if emp.review_rating == 5:
                description = "(Leading)"
            elif emp.review_rating == 4:
                description = "(Strong)"
            elif emp.review_rating == 3:
                description = "(Solid)"
            elif emp.review_rating == 2:
                description = "(Building)"
            else:
                description = "(Not Meeting Expectations)"
            print(f"{emp.first_name} {emp.last_name} reviewed on {emp.review_date} is rated {emp.review_rating} {description}")
        print("-" * 50)
        print()

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: object) -> list:
        """Prompts the user to enter a new employee’s data, validates input, and appends it."""
        try:
            emp = employee_type()
            emp.first_name = input("Enter the employee's first name: ").strip()
            emp.last_name = input("Enter the employee's last name: ").strip()
            emp.review_date = input("Enter the review date (YYYY-MM-DD): ").strip()
            emp.review_rating = int(input("Enter the review rating (1–5): ").strip())
            employee_data.append(emp)
        except ValueError as e:
            IO.output_error_messages("Invalid value entered.", e)
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while entering employee data.", e)
        return employee_data
