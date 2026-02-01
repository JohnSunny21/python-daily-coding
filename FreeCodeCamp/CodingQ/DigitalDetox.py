"""  
Digital Detox
Given an array of your login logs, determine whether you have met your digital detox goal.

Each log is a string in the format "YYYY-MM-DD HH:mm:ss".

You have met your digital detox goal if both of the following statements are true:

You logged in no more than once within any four-hour period.
You logged in no more than 2 times on any single day.

"""

import unittest


class DigitalDetoxTest(unittest.TestCase):

     def test1(self):
          self.assertEqual(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]), True)

     def test2(self):
          self.assertEqual(digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]), False)

     def test3(self):
          self.assertEqual(digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]), True) 

     def test4(self):
          self.assertEqual(digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]), False)

     def test5(self):
          self.assertEqual(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]), True)

     def test6(self):
          self.assertEqual(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]), False)


from datetime import datetime, timedelta
from collections import defaultdict

def digital_detox(logs):
     
     """
     Check if login logs meet digital detox goals:
     1. No more than once within any 4-hour period.
     2. No more than 2 times on any single day.
     """
     # Parse logs into datetime objects

     times = [datetime.strptime(log, "%Y-%m-%d %H:%M:%S") for log in logs]
     times.sort() # Chronologically


     for i in range(1, len(times)):
          if times[i] - times[i-1] < timedelta(hours = 4):
               return False
          
     daily_counts = defaultdict(int)
     for t in times:
          day = t.date()
          daily_counts[day] += 1
          if daily_counts[day] > 2:
               return False
          
     return True



if __name__ == "__main__":
     unittest.main()