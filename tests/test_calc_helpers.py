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

    def setUp(self):
        self.py_calc = PythonCalculator(10, 20)

    def test_sum(self):
        self.assertEqual(self.py_calc.sum(), 30,
                         "There is an issue calculating the sum!!")
    
    def test_dif(self):
        self.assertEqual(self.py_calc.dif(), -10,
                         "There is an issue calculating the difference!!")
        
    def test_mult(self):
        self.assertEqual(self.py_calc.mult(), 200,
                         "There is an issue calculating the product!!")
        
    def test_div(self):
        self.assertEqual(self.py_calc.div(), 0.5,
                         "There is an issue calfulating the quatient!!")
        
    
if __name__ == '__main__':
    unittest.main()
