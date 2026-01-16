"""  

Integer Hypotenuse
Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle, determine whether the hypotenuse is an integer.

The length of the hypotenuse is calculated by adding the squares of the two leg lengths together and then taking the square root of that total (a2 + b2 = c2).
"""

import math, unittest

class IntegerHypotenuseTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_integer_hypotenuse(3, 4), True)

    def test2(self):
        self.assertEqual(is_integer_hypotenuse(2, 3), False)

    def test3(self):
        self.assertEqual(is_integer_hypotenuse(5, 12), True)

    def test4(self):
        self.assertEqual(is_integer_hypotenuse(10, 10), False)

    def test5(self):
        self.assertEqual(is_integer_hypotenuse(780, 1040), True)

    def test6(self):
        self.assertEqual(is_integer_hypotenuse(250, 333), False)


def is_integer_hypotenuse(a, b):
    
    c = math.sqrt(a**2 + b**2)

    return c.is_integer()


"""
=> This is essentially checking if (a, b, c) form a Pythagorean triple.
=> .is_integer() in Python or Number.isInteger() in JS ensures the hypotenuse is a whole number.
=> Example of integer hypotenuses: (3, 4, 5), (5, 12, 13), (8, 15, 17).
"""
if __name__ == "__main__":
    print(is_integer_hypotenuse(3, 4))
    unittest.main()