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