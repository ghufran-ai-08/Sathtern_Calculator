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


def display_menu():
    """Display the calculator menu."""

    print("\n" + "-" * 45)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("-" * 45)

def perform_calculation(choice, first_number, second_number):
    """Perform the calculation selected by the user."""

    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
    }

    operation = operations.get(choice)

    if operation is None:
        raise ValueError("Invalid calculation choice.")

    return operation(first_number, second_number)


def main():
    """Run the calculator application."""

    print("=" * 45)
    print("          CALCULATOR APPLICATION")
    print("=" * 45)

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 5:
            print("\nThank you for using Calculator Application.")
            break

        first_number = get_number("Enter first number: ")
        second_number = get_number("Enter second number: ")

        try:
            result = perform_calculation(
                choice,
                first_number,
                second_number,
            )
        except ValueError as error:
            print(f"\nError: {error}")
            continue

        print("\n" + "-" * 45)
        print(f"Result: {result}")
        print("-" * 45)


if __name__ == "__main__":
    main()