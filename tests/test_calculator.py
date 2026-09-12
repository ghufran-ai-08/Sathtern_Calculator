"""Tests for the Calculator Application."""

import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, "src")

from calculator import (
    add,
    divide,
    get_menu_choice,
    get_number,
    multiply,
    subtract,
)


class TestCalculatorOperations(unittest.TestCase):
    """Test the calculator arithmetic operations."""

    def test_add(self):
        """Addition should return the correct sum."""

        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        """Subtraction should return the correct difference."""

        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        """Multiplication should return the correct product."""

        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        """Division should return the correct quotient."""

        self.assertEqual(divide(10, 5), 2)

    def test_divide_by_zero(self):
        """Division by zero should raise ValueError."""

        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_decimal_calculation(self):
        """Calculator operations should support decimal values."""

        self.assertEqual(add(2.5, 1.5), 4.0)

    def test_negative_numbers(self):
        """Calculator operations should support negative values."""

        self.assertEqual(add(-5, 10), 5)


class TestCalculatorInput(unittest.TestCase):
    """Test calculator input validation."""

    @patch("builtins.input", side_effect=["abc", "10.5"])
    def test_get_number_rejects_invalid_input(self, mock_input):
        """get_number should reject non-numeric input."""

        result = get_number("Enter number: ")

        self.assertEqual(result, 10.5)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", side_effect=["", "-7"])
    def test_get_number_rejects_empty_input(self, mock_input):
        """get_number should reject empty input."""

        result = get_number("Enter number: ")

        self.assertEqual(result, -7.0)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", side_effect=["hello", "3"])
    def test_get_menu_choice_rejects_invalid_input(self, mock_input):
        """get_menu_choice should reject invalid choices."""

        result = get_menu_choice()

        self.assertEqual(result, 3)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", side_effect=["9", "1"])
    def test_get_menu_choice_rejects_out_of_range(self, mock_input):
        """get_menu_choice should reject choices outside the menu."""

        result = get_menu_choice()

        self.assertEqual(result, 1)
        self.assertEqual(mock_input.call_count, 2)


if __name__ == "__main__":
    unittest.main()