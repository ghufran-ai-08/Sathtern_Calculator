"""Calculator Application.

A menu-driven calculator built for the Sathtern Python
Development Internship.
"""


def add(first_number, second_number):
    """Return the sum of two numbers."""

    return first_number + second_number


def subtract(first_number, second_number):
    """Return the difference between two numbers."""

    return first_number - second_number


def multiply(first_number, second_number):
    """Return the product of two numbers."""

    return first_number * second_number


def divide(first_number, second_number):
    """Return the quotient of two numbers."""

    if second_number == 0:
        raise ValueError("Cannot divide by zero.")

    return first_number / second_number


def get_number(prompt):
    """Prompt the user for a valid numeric value."""

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Invalid input. Please enter a number.")
            continue

        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_menu_choice():
    """Prompt the user for a valid calculator menu choice."""

    while True:
        choice = input("Enter your choice (1-5): ").strip()

        if choice in {"1", "2", "3", "4", "5"}:
            return int(choice)

        print("Invalid choice. Please select an option from 1 to 5.")