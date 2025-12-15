"""   

Speed Check
Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

1 mile equals 1.60934 kilometers.
If you are travelling less than or equal to the speed limit, return "Not Speeding".
If you are travelling 5 KPH or less over the speed limit, return "Warning".
If you are travelling more than 5 KPH over the speed limit, return "Ticket".

"""

import unittest

class SpeedCheckTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(speed_check(30, 70), "Not Speeding")

    def test2(self):
        self.assertEqual(speed_check(40, 60), "Warning")

    def test3(self):
        self.assertEqual(speed_check(40, 65), "Not Speeding")

    def test4(self):
        self.assertEqual(speed_check(60, 90), "Ticket")
        
    def test5(self):
        self.assertEqual(speed_check(65, 100), "Warning")

    def test6(self):
        self.assertEqual(speed_check(88, 40), "Ticket")


"""
1. Convert the speed from MPH -> KPH using
    speed_kph = speed_mph x 1.60934

2. Compare speed_kph agaisnt the given speed limit:
    -> if speed_kph <= limit -> "Not Speeding"
    -> else if speed_kph - limit <= 5 -> "Warning"
    -> else -> "Ticket" 
"""
def speed_check(speed_mph, speed_limit_kph):

    speed_kph = speed_mph * 1.60934

    if speed_kph <= speed_limit_kph:
        return "Not Speeding"
    elif speed_kph - speed_limit_kph <= 5:
        return "Warning"
    else:
        return "Ticket"
    

if __name__ == "__main__":
    print(speed_check(30, 50))   # Not Speeding (30 mph ≈ 48.28 kph)
    print(speed_check(35, 50))   # Warning (35 mph ≈ 56.33 kph, ~6.33 over → Ticket actually)
    print(speed_check(32, 50))   # Not Speeding (32 mph ≈ 51.5 kph, ~1.5 over → Warning)
    print(speed_check(40, 50))   # Ticket (40 mph ≈ 64.37 kph, ~14.37 over)

    unittest.main()

