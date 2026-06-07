"""

Last Load
Given the number of scoops of laundry detergent you have remaining and an array of how many scoops you used in each of the previous days, return the number of full days of detergent you have remaining.

Calculate your average daily usage from the usage history and assume that amount of usage each day going forward.
"""

import unittest


class LastLoadTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(last_load_date(10, [2, 2, 2, 2, 2, 2, 2]), 5)

    def test2(self):
        self.assertEqual(last_load_date(16, [2, 3, 0, 3, 4, 2, 1]), 7)

    def test3(self):
        self.assertEqual(last_load_date(33, [5, 0, 4, 3, 3, 2]), 11)

    def test4(self):
        self.assertEqual(last_load_date(50, [2, 0, 2, 9, 12, 0, 2]), 12)

    def test5(self):
        self.assertEqual(last_load_date(20, [13,9, 12, 10, 8]), 1)


TESTCASES = [
    ((10, [2, 2, 2, 2, 2, 2, 2],), 5),
    ((16, [2, 3, 0, 3, 4, 2, 1],), 7),
    ((33, [5, 0, 4, 3, 3, 2],), 11),
    ((50, [2, 0, 2, 9, 12, 0, 2],), 12),
    ((20, [13, 9, 12, 10, 8],), 1)
]




def last_load_date(scoops, usage):

    average_scoop = sum(usage) / len(usage)

    return scoops // average_scoop

"""
=> // in python is floor division, but it works differently depending on the types:
    -> if both operands are integers, -> integer floor division.
    -> if one operand is a float -> float floor division, result is still a float.

    Example:
        7 // 2.5 # 2.0 (float)
        int(7 // 2.5) # 2 (int)
    
=> So your function may return a float like 2.0 instead of an integer. If you want a strict integer result
    , wrap it in int().
"""


def last_load(remaining, history):

    if not history:
        return 0
    
    avg_usage = sum(history) / len(history)

    return int(remaining // avg_usage)








from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": last_load_date,
         "second": last_load},
        TESTCASES, 
        10000
    )

    unittest.main()