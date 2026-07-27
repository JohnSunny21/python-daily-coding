"""

Pronic Number
Given a number, determine whether it is a pronic number.

A pronic number is the product of two consecutive integers. For example, 6 is pronic because 2 * 3 = 6.
"""


import unittest


class PronicNumberTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(is_pronic(6), True)

    def test2(self):
        self.assertEqual(is_pronic(15), False)

    def test3(self):
        self.assertEqual(is_pronic(12), True)

    def test4(self):
        self.assertEqual(is_pronic(132), True)

    def test5(self):
        self.assertEqual(is_pronic(80), False)

    def test6(self):
        self.assertEqual(is_pronic(0), True)


TESTCASES = [
    ((6,), True),
    ((15,), False),
    ((12,), True),
    ((132,), True),
    ((80,), False),
    ((0,), True)
]



def is_pronic(n):

    if n <= 0:
        return True

    for i in range(1, n):
        if i * ( i + 1) == n:
            return True

    return False
"""

            ISSUE WITH THE ABOVE CODE
=> Treating n <= 0 as pronic
    -> By definition, only 0 is pronic.
    -> Negative numbers are not pronic.
    -> So the check should be if n =- 0: return True

=> Loop range
    -> In python we used range(1, n). That skips 0 case and also loops too far( no need to check all the way up to n).
    -> you only  need to loop up to sqrt(n) becasue beyond that i * ( i + 1) will exceed n.
"""

def is_pronic2(n):

    i = 0
    while i * (i + 1) <= n:
        if i * (i + 1) == n:
            return True

        i += 1

    return False







from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark({"first": is_pronic, "second": is_pronic2}, TESTCASES, 1000)
    unittest.main()