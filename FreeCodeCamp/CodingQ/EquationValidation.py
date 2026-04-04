""" 

Equation Validation
Given a string representing a math equation, determine whether it is correct.

The left side may contain up to three positive integers and the operators +, -, *, and /.
The equation will be given in the format: "number operator number = number" (with two or three numbers on the left). For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
The right side will always be a single integer.
Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from left-to-right.
"""

import unittest

class EquationValidationTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_valid_equation("2 + 2 = 4"), True)

    def test2(self):
        self.assertEqual(is_valid_equation("2 + 3 - 1 = 4"), True)

    def test3(self):
        self.assertEqual(is_valid_equation("8 / 2 = 4"), True)

    def test4(self):
        self.assertEqual(is_valid_equation("10 * 5 = 50"), True)

    def test5(self):
        self.assertEqual(is_valid_equation("2 - 2 = 0"), True)

    def test6(self):
        self.assertEqual(is_valid_equation("2 + 9 / 3 = 5"), True)

    def test7(self):
        self.assertEqual(is_valid_equation("20 - 2 * 3 = 14"), True)

    def test8(self):
        self.assertEqual(is_valid_equation("2 + 5 = 6"), False)

    def test9(self):
        self.assertEqual(is_valid_equation("10 - 2 * 3 = 24"), False)

    def test10(self):
        self.assertEqual(is_valid_equation("3 + 9 / 3 = 4"), False)



def is_valid_equation_first(equation):
    equation, result = equation.split("= ")


    return eval(equation) == int(result)

def is_valid_equation(equation):

    left, right = equation.split("=")
    right_val = int(right.strip())

    tokens = equation.strip().split()

    stack = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ("*","/"):
            prev = stack.pop()
            next_num = int(tokens[i + 1])
            if token == "*":
                stack.append(prev * next_num)
            else:
                stack.append(prev // next_num)
            i += 2

        else:
            if token.isdigit():
                stack.append(int(token))
            else:
                stack.append(token)
            i += 1
    

    result = stack[0]
    i = 1
    while i < len(stack):
        op = stack[i]
        num = stack[i + 1]
        if op == "+":
            result += num
        elif op == "-":
            result -= num
        i += 2


    return result == right_val






from utils.benchmark import benchmark

if __name__ == "__main__":
    TESTCASES = [
    (("2 + 2 = 4",), True),
    (("2 + 3 - 1 = 4",), True),
    (("8 / 2 = 4",), True),
    (("10 * 5 = 50",), True),
    (("2 - 2 = 0",), True),
    (("2 + 9 / 3 = 5",), True),
    (("20 - 2 * 3 = 14",), True),
    (("2 + 5 = 6",), False),
    (("10 - 2 * 3 = 24",), False),
    (("3 + 9 / 3 = 4",), False)
]
    scores = benchmark(
        {"first": is_valid_equation_first,
         "second": is_valid_equation},
        TESTCASES,
        10000
    )
    unittest.main()
