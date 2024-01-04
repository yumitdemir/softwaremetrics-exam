import unittest
import math

class MathFunctions:
    def degrees(self, radians):
        return math.degrees(radians)

class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        self.math_funcs = MathFunctions()

    def test_degrees(self):
        result = self.math_funcs.degrees(math.pi)
        self.assertEqual(result, 180)

    def test_degrees_with_invalid_input(self):
        with self.assertRaises(TypeError):
            self.math_funcs.degrees("invalid_input")

    def test_degrees_with_negative_value(self):
        result = self.math_funcs.degrees(-math.pi)
        self.assertEqual(result, -180)

    def test_degrees_with_zero(self):
        result = self.math_funcs.degrees(0)
        self.assertEqual(result, 0)

    def test_degrees_with_positive_value(self):
        result = self.math_funcs.degrees(3 * math.pi / 2)
        self.assertEqual(result, 270)

    def test_degrees_with_large_value(self):
        result = self.math_funcs.degrees(10 * math.pi)
        self.assertEqual(result, 1800)

    def test_degrees_with_float_input(self):
        result = self.math_funcs.degrees(0.5 * math.pi)
        self.assertEqual(result, 90)

if __name__ == '__main__':
    unittest.main()
