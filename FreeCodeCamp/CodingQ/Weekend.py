"""
Is It the Weekend?
Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

The weekend starts on Saturday.
If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Make sure the calculation ignores your local timezone.
"""

from datetime import datetime
import unittest

class WeekendTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(days_until_weekend("2025-11-14"),"1 day until the weekend.")

    def test2(self):
        self.assertEqual(days_until_weekend("2025-01-01"),"3 days until the weekend.")

    def test3(self):
        self.assertEqual(days_until_weekend("2025-12-06"),"It's the weekend!")
    
    def test4(self):
        self.assertEqual(days_until_weekend("2026-01-27"),"4 days until the weekend.")

    def test5(self):
        self.assertEqual(days_until_weekend("2026-09-07"),"5 days until the weekend.")
    
    def test6(self):
        self.assertEqual(days_until_weekend("2026-11-29"),"It's the weekend!")



def days_until_weekend(date_string):
    
    date_object = datetime.strptime(date_string,"%Y-%m-%d")
    week_day = date_object.isoweekday() # Monday = 1 , Sunday = 7
    day_name = date_object.strftime("%A")

    no_of_days = 6 - week_day # Here we take the 6 because the saturday is considered as weekend
    # if we take the 7 which is sunday then the saturday will be skipped and the weeked is calculated for sunday only.

    if day_name in ['Saturday', 'Sunday']:
        return "It's the weekend!"
    if no_of_days > 1:
        return f"{no_of_days} days until the weekend."
    else:
        return f"{no_of_days} day until the weekend."


    
# The above method can be refined again to reduce some statement and remove redundant code

def days_until_weekend_refined(date_string):
    """
    1. Redundant day_name usage
    day_name in ["Saturday", "Sundar"]

    But it already have week_day , so we can simply:
    use the
    if week_day >= 6:
        return "It's the weekend!"

    This avoids the exxxtra strftime() call and keeps it cleaner.

    2. Edge case: Sunday

    isoweekday() return 7 for sunday, so:
    no_of_days = 6 - weekday # Becomes -1 on sunday
    But we have the short-circuit with the weekend check,
    but if we remove or reordered, we get a negative value and unexpected results.
    """

    date_object = datetime.strptime(date_string,"%Y-%m-%d")
    weekday = date_object.weekday()

    if weekday > 6:
        return "It's the weekend!"
    
    days_left = 6 - weekday
    unit = "day" if days_left == 1 else "days"
    return f"{days_left} {unit} until the weekend."

    



# This is another version
def days_until_weekend_optimized(date_string):
    date = datetime.strptime(date_string,"%Y-%m-%d")
    weekday = date.weekday() # Monday = 0, Sunday = 6


    """
    This Works as :

    => Uses datetime.strptime() to parse the input date.
    => weekday() returns an integer from 0 (Monday ) to 6 (Sunday)
    => Calculates how many days until Saturday (weekday == 5).
    => Handles singular / Plural grammer for "day/"days".

    """
    if weekday == 5 or weekday == 6:
        return "It's the weekend!"
    days_left = 5 - weekday # Saturday weekday is 5

    unit = "day" if days_left == 1 else "days"
    return f"{days_left} {unit} until the weekend."


    

    




if __name__ == "__main__":
    print(days_until_weekend("2025-11-14"))
    unittest.main()