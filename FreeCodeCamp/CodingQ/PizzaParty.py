""" 

Pizza Party
Given an array of hours worked today per person, return the number of pizzas to order for a pizza party.

Divide each person's hours worked by 3 to get their slice count.
You can't eat a partial slice, so round each person's slice count up to the nearest whole number.
Each person gets a minimum of two slices.
Each pizza has 8 slices. Round the total number of pizzas up to the nearest whole pizza.
"""


import unittest


class PizzaPartyTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_pizzas_to_order([8, 8, 8]), 2)

    def test2(self):
        self.assertEqual(get_pizzas_to_order([10, 9, 8, 2, 2, 6, 10]), 3)

    def test3(self):
        self.assertEqual(get_pizzas_to_order([1, 2, 3, 4, 5]), 2)

    def test4(self):
        self.assertEqual(get_pizzas_to_order([8, 8, 8, 8, 8, 8, 8, 8]), 3)

    def test5(self):
        self.assertEqual(get_pizzas_to_order([9, 9, 6]), 1)

    def test6(self):
        self.assertEqual(get_pizzas_to_order([10, 12, 16, 9, 8, 11, 15, 8, 0]), 5)


TESTCASES = [
    (([8, 8, 8],), 2),
    (([10, 9, 8, 2, 2, 6, 10],), 3),
    (([1, 2, 3, 4, 5],), 2),
    (([8, 8, 8, 8, 8, 8, 8, 8],), 3),
    (([9, 9, 6],), 1),
    (([10, 12, 16, 9, 8, 11, 15, 8, 0],), 5)
]




import math
def get_pizzas_to_order(hours_worked):


    total_slices = 0

    for hour in hours_worked:
        slices = math.ceil(hour / 3)
        slices = max(slices, 2)

        total_slices += slices

    return math.ceil(total_slices / 8)




from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": get_pizzas_to_order},
        TESTCASES,
        10000
    )
    unittest.main()