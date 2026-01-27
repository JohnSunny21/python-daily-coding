"""   

Odd or Even Day
Given a timestamp (number of milliseconds since the Unix epoch), return:

"odd" if the day of the month for that timestamp is odd.
"even" if the day of the month for that timestamp is even.
For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd" because the day number (27) is an odd number.
"""

import unittest


class OddOrEvenDayTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(odd_or_even_day(1769472000000), "odd")
        
    def test2(self):
        self.assertEqual(odd_or_even_day(1769444440000), "even")

    def test3(self):
        self.assertEqual(odd_or_even_day(6739456780000), "odd")

    def test4(self):
        self.assertEqual(odd_or_even_day(1), "odd")

    def test5(self):
        self.assertEqual(odd_or_even_day(86400000), "even")





from datetime import datetime
def odd_or_even_day(timestamp):

    seconds = timestamp / 1000.0
    date_obj = datetime.fromtimestamp(seconds)

    if date_obj.day % 2 == 0:
        return "even"
    else:
        return "odd"
    
"""

1. Timezone awareness
=> datetime.fromtimestamp() uses the localtimezon of the system.
-> if you want consistent results regradless of environment, use datetime,utcfromtimestamp()

-> otherwise your function may return different results depending on where it runs.
"""

def odd_or_even_day(timestamp):

    dt = datetime.utcfromtimestamp(timestamp / 1000)
    
    day = dt.day

    return "odd" if day % 2 else "even"

"""
=> Use UTC consistently to avoid timezone shifts.
-> datetime.utcfromtimestamp() in Python
-> Parity check is just day % 2
"""
def odd_or_even_day(timestamp):

    return "even" if datetime.utcfromtimestamp(timestamp / 1000).day%2 == 0 else "odd"


odd_or_even_day = lambda ts: "even" if datetime.utcfromtimestamp(ts / 1000).day % 2==0 else "odd"



if __name__ == "__main__":

    unittest.main()


