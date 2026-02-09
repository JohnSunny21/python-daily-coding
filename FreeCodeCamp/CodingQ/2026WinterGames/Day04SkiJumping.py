"""  

2026 Winter Games Day 4: Ski Jumping
Given distance points, style points, a wind compensation value, and K-point bonus value, calculate your score for the ski jump and determine if you won a medal or not.

Your score is calculated by summing the above four values.
The current total scores of the other jumpers are:

165.5
172.0
158.0
180.0
169.5
175.0
162.0
170.0
If your score is the best, return "Gold"
If it's second best, return "Silver"
If it's third best, return "Bronze"
Otherwise, return "No Medal"
"""

import unittest

class SkiJumpingTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(ski_jump_medal(125.0, 58.0, 0.0, 6.0), "Gold")

      def test2(self):
          self.assertEqual(ski_jump_medal(119.0, 50.0, 1.0, 4.0), "Bronze")

      def test3(self):
          self.assertEqual(ski_jump_medal(122.0, 52.0, -1.0, 4.0), "Silver")

      def test4(self):
          self.assertEqual(ski_jump_medal(118.0, 50.5, -1.5, 4.0), "No Medal")

      def test5(self):
          self.assertEqual(ski_jump_medal(124.0, 50.5, 2.0, 5.0), "Gold")

      def test6(self):
          self.assertEqual(ski_jump_medal(119.0, 49.5, 0.0, 3.0), "No Medal")


def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):

    total_score = distance_points + style_points + wind_comp + k_point_bonus

    current_scores = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]

    current_scores.append(total_score)

    current_scores = sorted(current_scores, reverse=True)

    if current_scores[0] == total_score:
        return "Gold"
    elif current_scores[1] == total_score:
        return "Silver"
    elif current_scores[2] == total_score:
        return "Bronze"
    else:
        return "No Medal"

"""
This works fine when your score is unique. but if there's already a jumper with the same score( say 180.0) , then both
scores are equal.

Python's sorted() doesn't distinguish between "Yuur 180" and "their 180"- it just places them in order. So you can't tell which 180 belongs to you.
That means:
=> If you tie for first, you'll still get "Gold" because your score equals the top value.
-> But you can't distinguish whether you're the only gold or sharing it.
=> Same for ties with silver or bronze.
"""

"""

If we want to have a solution for the tie breaks as well we need to consider this alternate solution
=> Adding identifiers:
        Store scores as tuples like ("Me", total_score) and ("other", 180.0). Then when you sort, you can check exactly where "Me" lands.
        -> This lets you distinguish ties, but it complicates the code.
"""

def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    total_score = distance_points + style_points + wind_comp + k_point_bonus

    current_scores = [
        ("Other", 165.5), ("Other", 172.0), ("Other", 158.0),
        ("Other", 180.0), ("Other", 169.5), ("Other", 175.0),
        ("Other", 162.0), ("Other", 170.0),
        ("Me", total_score)
    ]

    current_scores.sort(key= lambda x : x[1], reverse=True)

    for i, (who, score) in enumerate(current_scores, start=1):
        if who == "Me":
            position = i
            break
    
    if position == 1:
        return "Gold"
    elif position == 2:
        return "Silver"
    elif position == 3:
        return "Bronze"
    else:
        return "No Medal"
    

if __name__ == "__main__":
    unittest.main()
