""" 


Sleep Debt
Given an array of hours slept each night leading up to today, and a target number of hours per night, return how many hours of sleep you need tonight to eliminate your sleep debt.

Include tonight's hours in the total time needed to catch up.
If you've slept enough to cover tonight's target or more, return 0.
"""


import unittest


class SleepDebtTest(unittest.TestCase):




    def test1(self):
        self.assertEqual(sleep_debt([6, 6, 6, 6, 6, 6], 8), 20)

    def test2(self):
        self.assertEqual(sleep_debt([6, 7, 8, 4, 8, 6], 7), 10)

    def test3(self):
        self.assertEqual(sleep_debt([10, 10, 9, 10, 9, 11], 9), 4)

    def test4(self):
        self.assertEqual(sleep_debt([8, 7, 6, 7, 6, 8], 6), 0)

    def test5(self):
        self.assertEqual(sleep_debt([8, 9, 10, 9, 10, 7], 7), 0)


TESTCASES = [
    (([6, 6, 6, 6, 6, 6], 8,), 20),
    (([6, 7, 8, 4, 8, 6], 7,), 10),
    (([10, 10, 9, 10, 9, 11], 9,), 4),
    (([8, 7, 6, 7, 6, 8], 6,), 0),
    (([8, 9, 10, 9, 10, 7], 7,), 0)
]





def sleep_debt(hours_slept, target_hours):

    result = []

    for hour in hours_slept:
        diff = target_hours - hour
        result.append(diff)



    total_debt_hours = sum(result) + target_hours

    return total_debt_hours if total_debt_hours > 0 else 0


def sleep_debt_two(hours_slept, target_hours):

    target_debt_hours = sum([target_hours - hour for hour in hours_slept]) + target_hours


    return target_debt_hours if target_debt_hours > 0 else 0

def sleep_debt_three(hours, target):

    nights = len(hours)
    total_target = (nights + 1) * target
    total_actual = sum(hours)
    needed = total_target - total_actual

    return max(0, needed)


from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": sleep_debt,
         "second": sleep_debt_two,
         "three": sleep_debt_three},
        TESTCASES,
        10000
    )

    unittest.main()