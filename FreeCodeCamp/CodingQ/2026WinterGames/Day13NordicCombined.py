"""  
2026 Winter Games Day 13: Nordic Combined
Given an array of jump scores for athletes, calculate their start delay times for the cross-country portion of the Nordic Combined.

The athlete with the highest jump score starts first (0 second delay). All other athletes start later based on how far behind their jump score is compared to the best jump.

To calculate the delay for each athlete, subtract the athlete's jump score from the best overall jump score and multiply the result by 1.5. Round the delay up to the nearest integer.
"""

import unittest


class NordicCombinedTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(calculate_start_delays([120, 110, 125]), [8, 23, 0])

      def test2(self):
          self.assertEqual(calculate_start_delays([118, 125, 122, 120]), [11, 0, 5, 8])

      def test3(self):
        self.assertEqual(calculate_start_delays([100, 105, 95, 110, 120, 115, 108]), [30, 23, 38, 15, 0, 8, 18])      

      def test4(self):
          self.assertEqual(calculate_start_delays([130, 125, 128, 120, 118, 122, 127, 115, 132, 124]), [3, 11, 6, 18, 21, 15, 8, 26, 0, 12])




import math
def calculate_start_delays(jump_scores):
    result = []
    max_score = max(jump_scores)
    for score in jump_scores:
        result.append(math.ceil((max_score - score) * 1.5))

    return result

# using naming conventions
def calculate_start_delays(jump_scores):
    best_score = max(jump_scores)
    delays = []
    for score in jump_scores:
        delay = (best_score - score ) * 1.5
        delays.append(math.ceil(delay))
    return delays




if __name__ == "__main__":
    unittest.main()