"""
This is a module that contains the Evaluator method,
that contains methods to evaluate and make something
useful out of the equation
"""

class Evaluator():
    def __init__(self, equation:int):
        self.equation = equation

    def equation_intersector(self)-> dict:
        """
        This is a function that intersects the provided
        string and appends the operands and the operators in the 
        respective lists
        """

        # this is the list that holds the operands i.e the numbers
        operands = []

        # this is the list that holds the operators
        operators = []

        # This is a list that contains both the operands and the opeators
        complete_list = self.equation.split()

        # The for loops that loop through the complete list to
        # insert the items into the appropriate list

        # Inserts the operands into the operands list
        for index in range(0, len(complete_list), 2):
            operands.append(complete_list[index])

        # Inserts the operator into the operators list
        for index in range(1, len(complete_list), 2):
            operators.append(complete_list[index])

        # dictionaty that we can return to our main program to
        # maintain our abstraction
        super_list = {"operands": operands, "operators": operators}
        
        return super_list