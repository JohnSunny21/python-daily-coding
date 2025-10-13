"""
24 to 12
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
"""

import unittest

class Time24to12Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(to_12("1124"),"11:24 AM")

    def test2(self):
        self.assertEqual(to_12("0900"),"9:00 AM")

    def test3(self):
        self.assertEqual(to_12("1455"),"2:55 PM")

    def test4(self):
        self.assertEqual(to_12("2346"),"11:46 PM")
    
    def test5(self):
        self.assertEqual(to_12("0030"),"12:30 AM")








def to_12(time):

    hour = int(time[:2])
    minutes = int(time[2:])

    if hour == 0:
        hour_12 = 12
        period = "AM"
    elif hour < 12:
        hour_12 = hour
        period = "AM"
    elif hour == 12:
        hour_12 = 12
        period = "PM"
    else:
        hour_12 = hour - 12
        period = "PM"

    return f"{hour_12}:{minutes:02d} {period}"

    

def convert_to_12_hour(time):

    hour = int(time[:2])
    minute = time[2:]


    period = "AM"

    if hour == 0:
        hour_12 = 12
    elif hour == 12:
        hour_12 = 12
        period = "PM"
    elif hour > 12:
        hour_12 = hour -12
        period = "PM"
    else:
        hour_12 = hour
    



    return f"{hour_12}:{minute} {period}"
if __name__ == "__main__":

    print(to_12("1124"))
    unittest.main()