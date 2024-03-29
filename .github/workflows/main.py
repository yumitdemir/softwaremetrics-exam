import unittest
import math
from typing import Union


class MathFunctions:
    """
    A class containing mathematical functions.
    """

    def degrees(self, radians: Union[int, float]) -> float:
        """
        Convert radians to degrees.

        Args:
            radians (Union[int, float]): The angle in radians.

        Returns:
            float: The angle in degrees.

        Raises:
            TypeError: If the input is not a valid numeric type.
        """
        if radians is None:
            raise TypeError("Input cannot be None.")
        if not isinstance(radians, (int, float)):
            raise TypeError("Input must be a numeric type (int or float).")

        return math.degrees(radians)

class TestMathFunctions(unittest.TestCase):
    """
    Unit tests for MathFunctions class.
    """

    def setUp(self) -> None:
        """
        Set up the test fixture.
        """
        self.math_funcs = MathFunctions()

    def test_degrees(self) -> None:
        """
        Test the degrees function with a valid input.
        """
        result = self.math_funcs.degrees(math.pi)
        self.assertEqual(result, 180)

    def test_degrees_with_invalid_input(self) -> None:
        """
        Test the degrees function with an invalid input.
        """
        with self.assertRaises(TypeError):
            self.math_funcs.degrees("invalid_input")

    def test_degrees_with_negative_value(self) -> None:
        """
        Test the degrees function with a negative input.
        """
        result = self.math_funcs.degrees(-math.pi)
        self.assertEqual(result, -180)

    def test_degrees_with_zero(self) -> None:
        """
        Test the degrees function with zero radians.
        """
        result = self.math_funcs.degrees(0)
        self.assertEqual(result, 0)

    def test_degrees_with_positive_value(self) -> None:
        """
        Test the degrees function with a positive input.
        """
        result = self.math_funcs.degrees(3 * math.pi / 2)
        self.assertEqual(result, 270)

    def test_degrees_with_large_value(self) -> None:
        """
        Test the degrees function with a large input.
        """
        result = self.math_funcs.degrees(10 * math.pi)
        self.assertEqual(result, 1800)

    def test_degrees_with_float_input(self) -> None:
        """
        Test the degrees function with a floating-point input.
        """
        result = self.math_funcs.degrees(0.5 * math.pi)
        self.assertEqual(result, 90)

    def test_degrees_with_none_input(self) -> None:
        """
        Test the degrees function with a None input.
        """
        with self.assertRaises(TypeError):
            self.math_funcs.degrees(None)

if __name__ == '__main__':
    unittest.main()
