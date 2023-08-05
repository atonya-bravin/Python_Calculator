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
            # check to validate that the operand is a valid integer
            try:
                operand = int(complete_list[index])
                operands.append(operand)
            except ValueError:
                operand = complete_list[index]
                print(f"Value Error: {operand} not an number")

        # a list of acceptable operands
        acceptable_operators = ["/", "*", "+", "-"]

        # check if any of the acceptable operators appears in the operands list
        # If it appears, it means that two operators followed each other

        for index in range(len(complete_list)):
            if complete_list[index] in acceptable_operators and index % 2 == 0:
                first_operator = complete_list[index - 1]
                second_operator = complete_list[index]
                print(f"Syntax Error: Operators {first_operator} {second_operator}")
                exit(1)

        # Inserts the operator into the operators list
        for index in range(1, len(complete_list), 2):            
            if complete_list[index] in acceptable_operators:
                operators.append(complete_list[index])

            else:
                print(f"Syntax Error: {complete_list[index]} is not a known operator")
                exit(1)

        # dictionaty that we can return to our main program to
        # maintain our abstraction
        super_list = {"operands": operands, "operators": operators}
        
        return super_list