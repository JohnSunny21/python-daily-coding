"""  
Leap Year Calculator
Given an integer year, determine whether it is a leap year.

A year is a leap year if it satisfies the following rules:

The year is evenly divisible by 4, and
The year is not evenly divisible by 100, unless
The year is evenly divisible by 400.
"""

import unittest

class LeapYearCalculatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_leap_year(2024), True)

    def test2(self):
        self.assertEqual(is_leap_year(2023), False)

    def test3(self):
        self.assertEqual(is_leap_year(2100), False)

    def test4(self):
        self.assertEqual(is_leap_year(2000), True)

    def test5(self):
        self.assertEqual(is_leap_year(1999), False)

    def test6(self):
        self.assertEqual(is_leap_year(2040), True)

    def test7(self):
        self.assertEqual(is_leap_year(2026), False)



def is_leap_year(year):

    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

"""
1. Divisible by 4 -> candidate for leap year.
2. Divisible by 100 -> normally not a leap year (exception case).
3. Divisible by 400 -> is a leap year (special override).

So: 
-> 2000 -> leap year (divisible by 400).
-> 1900 -> not a leap year (divisible by 100 but not 400).
-> 2024 -> leap year (divisble by 4, not by 100).
-> 2023 -> not a leap year (not divisible by 4).

==> Year = 2024
 -> 2024 % 4 == 0 -> True
 -> 2024 % 100 != 0 -> True
 -> Whole condition -> True -> Leap Year.

==> Year - 1900
 -> 1900 % 4 == 0 -> True
 -> 1900 % 100 != 0 -> False
 -> 1900 % 400 == 0 -> False
 -> Inner condition -> False -> Not leap year.

==> Year = 2000 
 -> 2000 % 4 == 0 -> True
 -> 2000 % 100 != 0 -> False
 -> 2000 % 400 == 0 -> True
 -> Inner condition -> True -> Leap Year.


-> Divisible by 4 -> candidate
-> Centuries (divisible by 100) are excluded.
-> Exceptioon: centuries divisible by 400 are included.
"""

if __name__ == "__main__":
    print(is_leap_year(2026))
    unittest.main()