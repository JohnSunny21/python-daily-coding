""" 

Parking Fee Calculator
Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.

The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is 2pm for example.
The first string will be the time you parked your car, and the second will be the time you picked it up.
If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.
Fee rules:

Each hour parked costs $3.
Partial hours are rounded up to the next full hour.
If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
There is a minimum fee of $5 (only used if the total would be less than $5).
Return the total cost in the format "$cost", "$5" for example.

"""

import unittest


class ParkingFeeCalculatorTest(unittest.TestCase):


      def test1(self):
          self.assertEqual(calculate_parking_fee("09:00", "11:00"), "$6")

      def test2(self):
          self.assertEqual(calculate_parking_fee("10:00", "10:30"), "$5")

      def test3(self):
          self.assertEqual(calculate_parking_fee("08:10", "10:45"), "$9")

      def test4(self):
          self.assertEqual(calculate_parking_fee("14:40", "23:10"), "$27")

      def test5(self):
          self.assertEqual(calculate_parking_fee("18:15", "01:30"), "$34")

      def test6(self):
          self.assertEqual(calculate_parking_fee("11:11", "11:10"), "$82")




def calculate_parking_fee(park_time, pickup_time):

    start_hour, start_minutes = map(int, park_time.split(":"))
    end_hour, end_minutes = map(int, pickup_time.split(":"))



    total_fee = 0

    if end_hour < start_hour:
        total_fee += 10
        total_hours = (end_hour - start_hour) % 24
        total_fee += total_hours * 3
    else:
        total_hours = end_hour - start_hour
        total_fee += total_hours * 3

    total_minutes = start_minutes + end_minutes

    if total_minutes > 30:
        total_fee += 3
    
    if total_fee < 5:
        total_fee = 5

    return f"${total_fee}"

""" The above solution is incomplete and has some issues with it

=> Hour Calculation: 
    You used (end_hour - start_hour ) % 24. That handles overnight correctly in terms of hours, 
    but it ignores the minutes. For Examples, "14:00" => "16:30" should be 2.5 hours, rounded up to 3. Your code only sees 2 hours and then tries to handle minues separately.

=> Minute handling:
    You added start_minutes + end_minutes and checked if it's greater than 30. That's not the right way to measure
    partial hours, You need the difference in minutes, not the sum. for example, "14:00" => "16:30" should give 150 minutes total not 0 + 30 = 30

=> The mistakes are in the details of time arithmetic (minutes difference vs sum) and the minimum fee ccondition.


===> try to calculate the total minutes first instead of patching  minutes separately.The clean way is to compute total minutes parked, then convert to hours with ceil.
"""









import math
def calculate_parking_fee(park_time, pickup_time):

    h1, m1 = map(int, park_time.split(":"))
    h2, m2 = map(int, pickup_time.split(":"))


    park_minutes = h1*60 + m1
    pickup_minutes = h2*60 + m2

    overnight = False
    if pickup_minutes < park_minutes:
        overnight  = True
        duration = (24*60 - park_minutes) + pickup_minutes
    else:
        duration = pickup_minutes - park_minutes


    hours = math.ceil(duration/ 60)
    cost = hours * 3
    if overnight:
        cost += 10

    if cost < 5:
        cost = 5

    return f"${cost}"


if __name__ == "__main__":
    unittest.main()