"""
Weekday Finder
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.
"""

import unittest
from datetime import datetime

class WeekdayFinderTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_weekday("2025-11-06"),"Thursday")

    def test2(self):
        self.assertEqual(get_weekday("1999-12-31"),"Friday")

    def test3(self):
        self.assertEqual(get_weekday("1111-11-11"),"Saturday")

    def test4(self):
        self.assertEqual(get_weekday("2112-12-21"),"Wednesday")

    def test5(self):
        self.assertEqual(get_weekday("2345-10-01"),"Monday")


def get_weekday(date_string):

    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    day_name = date_object.strftime("%A")
    return day_name
# If we imported the datetime module like import datetime then we need 
# to use the date_object = datetime.datetime.strptime()

if __name__ == "__main__":
    print(get_weekday("2025-11-05"))
    unittest.main()