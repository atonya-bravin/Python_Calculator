"""
This module contains a class that holds the helper
methods to help with calculations
"""


class PythonCalculator():
    """
    The class that holds the methods that help with the calculations
    """

    def sum(self, first_number: int, second_number: int) -> int:
        """
        This is a function that takes in two numbers
        and returns to us their sum
        """
        return first_number + second_number

    def dif(self, first_number: int, second_number: int) -> int:
        """
        This is a function that takes in two
        numbers and returns to us their difference
        """
        return first_number - second_number

    def mult(self, first_number: int, second_number: int) -> int:
        """
        This is a function that takes in two
        numbers and returns to us their product
        """
        return first_number * second_number

    def div(self, first_number: int, second_number: int) -> float:
        """
        This is a function that takes in two
        numbers and returns to us their quatient
        """
        return first_number / second_number

    def rem(self, first_number: int, second_number: int) -> int:
        """
        This is a function that takes in two numbers and returns to us the
        reminder after their division
        """
        return first_number % second_number
