"""  


Groundhog Day
Today is Groundhog Day, in which a groundhog predicts the weather based on whether or not it sees its shadow.

Given a value representing the groundhog's appearance, return the correct prediction:

If the given value is the boolean true (the groundhog saw its shadow), return "Looks like we'll have six more weeks of winter.".
If the value is the boolean false (the groundhog did not see its shadow), return "It's going to be an early spring.".
If the value is anything else (the groundhog did not show up), return "No prediction this year.".

"""

import unittest


class GroundingDayTest(unittest.TestCase):
      
    def test1(self):
          self.assertEqual(groundhog_day_prediction(" "), "No prediction this year.")

    def test2(self):
          self.assertEqual(groundhog_day_prediction("True"), "No prediction this year.")

    def test3(self):
         self.assertEqual(groundhog_day_prediction(None), "No prediction this year.")
    
    def test4(self):
         self.assertEqual(groundhog_day_prediction(" "), "No prediction this year.")

    def test5(self):
        self.assertEqual(groundhog_day_prediction("True"), "No prediction this year.")


def groundhog_day_prediction(appearance):
     
     if appearance == True:
          return "Looks like we'll have six more weeks of winter."
     elif appearance == False:
          return "It's going to be an early spring."
     else:
          return "No prediction this year."
     

def groundhog_day_prediction(appearance):
     
     if appearance is True:
          return "Looks like we'll have six more weeks of winter."
     elif appearance is False:
          return "It's going to be an early spring."
     else:
          return "No prediction this year."
     
""" 
Minor Improvements
1. Use is True / is False instead of == True / == False
    -> In Python, == checks equality, while is checks identity.
    -> For boolean,s is is more explicit and avoids edge cases( like 1 == True being True).

The first solution is correct. The only tweak I'd suggest is using is True / is False for clarity and Python best practice. 
That way, you avoid accidental matches with non boolen values like 1 or 0.
"""
     


if __name__ == "__main__":
     unittest.main()