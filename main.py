# ------------------------------------------------------------------------------------------ #
# Title: main.py
# Description: A script to run the Employee Review Rating application
# ChangeLog:
#   Sophia Brooks, 06/17/2025, Created script based on Assignment08-Starter.py
# ------------------------------------------------------------------------------------------ #

from data_classes import Employee
from processing_classes import FileProcessor
from presentation_classes import IO

# Constants
FILE_NAME: str = "EmployeeRatings.json"

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

# Variables
employees: list = []
menu_choice = ""

# Load data at program start
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)

# Repeat the following tasks until user exits
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Show data
        IO.output_employee_data(employee_data=employees)

    elif menu_choice == "2":  # Enter new data
        employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
        IO.output_employee_data(employee_data=employees)

    elif menu_choice == "3":  # Save to file
        FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
        print(f"\nData has been saved to {FILE_NAME}.\n")

    elif menu_choice == "4":  # Exit
        print("Goodbye!")
        break
