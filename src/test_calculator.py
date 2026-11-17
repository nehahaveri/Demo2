import unittest

from calculator import calculator


class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(calculator("add", 2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(calculator("add", -2, -3), -5)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(calculator("add", -2, 3), 1)

    def test_add_floats(self):
        self.assertAlmostEqual(calculator("add", 0.1, 0.2), 0.3)

    def test_subtract_positive_numbers(self):
        self.assertEqual(calculator("subtract", 5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(calculator("subtract", -2, -3), 1)

    def test_subtract_result_negative(self):
        self.assertEqual(calculator("subtract", 3, 5), -2)

    def test_subtract_floats(self):
        self.assertAlmostEqual(calculator("subtract", 1.5, 0.5), 1.0)

    def test_multiply_positive_numbers(self):
        self.assertEqual(calculator("multiply", 4, 3), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(calculator("multiply", 7, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(calculator("multiply", -2, 3), -6)

    def test_divide_positive_numbers(self):
        self.assertEqual(calculator("divide", 6, 3), 2)

    def test_divide_returns_float(self):
        self.assertAlmostEqual(calculator("divide", 6, 4), 1.5)

    def test_divide_negative_numbers(self):
        self.assertEqual(calculator("divide", -6, 3), -2)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculator("divide", 1, 0)

    def test_invalid_operation_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculator("modulo", 2, 3)

    def test_empty_operation_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculator("", 2, 3)


if __name__ == "__main__":
    unittest.main()
