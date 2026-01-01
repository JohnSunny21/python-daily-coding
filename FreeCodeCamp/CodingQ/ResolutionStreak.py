"""  

Resolution Streak
Given an array of arrays, where each sub-array represents a day of your resolution activities and contains three integers: the number of steps walked that day, the minutes of screen time that day, and the number of pages read that day; determine if you are keeping your resolutions.

The first sub-array is day 1, and second day 2, and so on.
A day is considered successful if all three of the following goals are met:

You walked at least 10,000 steps.
You had no more than 120 minutes of screen time.
You read at least five pages.
If all of the given days are successful, return "Resolution on track: N day streak." Where N is the number of successful days.

If one or more days is not a success, return "Resolution failed on day X: N day streak.". Where X is the day number of the first unsuccessful day, and N is the number of successful days before the first unsuccessful day.
"""

import unittest

class ResolutionStreakTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]]), "Resolution on track: 3 day streak.")

    def test2(self):
        self.assertEqual(resolution_streak([[10000, 120, 5], [10950, 121, 11]]), "Resolution failed on day 2: 1 day streak.")

    def test3(self):
        self.assertEqual(resolution_streak([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]]),  "Resolution failed on day 3: 2 day streak.")

    def test4(self):
        self.assertEqual(resolution_streak([[11600, 76, 13], [12556, 64, 26], [10404, 32, 59], [9999, 44, 124], [7508, 23, 167], [10900, 80, 0]]),  "Resolution failed on day 4: 3 day streak.")

    def test5(self):
        self.assertEqual(resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9], [10200, 60, 10], [10678, 87, 9], [12431, 67, 13], [10444, 107, 19], [10111, 95, 5], [10000, 120, 7], [11980, 101, 8]]), "Resolution on track: 10 day streak.")


def resolution_streak(days):

    count = 0
    break_day = 0
    for index, (walk, screen_time, pages) in enumerate(days, 1):
        if walk >= 10000 and screen_time <= 120 and pages >= 5:
            count += 1
        else:
            break_day = index
            break

    if count == len(days):
        return f"Resolution on track: {count} day streak."
    else:
        return f"Resolution failed on day {break_day}: {count} day streak."
    
""" 
The below is the minor refinement

=> break_day initialization: You set break_day = 0 initially, that's fine. but it's only used if a failure occurs. You could
simplify by returning immediately inside the loop instead of storing (break_day):

=> This avoids the extra variables and makes the logic tighter.
=> The above solution is correct and efficient . The refinements above are just stylistic - they reduce variables and make the code slightly cleaner,The above version is perfectly valid.
"""

def resolution_streak(days):
    for index, (steps, screen_time, pages_read) in enumerate(days, 1):
        if not(steps >= 10000 and screen_time <= 120 and pages_read >= 5):
            return f"Resolution failed on day {index}: {index-1} day streak."
    
    return f"Resolution on track: {len(days)} day streak."

if __name__ == "__main__":
    unittest.main()