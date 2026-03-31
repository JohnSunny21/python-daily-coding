""" 

Wake-Up Alarm
Given a string representing the time you set your alarm and a string representing the time you actually woke up, determine if you woke up early, on time, or late.

Both times will be given in "HH:MM" 24-hour format.
Return:

"early" if you woke up before your alarm time.
"on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
"late" if you woke up more than 10 minutes after your alarm time.
Both times are on the same day.
"""

import unittest


class WakeUpAlarmTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(alarm_check("07:00", "06:45"), "early")  

    def test2(self):
        self.assertEqual(alarm_check("06:30", "06:30"), "on time")

    def test3(self):
        self.assertEqual(alarm_check("08:10", "08:15"), "on time")

    def test4(self):
        self.assertEqual(alarm_check("09:30", "09:45"), "late")   

    def test5(self):
        self.assertEqual(alarm_check("08:15", "08:25"), "on time")

    def test6(self):
        self.assertEqual(alarm_check("05:45", "05:56"), "late")   

    def test7(self):
        self.assertEqual(alarm_check("04:30", "04:00"), "early") 




def alarm_check(alarm_time, wake_time):
    alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
    wake_hour, wake_minute = map(int, wake_time.split(":"))


    alarm_time = alarm_hour * 60 + alarm_minute
    wake_time = wake_hour * 60 + wake_minute


    if wake_time < alarm_time:
        return "early"
    
    elif wake_time == alarm_time or (wake_time - alarm_time) <= 10:
        return "on time"
    else:
        return "late"
    

from datetime import datetime, timedelta

def wake_up_status(alarm: str, wake: str) -> str:

    # Step 1: Parse both times into datetime objects
    # Format is "HH:MM" so we use strptime

    alarm_time = datetime.strptime(alarm, "%H:%M")
    wake_time = datetime.strptime(wake, "%H:%M")

    # Step 2: Compare times
    if wake_time < alarm_time:
        # Wake up before alarm
        return "early"
    
    # Step 3: Dafine snooze window (10 minutes after alarm)
    snooze_limit = alarm_time + timedelta(minutes=10)

    if wake_time <= snooze_limit:
        # Wake up at alarm or within 10 minutes
        return "on time"
    
    else:
        # More than 10 minutes late
        return "late"
    
    

from utils.benchmark import benchmark

if __name__ == "__main__":

    TESTCASES = [
    (("07:00", "06:45",), "early"),
    (("06:30", "06:30",), "on time"),
    (("08:10", "08:15",), "on time"),
    (("09:30", "09:45",), "late"),
    (("08:15", "08:25",), "on time"),
    (("05:45", "05:56",), "late"),
    (("04:30", "04:00",), "early")
]
    
    scores = benchmark({
        "basic": alarm_check,
        "using_datetime": wake_up_status
    },
    TESTCASES,
    10000)
    unittest.main()