""" 

Anniversary Milestones
Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:

Years Married	Milestone
1	"Paper"
5	"Wood"
10	"Tin"
25	"Silver"
40	"Ruby"
50	"Gold"
60	"Diamond"
70	"Platinum"
If they haven't reached the first milestone, return "Newlyweds".
"""


import unittest

class AnniversaryMilestonesTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(get_milestone(0), "Newlyweds")

      def test2(self):
          self.assertEqual(get_milestone(1), "Paper")    

      def test3(self):
          self.assertEqual(get_milestone(8), "Wood")     

      def test4(self):
          self.assertEqual(get_milestone(10), "Tin")     

      def test5(self):
          self.assertEqual(get_milestone(26), "Silver")  

      def test6(self):
          self.assertEqual(get_milestone(45), "Ruby")    

      def test7(self):
          self.assertEqual(get_milestone(50), "Gold")    

      def test8(self):
          self.assertEqual(get_milestone(64), "Diamond") 

      def test9(self):
          self.assertEqual(get_milestone(71), "Platinum")



def get_milestone(years):

    married_milestone = {
        1: "Paper",
        5: "Wood",
        10: "Tin",
        25: "Silver",
        40: "Ruby",
        50: "Gold",
        60: "Diamond",
        70: "Platinum"
    }

    for year, milestone in reversed(married_milestone.items()):
        if years>= year:
            return milestone
        
    return "Newlyweds"


def get_milestone(years):
    
    milestones = {
        1: "Paper",
        5: "Wood",
        10: "Tin",
        25: "Silver",
        40: "Ruby",
        50: "Gold",
        60: "Diamond",
        70: "Platinum"
    }

    if years < 1:
        return "Newlyweds"
    
    recent = max([y for y in milestones if y <= years], default=None)

    return milestones[recent] if recent else "Newlyweds"


if __name__ == "__main__":
    unittest.main()