"""  
2026 Winter Games Day 7: Speed Skating
Given two arrays representing the lap times (in seconds) for two speed skaters, return the lap number where the difference in lap times is the largest.

The first element of each array corresponds to lap 1, the second to lap 2, and so on.
"""


import unittest


class SpeedSkatingTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(largest_difference([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23]), 1)

    def test2(self):
        self.assertEqual(largest_difference([25.82, 25.90, 26.05, 26.00, 26.48], [25.85, 25.92, 26.07, 25.98, 25.95]), 5)

    def test3(self):
        self.assertEqual(largest_difference([25.88, 26.10, 25.95, 26.05, 26.00], [25.90, 26.55, 25.92, 26.03, 26.01]), 2)

    def test4(self):
        self.assertEqual(largest_difference([25.92, 26.01, 26.05, 25.88, 26.12], [25.95, 26.00, 26.03, 26.45, 26.10]), 4)

    def test5(self):
        self.assertEqual(largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30]), 3)

import math
def largest_difference(skater1, skater2):

    max_diff = 0
    final_index = 0
    for index, (lap1, lap2) in enumerate(zip(skater1, skater2), start=1):
        diff = abs(lap1 - lap2)
        if max_diff < diff:
            max_diff = diff
            final_index = index
    return final_index

""" 
=> Always use abs() when comparing differences, since we  care about the magnitude, not the direction
"""

def largeset_difference(skater1, skater2):

    max_diff = -1
    lap_number = -1

    for i in range(len(skater1)):
        diff = abs(skater1[i] - skater2[i])
        if diff > max_diff:
            max_diff = diff
            lap_number = i + 1

    return lap_number




if __name__ == "__main__":
    print(largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30]))
    unittest.main()
