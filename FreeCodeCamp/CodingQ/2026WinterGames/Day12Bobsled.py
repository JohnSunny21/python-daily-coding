"""  
2026 Winter Games Day 12: Bobsled
Given an array representing the weights of the athletes on a bobsled team and a number representing the weight of the bobsled, determine whether the team is eligible to race.

The length of the array determines the team size: 1, 2 or 4 person teams.
All given weight values are in kilograms (kg).
The bobsled (sled by iteself) must have a minimum weight of:

162 kg for a 1-person team
170 kg for a 2-person team
210 kg for a 4-person team
The total weight of the bobsled (athletes plus sled) must not exceed:

247 kg for a 1-person team
390 kg for a 2-person team
630 kg for a 4-person team
Return "Eligible" if the team meets all the requirements, or "Not Eligible" if the team fails to meet one or more of the requirements.
"""

import unittest


class BobsledTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(check_eligibility([80], 160), "Not Eligible")

      def test2(self):
          self.assertEqual(check_eligibility([80], 170), "Not Eligible")

      def test3(self):
          self.assertEqual(check_eligibility([85, 90], 170), "Eligible")

      def test4(self):
          self.assertEqual(check_eligibility([85, 95], 168), "Not Eligible")

      def test5(self):
          self.assertEqual(check_eligibility([112, 97], 185), "Not Eligible")

      def test6(self):
          self.assertEqual(check_eligibility([110, 102, 90, 106], 222), "Eligible")

      def test7(self):
          self.assertEqual(check_eligibility([106, 99, 90, 88], 205), "Not Eligible")

      def test8(self):
          self.assertEqual(check_eligibility([106, 99, 103, 96], 227), "Not Eligible")

      def test9(self):
          self.assertEqual(check_eligibility([78], 165), "Eligible")




def check_eligibility(athlete_weights, sled_weight):

    team_size = len(athlete_weights)
    total_weight = sum(athlete_weights) + sled_weight

    if team_size == 1:
        if sled_weight < 162 or total_weight > 247:
            return "Not Eligible"
        return "Eligible"
    
    elif team_size == 2:
        if sled_weight < 170 or total_weight > 390:
            return "Not Eligible"
        return "Eligible"
    
    elif team_size == 4:
        if sled_weight < 210 or total_weight > 630:
            return "Not Eligible"
        return "Eligible"
    

    else:
        # Invalid team size
        return "Not Eligible"
    
def check_eligibility(athletes, sled_weight):
    
    team_size = len(athletes)
    total_weight = sum(athletes) + sled_weight

    min_weights = {1: 162, 2: 170, 4: 210}
    max_weights = {1: 247, 2: 390, 4: 630}

    if team_size not in min_weights:
        return "Not Eligible"
    
    if sled_weight < min_weights[team_size]:
        return "Not Eligible"
    
    if total_weight > max_weights[team_size]:
        return "Not Eligible"
    
    return "Eligible"


if __name__ == "__main__":
    unittest.main()

