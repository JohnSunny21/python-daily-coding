""" 



Closest Time Direction
Given two times, determine whether you can get from the first to the second faster by moving forward or backward.

Times are given in 24-hour format ("HH:MM")
The clock wraps around (23:59 goes to 00:00 when moving forward, and 00:00 goes to 23:59 when moving backwards)
Return:

"forward" if moving forward is shorter
"backward" if moving backward is shorter
"equal" if both directions take the same amount of time
"""

import unittest


class ClosestTimeDirection(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_direction("10:00", "12:00"), "forward")

    def test2(self):
        self.assertEqual(get_direction("11:00", "05:00"), "backward")

    def test3(self):
        self.assertEqual(get_direction("00:00", "12:00"), "equal")

    def test4(self):
        self.assertEqual(get_direction("15:45", "01:10"), "forward")

    def test5(self):
        self.assertEqual(get_direction("03:30", "19:50"), "backward")

    def test6(self):
        self.assertEqual(get_direction("06:30", "18:30"), "equal")


TESTCASES = [
    (("10:00", "12:00",), "forward"),
    (("11:00", "05:00",), "backward"),
    (("00:00", "12:00",), "equal"),
    (("15:45", "01:10",), "forward"),
    (("03:30", "19:50",), "backward"),
    (("06:30", "18:30",), "equal")
]

def get_direction(time1, time2):
    
    def to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m 
    
    start = to_minutes(time1)
    end = to_minutes(time2)

    forward = (end - start) % 1440
    backward = (start - end) % 1440

    if forward < backward:
        return "forward"
    elif backward < forward:
        return "backward"
    else:
        return "equal"


""" 

Forward difference

If you move forward around the clock, the distance is:

forward = (end  - start) mod 1440

If end >= start, this is just end - start.

If end < start, the subtraction is negative, but modulo wraps it around to the correct forward distance.

Example 1:  
Start = 10:00 → 600 minutes
End = 11:00 → 660 minutes
Forward = (660 - 600) % 1440 = 60 minutes.

Example 2 (wrap around):  
Start = 23:50 → 1430 minutes
End = 00:10 → 10 minutes
Forward = (10 - 1430) % 1440 = -1420 % 1440 = 20 minutes.
So moving forward only takes 20 minutes.

Backend difference

If you move backward, the distance is:

backward = (start - end ) mod 1440

If start >= end, this is just start - end.

If start < end, modulo wraps it around to the correct backward distance.

Example 1:  
Start = 10:00 → 600 minutes
End = 11:00 → 660 minutes
Backward = (600 - 660) % 1440 = -60 % 1440 = 1380 minutes.
So backward takes 1380 minutes (much longer than forward).

Example 2 (wrap around):  
Start = 23:50 → 1430 minutes
End = 00:10 → 10 minutes
Backward = (1430 - 10) % 1440 = 1420 minutes.
So backward takes 1420 minutes.


=> Forward  = (end - start) % 1440 -> shortest forward path.
-> backward - (start - end) % 1440 -> shortest backward path.

so the subraction direction matters:

=> Forward: how far end is ahead of start.
-> Backward: how far start is ahead of end.

That's why we use end- start for forward and start - end for backward

"""
from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark(
        {"first": get_direction},
        TESTCASES,
        10000
    )

    unittest.main()