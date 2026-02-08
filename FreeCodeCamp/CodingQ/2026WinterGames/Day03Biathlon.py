"""  
2026 Winter Games Day 3: Biathlon
Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.

Each round consists of 5 targets.
Each missed target results in a 150 meter penalty loop.
"""

import unittest

class BiathlonTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(calculate_penalty_distance([5, 5]), 0)

      def test2(self):
          self.assertEqual(calculate_penalty_distance([4, 5, 3, 5]), 450)

      def test3(self):
          self.assertEqual(calculate_penalty_distance([5, 4, 5, 5]), 150)

      def test4(self):
          self.assertEqual(calculate_penalty_distance([4, 3, 0, 3]), 1500)


def calculate_penalty_distance(rounds):

    penalty_ski = 0
    for hits in rounds:
        if hits < 5:
            penalty_ski += (5 - hits) * 150

    return penalty_ski

"""
-> the if condition hits < 5 is fine. It avoids adding penalty when all targets are hit.
-> If you want to be stricter, you could remove the if and just always compute (5- hits) * 150, since when hits == 5 it naturally gives 0.
"""

def calculate_penalty_distance(rounds):

    total_penalty = 0

    for hits in rounds:

        misses = 5  - hits

        total_penalty += misses * 150

    return total_penalty


def calculate_penalty_distance_oneliner(rounds):

    return sum((5 - hits) * 150 for hits in rounds)


def calculate_penalty_distance_dict_approach(rounds):

    penalty_map = {hits: (5 - hits) * 150 for hits in range(6)}

    return sum(penalty_map[hits] for hits in rounds)

if __name__ == "__main__":
    unittest.main()
