""" 

What Day Is It?
Given a Unix timestamp in milliseconds, return the day of the week.

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


class WhatDayIsItTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_day_of_week(1775492249000), "Monday")

    def test2(self):
        self.assertEqual(get_day_of_week(1766246400000), "Saturday")

    def test3(self):
        self.assertEqual(get_day_of_week(33791256000000), "Tuesday")

    def test4(self):
        self.assertEqual(get_day_of_week(1773576000000), "Sunday")

    def test5(self):
        self.assertEqual(get_day_of_week(0), "Thursday")


import datetime
def get_day_of_week(timestamp_ms: int) -> str:

    timestamp_s = timestamp_ms / 1000

    dt = datetime.datetime.utcfromtimestamp(timestamp_s)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return days[dt.weekday()]

"""
The above solution does not work for the test case like 

        self.assertEqual(get_day_of_week(33791256000000), "Tuesday")

The error happens because the timestamp we passed in (33791256000000 ms) is way outside the range that your local
Python build of datetime can handle.

=> datetime.utcfromtimestamp() expects seconds since epoch, so you divided by 1000 => 33791256000 seconds.
=> That corresponds to a date around the year 3050 CE.
=> On many online platforms (Like CPython builds combined with 64-bit time support, this works fine).
=> But on the windows with certain Python builds, the underlying C runtime only supports timestamps up to around
    the year 3000 or so. That's why you get OSError: [Errno 22] Invalid argument.

We solved the above problem in the below solution


"""

def get_day_of_week(timestamp_ms):

    # Epoch start
    epoch = datetime.datetime(1970, 1, 1)

    # Add milliseconds as timedelta
    dt = epoch + datetime.timedelta(milliseconds=timestamp_ms)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return days[dt.weekday()]
"""

This way you're not relying on utcfromtimestamp, so you won't hit the platform's timestamp range limits.

=> utcfromtimestamp delegates to the OS C runtime, which has platform-specific limits.
=> Using timedelta from the epoch is pure Python Arithmatic, so it works for very large timestamps.
"""



from utils.benchmark import benchmark

if __name__ == "__main__":

    TESTCASES = [
    ((1775492249000,), "Monday"),
    ((1766246400000,), "Saturday"),
    ((33791256000000,), "Tuesday"),
    ((1773576000000,), "Sunday"),
    ((0,), "Thursday")
]
    scores = benchmark({
        "first": get_day_of_week
    },
    TESTCASES,
    10000)

    unittest.main()