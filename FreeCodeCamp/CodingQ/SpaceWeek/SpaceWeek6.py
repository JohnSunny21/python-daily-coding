"""
Space Week Day 6: Moon Phase
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

"New": days 1 - 7
"Waxing": days 8 - 14
"Full": days 15 - 21
"Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.

Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
You will not be given any dates before the reference date.
Return the correct phase as a string.
"""

import unittest
from datetime import datetime

class SpaceWeek6Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(moon_phase("2000-01-12"),"New")

    def test2(self):
        self.assertEqual(moon_phase("2000-01-13"),"Waxing")

    def test3(self):
        self.assertEqual(moon_phase("2014-10-15"),"Full")

    def test4(self):
        self.assertEqual(moon_phase("2012-10-21"),"Waning")

    def test5(self):
        self.assertEqual(moon_phase("2022-12-14"),"New")





def moon_phase(date_string):
    
   reference_date = datetime(2000,1,6)
   given_date = datetime.strptime(date_string,"%Y-%m-%d")
   days_passed = (given_date - reference_date).days
   cycle_day = (days_passed % 28) + 1 # Day 1 to 28


   if 1<= cycle_day <= 7:
       return "New"
   elif 8 <= cycle_day <= 14:
       return "Waxing"
   elif 15 <= cycle_day <= 21:
       return "Full"
   else:
       return "Waning"




if __name__ == "__main__":
    print(moon_phase("2000-01-06"))
    print(moon_phase("2000-01-13"))
    unittest.main()