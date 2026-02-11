"""  

2026 Winter Games Day 6: Figure Skating
Given an array of judge scores and optional penalties, calculate the final score for a figure skating routine.

The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove the highest and lowest judge scores and sum the remaining 8 scores to get the base score.

Any additional arguments passed to the function are penalties. Subtract all penalties from the base score to get the final score.
"""


import unittest


class FigureSkatingTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1), 64)

      def test2(self):
          self.assertEqual(compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 80)

      def test3(self):
          self.assertEqual(compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1), 67)

      def test4(self):
          self.assertEqual(compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0), 67.5)

      def test5(self):
          self.assertEqual(compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5), 59)


def compute_score(judge_scores, *penalties):

    judge_scores.sort(reverse=True)
    # we can use the sorted(judge_scores) here and this judge_score.sort will return None.
    judge_scores.pop(0)
    judge_scores.pop()

    total_score = sum(judge_scores)
    if not penalties:
        return total_score
    else:
        for penalty in penalties:
            total_score -= penalty

        return total_score
    

"""
We can improve this code by making some few changes

=> You can simplify penalty subtraction with sum(penalties)
"""

def compute_score(judge_scores, *penlties):
    scores = sorted(judge_scores)
    base_score = sum(scores[1: -1])

    total_score = base_score - sum(penlties)

    return total_score


if __name__ == "__main__":
    unittest.main()