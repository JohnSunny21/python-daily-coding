"""  


2026 Winter Games Day 10: Alpine Skiing
Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.

To determine the rating:

Calculate the steepness of the hill by taking the drop divided by the distance.
Then, calculate the adjusted steepness based on the hill type:
"Downhill" multiply steepness by 1.2
"Slalom": multiply steepness by 0.9
"Giant Slalom": multiply steepness by 1.0
Return:

"Green" if the adjusted steepness is less than or equal to 0.1
"Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
"Black" if the adjusted steepness is greater than 0.25
"""

import unittest


class AlpineSkiingTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(get_hill_rating(620, 2800, "Downhill"), "Black")

      def test2(self):
          self.assertEqual(get_hill_rating(420, 1680, "Giant Slalom"), "Blue")

      def test3(self):
          self.assertEqual(get_hill_rating(250, 3000, "Downhill"), "Green")

      def test4(self):
          self.assertEqual(get_hill_rating(110, 900, "Slalom"), "Blue")

      def test5(self):
          self.assertEqual(get_hill_rating(380, 1500, "Giant Slalom"), "Black")

      def test6(self):
          self.assertEqual(get_hill_rating(95, 900, "Slalom"), "Green")


def get_hill_rating(drop, distance, type):

    steepness = drop / distance

    if type == "Downhill":
        adjusted = steepness * 1.2
    elif type == "Slalom":
        adjusted = steepness * 0.9
    elif type == "Giant Slalom":
        adjusted = steepness * 1.0
    else:
        raise ValueError("Invalid hill type")
    

    if adjusted <= 0.1:
        return "Green"
    elif adjusted <= 0.25:
        return "Blue"
    else:
        return "Black"
    

if __name__ == "__main__":
    unittest.main()
