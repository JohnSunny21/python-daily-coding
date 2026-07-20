""" 

Golden Ratio
Given two numbers, determine if their ratio approximates the golden ratio.

Use a golden ratio of 1.618
Allow a tolerance of 0.01
"""


import unittest

class GoldenRatioTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(is_golden_ratio(21, 34), True)

    def test2(self):
        self.assertEqual(is_golden_ratio(15, 20), False)

    def test3(self):
        self.assertEqual(is_golden_ratio(8, 13), True)

    def test4(self):
        self.assertEqual(is_golden_ratio(10, 16), False)

    def test5(self):
        self.assertEqual(is_golden_ratio(1618, 1000), True)

    def test6(self):
        self.assertEqual(is_golden_ratio(88, 55), False)


TESTCASES = [
    ((21, 34,), True),
    ((15, 20,), False),
    ((8, 13,), True),
    ((10, 16,), False),
    ((1618, 1000,), True),
    ((88, 55,), False)
]


def is_golden_ratio_wrong(a, b):

    golden_ratio = 1.618

    a = a * golden_ratio

    return b - a <= 0.01

"""
=> The above solution is wrong. Right now we are multiplying a by 1.618 and then checking if b - a <= 0.01
    That doesn't actually test whether the ratio of a and b is close to the golden ratio = it just compares a scaled version of a to b.

    The golden ratio is 
        ratio = max(a, b) / min(a, b)

    Then check if: 
        |ratio - 1.618| <= 0.01 
        This is correct solution

"""



def is_golden_ratio(a, b):

    golden_ratio = 1.618
    tolerance = 0.01

    # Ensure the ratio must be >= 1
    ratio = max(a, b) / min(a, b)

    return abs(ratio - golden_ratio) <= tolerance







from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": is_golden_ratio}, TESTCASES, 10000)
    unittest.main()