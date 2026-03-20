""" 
Equinox Shadows
Today is the equinox, when the sun is directly above the equator and perfectly overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.

The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
You will only be given a time in 30 minute increments.
Rules:

The sun rises at 6am directly "east", and sets at 6pm directly "west".
A shadow always points opposite the sun.
The shadow's length (in feet) is the number of hours away from noon, cubed.
There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.
Return:

If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
Otherwise, return "No shadow".
For example, given "10:00", return "8ft west" because 10am is 2 hours from noon, so 23 = 8 feet, and the shadow points west because the sun is in the east at 10am.
"""

import unittest
from utils.benchmark import benchmark

class EquinoxShadowsTest(unittest.TestCase):


      def test1(self):
          self.assertEqual(get_shadow("10:00"), "8ft west")

      def test2(self):
          self.assertEqual(get_shadow("15:00"), "27ft east")

      def test3(self):
          self.assertEqual(get_shadow("12:00"), "No shadow")

      def test4(self):
          self.assertEqual(get_shadow("17:30"), "166.375ft east")

      def test5(self):
          self.assertEqual(get_shadow("05:00"), "No shadow")

      def test6(self):
          self.assertEqual(get_shadow("06:00"), "216ft west")

      def test7(self):
          self.assertEqual(get_shadow("18:00"), "No shadow")

      def test8(self):
          self.assertEqual(get_shadow("07:30"), "91.125ft west")

      def test9(self):
          self.assertEqual(get_shadow("00:00"), "No shadow")


def get_shadow(time):

    hour, minutes = map(int, time.split(":"))

    direction = "west"
    if hour < 6 or hour >= 18 or (hour == 12 and minutes == 0):
        return "No shadow"
    
    if hour >= 12:
        direction = "east"


    hours_from_noon = abs(hour + minutes/60 - 12)
    length = hours_from_noon ** 3

    if length.is_integer():
        length = int(length)


    return f"{length}ft {direction}"



if __name__ == "__main__":
    TESTCASES = [
    (("10:00",), "8ft west"),
    (("15:00",), "27ft east"),
    (("12:00",), "No shadow"),
    (("17:30",), "166.375ft east"),
    (("05:00",), "No shadow"),
    (("06:00",), "216ft west"),
    (("18:00",), "No shadow"),
    (("07:30",), "91.125ft west"),
    (("00:00",), "No shadow")
    
]
    
    scores = benchmark(
        {"solution": get_shadow},
        TESTCASES,
        number= 1000
    )
    
    
    unittest.main()