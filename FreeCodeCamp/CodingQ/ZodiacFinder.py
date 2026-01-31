"""  

Zodiac Finder
Given a date string in the format "YYYY-MM-DD", return the zodiac sign for that date using the following chart:

Date Range	Zodiac Sign
March 21 - April 19	"Aries"
April 20 - May 20	"Taurus"
May 21 - June 20	"Gemini"
June 21 - July 22	"Cancer"
July 23 - August 22	"Leo"
August 23 - September 22	"Virgo"
September 23 - October 22	"Libra"
October 23 - November 21	"Scorpio"
November 22 - December 21	"Sagittarius"
December 22 - January 19	"Capricorn"
January 20 - February 18	"Aquarius"
February 19 - March 20	"Pisces"
Zodiac signs are based only on the month and day, you can ignore the year.
"""



import unittest

class ZodiacFinderTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(get_sign("2026-01-31"), "Aquarius")

      def test2(self):
          self.assertEqual(get_sign("2001-06-10"), "Gemini")

      def test3(self):
          self.assertEqual(get_sign("1985-09-07"), "Virgo")

      def test4(self):
          self.assertEqual(get_sign("2023-03-19"), "Pisces")

      def test5(self):
          self.assertEqual(get_sign("2045-11-05"), "Scorpio")

      def test6(self):
          self.assertEqual(get_sign("1985-12-06"), "Sagittarius")      

      def test7(self):
          self.assertEqual(get_sign("2025-12-30"), "Capricorn")        

      def test8(self):
          self.assertEqual(get_sign("2018-10-08"), "Libra")

      def test9(self):
          self.assertEqual(get_sign("1958-05-04"), "Taurus")

from datetime import datetime

def get_sign(date_str):

    date = datetime.strptime(date_str, "%Y-%m-%d")
    month, day = date.month, date.day


    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    else:
        return "Invalid date"
    




# This version is more data-driven
ZODIAC_RANGES = [
    (3, 21, 4, 19, "Aries"),
    (4, 20, 5, 20, "Taurus"),
    (5, 21, 6, 20, "Gemini"),
    (6, 21, 7, 22, "Cancer"),
    (7, 23, 8, 22, "Leo"),
    (8, 23, 9, 22, "Virgo"),
    (9, 23, 10, 22, "Libra"),
    (10, 23, 11, 21, "Scorpio"),
    (11, 22, 12, 21, "Sagittarius"),
    (12, 22, 1, 19, "Capricorn"),
    (1, 20, 2, 18, "Aquarius"),
    (2, 19, 3, 20, "Pisces"),
]

def get_sign(date_str):

    date = datetime.strptime(date_str,"%Y-%m-%d")
    month, day = date.month, date.day

    for start_m, start_d, end_m, end_d, sign in ZODIAC_RANGES:
        if start_m < end_m:

            if(month == start_m and day >= start_d) or \
            (month == end_m and day <= end_d):
            # (start_m < month < end_m):
                return sign
            
        else:
            if(month == start_m and day >= start_d) or \
            (month == end_m and day <= end_d):
            # (month > start_m or month < end_m):
                return sign
    return "Invalid date"

"""
=> Maintainable: All ranges are in one data structure , easy to update.
=> Readable: No long chain of it/ elif
=> Extensible: You can add or modify ranges without touching logic.
=> Handles wrap-around cases(Capricon, Aquarius, Pisces) cleanly.
"""


"""

There is a condition like month > startM and month < endM 
=> It's used for longer zodiac ranges that span multiple months.
=> Example: Gemini runs from May 21 (5 / 21) to June 20 (6 / 20).
    -> If the date is June 10, then:
        -> month == 6 and day <= 20 -> condition satisfies.
    -> if the date is May 25. then:
        -> month == 5 and day >= 21 -> condition satisfies.
    -> if the date is between May and Jue (say month 5.5 doesn't exist, but if it were july in a longer range), then month> startM and month < endM would catch it.

    
so for this problem no need for that .

=> Zodiac ranges are always two months long.
=> The "middle month" condition is unnecessary/
=> The only special case is wrap- around ranges(Capricorn, Aquarius, Pisces), where the ranges crosses December -> January -> February -> March
"""
    


if __name__ == "__main__":
    unittest.main()