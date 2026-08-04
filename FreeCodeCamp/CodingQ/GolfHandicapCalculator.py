""" 
Golf Handicap Calculator
Given an array of golf scores and a corresponding array of course par values, return the golfer's handicap index using the following method:

Calculate the differential for each round by subtracting the par from the score, then return the average of all differentials rounded to one decimal place.
"""



import unittest

class GolfHandicapCalculatorTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(calculate_handicap([72, 72, 72], [72, 72, 72]), 0)

    def test2(self):
        self.assertEqual(calculate_handicap([80, 76, 78, 78], [72, 72, 72, 72]), 6)

    def test3(self):
        self.assertEqual(calculate_handicap([42, 45, 46, 44], [36, 36, 36, 36]), 8.3)

    def test4(self):
        self.assertEqual(calculate_handicap([85, 80, 76, 79, 82], [72, 72, 72, 71, 71]), 8.8)

    def test5(self):
        self.assertEqual(calculate_handicap([41, 50, 48, 52, 46, 49], [35, 37, 35, 37, 35, 37]), 11.7)


TESTCASES = [
    (([72, 72, 72], [72, 72, 72],), 0),
    (([80, 76, 78, 78], [72, 72, 72, 72],), 6),
    (([42, 45, 46, 44], [36, 36, 36, 36],), 8.3),
    (([85, 80, 76, 79, 82], [72, 72, 72, 71, 71],), 8.8),
    (([41, 50, 48, 52, 46, 49], [35, 37, 35, 37, 35, 37],), 11.7)
]




def calculate_handicap(scores, pars):

    result = []

    for i in range(len(scores)):
        result.append(abs(scores[i] - pars[i]))

    avg = sum(result) / len(result)

    return round(avg, 1)

"""

=> one test case fails the above solution which is
    -> calculate_handicap([42, 45, 46, 44], [36, 36, 36, 36])
        -> Differentials:
            -> 42 - 36 = 6
            -> 45 - 36 = 9
            -> 46 - 36 = 10
            -> 44 - 36 = 8

        -> Average = (6 + 9 + 10 + 8) / 4 = 33/4 = 8.25

    Now, here's the catch:
    => in python, round(8.25, 1) => 8.2
    => but mathematically, many expect 8.25 => 8.3
That is because Python's round() uses banker's rounding (round half to even).
so 8.25 rounds to 8.2(since 2 is even). not 8.3

we can fix that using the traditional rounding(round half up), you can use the Decimal class:
"""

from decimal import Decimal , ROUND_HALF_UP

def calculate_handicap(scores, pars):
    diffs = [s - p for s, p in zip(scores, pars)]
    avg = sum(diffs) / len(diffs)

    return float(Decimal(str(avg)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))



from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": calculate_handicap}, TESTCASES, 1000)
    unittest.main()