"""
This module contains a class that holds the helper
methods to help with calculations
"""


class PythonCalculator():
    """
    The class that holds the methods that help with the calculations
    """

    def __init__(self, first_number: int, second_number: int):
        self.first_number = first_number
        self.second_number = second_number


    def sum(self) -> int:
        """
        This is a function that takes in two numbers
        and returns to us their sum
        """
        return self.first_number + self.second_number

    def dif(self) -> int:
        """
        This is a function that takes in two
        numbers and returns to us their difference
        """
        return self.first_number - self.second_number

    def mult(self) -> int:
        """
        This is a function that takes in two
        numbers and returns to us their product
        """
        return self.first_number * self.second_number

    def div(self) -> float:
        """
        This is a function that takes in two
        numbers and returns to us their quatient
        """
        return self.first_number / self.second_number

    def rem(self) -> int:
        """
        This is a function that takes in two numbers and returns to us the
        reminder after their division
        """
        return self.first_number % self.second_number
