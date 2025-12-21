"""  
Daylight Hours
December 21st is the winter solstice for the northern hemisphere and the summer solstice for the southern hemisphere. That means it's the day with the least daylight in the north and the most daylight in the south.

Given a latitude number from -90 to 90, return a rough approximation of daylight hours on the solstice using the following table:

Latitude	Daylight Hours
-90	24
-75	23
-60	21
-45	15
-30	13
-15	12
0	12
15	11
30	10
45	9
60	6
75	2
90	0
If the given latitude does not exactly match a table entry, use the value of the closest latitude.
"""

import unittest

class DaylightHoursTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(daylight_hours(45), 9)

    def test2(self):
        self.assertEqual(daylight_hours(0), 12)

    def test3(self):
        self.assertEqual(daylight_hours(-90), 24)

    def test4(self):
        self.assertEqual(daylight_hours(-10), 12)

    def test5(self):
        self.assertEqual(daylight_hours(23), 10)
    
    def test6(self):
        self.assertEqual(daylight_hours(88), 0)

    def test7(self):
        self.assertEqual(daylight_hours(-33), 13)

    def test8(self):
        self.assertEqual(daylight_hours(70), 2)


def daylight_hours(latitude):

    solstice_table = {
        -90	:24,
        -75	:23,
        -60	:21,
        -45	:15,
        -30	:13,
        -15	:12,
        0	:12,
        15	:11,
        30	:10,
        45	:9,
        60	:6,
        75	:2,
        90	:0
    }

    while latitude not in solstice_table:
        latitude += 1

    if latitude in solstice_table:
        return solstice_table[latitude]
    
"""
If the latitude isn't in the table, this solution keep incrementing it until it matches a key.

=> Example: latitude = 28 -> loop runs:
    -> 28 not in table -> becomes 29
    -> 29 not in table -> becomes 30
    -> 30 is in table -> stop

=> works for values below a table entry.

⚠️Problems

1. Only increments upward
    -> If latitude = 77 -> loop goes 77 -> 78 -> ... -> 90.
    -> Closest entry should be 75 (2 hours), but your code picks 90 (0 hours).
    -> So it doesn't find the closest, it finds the next higher entry.

2. Infinite loop risk
    -> If latitude > 90 (say 91), it will keep incrementing forever because 91 will never match a key.
3. Doesn't handle negative side properly
    -> If latitude = -77 -> loop goes - 77 -> -76 -> ... -> -75.
    -> That works, but again it's always rounding upward, not finding the nearest.

"""

# ✅ Correct Implementation

def daylight_hours(latitude):

    solstice_table = {
        -90: 24, -75: 23, -60: 21, -45: 15,
        -30: 13, -15: 12, 0: 12, 15: 11,
        30: 10, 45: 9, 60: 6, 75: 2, 90: 0
    }
    
    # Finding the closest latitude key
    closest_lat = min(solstice_table.keys(), key=lambda x: abs(x - latitude))
    
    return solstice_table[closest_lat]

"""  
=> Use a lookup table for exact latitudes.
=> Use min(..., key=lambda x: aba(x - latitude)) (for python) or .reduce() (for JS) to find the closest latitude.
=> This ensures correct approximation for any latitude between -90 and 90.
"""


if __name__ == "__main__":
    print(daylight_hours(76))
    print(daylight_hours(91))
    unittest.main()