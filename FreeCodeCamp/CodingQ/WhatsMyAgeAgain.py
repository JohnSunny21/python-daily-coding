"""

What's My Age Again?
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025
"""

import unittest

class WhatsMyAgeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(calculate_age("2000-11-20"),25)

    def test2(self):
        self.assertEqual(calculate_age("2000-12-01"),24)

    def test3(self):
        self.assertEqual(calculate_age("2014-10-25"),11)

    def test4(self):
        self.assertEqual(calculate_age("1994-01-06"),31)

    def test5(self):
        self.assertEqual(calculate_age("1994-12-14"),30)





from datetime import datetime

def calculate_age(birthday):

    date_object = datetime.strptime(birthday, "%Y-%m-%d")
    # current_date_object = datetime.strptime("2025-11-27","%Y-%m-%d")

    # or we can write it as 
    reference_date = datetime(2025,11,27)

    age = reference_date.year - date_object.year


    if (reference_date.month, reference_date.day) < (date_object.month, date_object.day):
        age -= 1
    

    return age


if __name__ == "__main__":
    print(calculate_age("2000-11-20"))
    print(calculate_age("2000-12-01"))
    print(calculate_age("1994-12-14"))
    unittest.main()
