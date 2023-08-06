from equation_evaluator import Evaluator
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


class calc():
    def calculate(self, operands, operators):
        """
        This is the method that uses the BODMAS property to call in all the
        other mathematical functions above to perform the computation of the
        equation provided
        """

        operator_sequence = ["of", "/", "*", "+", "-"]
        result = 0

        # Create a BODMAS experience
        # loop through the operator sequence, taking in each operator
        # in the sequence and conducting all it's operations before moving to the next one.
        for index in range(len(operator_sequence)):
            current_operator = operator_sequence[index]
            while current_operator in operators:
                operator_index = operators.index(current_operator)
                # if the operator is at index 0
                # then the first number has the same index in the operands list
                if operator_index == 0:
                    first_number = operands[operator_index]
                elif operators[0] != current_operator:
                    # This makes sure that the that we do not take the first number in the
                    # operands list as the first number unless the operator associated to it
                    # is the current operator in the loop
                    first_number = operands[operator_index]
                else:
                    first_number = operands[operator_index - 1]
                second_number = operands[operator_index + 1]
                
                # remove the first number of the equation from the list
                # This is to make susre that the result of the simple equation is in its position
                operands.pop(operator_index)

                # remove the operator that we have just used
                operators.pop(operator_index)

                # make sure that incase a negative sign is before the number,
                # the number is posted to the relevant method along with its signage
                if len(operators) > 0 and operators[operator_index - 1] == "-":
                    first_number = first_number * (-1)

                # create a simple_equation object to call all the methods from
                simple_equation = PythonCalculator(first_number, second_number)

                if current_operator == "+":
                    operands[operator_index] = simple_equation.sum()
                    #if the result from the sum method is > 0 
                    # then the sign should be changed to +
                    # this will basically affect the negative numbers
                    if operands[operator_index] > 0 and len(operands) > 1:
                        operators[operator_index  - 1] = "+"
                elif current_operator == "-":
                    operands[operator_index] = simple_equation.dif()
                elif current_operator == "*" or current_operator == "of":
                    operands[operator_index] = simple_equation.mult()
                elif current_operator == "/":
                    operands[operator_index] = simple_equation.div()
                result = operands[operator_index]
        return result        

if __name__ == "__main__":
    equation = input("Enter your Equation: ")
    math_equation = Evaluator(equation)
    equation_items = math_equation.equation_intersector()
    operands = equation_items['operands']
    operators = equation_items['operators']
    calculator = calc()
    print(calculator.calculate(operands, operators))
