"""
This is a module containing the tests of
all the calculator's helper functions
"""
from python_calculator_helpers.python_calculator import PythonCalculator
import unittest
from unittest import TestCase


class CalculatorHelpersTester(TestCase):
    """
    This is a class that holds all the tests to the
    helper methods of our calculator
    """

    py_calc = PythonCalculator(10, 20)

    def test_sum(self):
        self.assertEqual(self.py_calc.sum(), 30,
                         "There is an issue calculating the sum!!")


if __name__ == '__main__':
    unittest.main()
