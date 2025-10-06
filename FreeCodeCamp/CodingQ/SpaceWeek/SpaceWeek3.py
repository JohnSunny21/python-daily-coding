"""
Space Week Day 3: Phone Home
For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

The first value in the array is the distance from your location to the first satellite.
Each subsequent value, except for the last, is the distance to the next satellite.
The last value in the array is the distance from the previous satellite to your home planet.
The message travels at 300,000 km/s.
Each satellite the message passes through adds a 0.5 second transmission delay.
Return a number rounded to 4 decimal places, with trailing zeros removed.
"""

import unittest

class SpaceWeekTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(send_message([300000,300000]),2.5)

    def test2(self):
        self.assertEqual(send_message([384400,384400]),3.0627)

    def test3(self):
        self.assertEqual(send_message([54600000,54600000]),364.5)
    
    def test4(self):
        self.assertEqual(send_message([1000000,500000000,1000000]),1674.3333)

    def test5(self):
        self.assertEqual(send_message([10000, 21339, 50000, 31243, 10000]),2.4086)

    def test6(self):
        self.assertEqual(send_message([802101, 725994, 112808, 3625770, 481239]),21.1597)










def send_message(route):


    total_distance = sum(route)
    total_num_of_satellites = route[:-1]

    total_time = (total_distance / 300000) + len(total_num_of_satellites) * 0.5

    return round(total_time,4)

"""

 Why round(total_time, 4) gives 4 decimal places
Yes, round(total_time, 4) returns a float rounded to 4 decimal places. But floats in Python don’t preserve trailing zeros — so round(2.5, 4) gives 2.5, not 2.5000.
To force 4 decimal places, we use:
format(round(total_time, 4), '.4f')  # → '2.5000'


Then we strip trailing zeros with:
.rstrip('0')  # → '2.5'



❓ Why .rstrip('.') is used
This is a defensive edge-case guard. After stripping trailing zeros, you might end up with a string like:
'2.'  # ← not ideal


This happens when the number is something like 2.0000:
- format(..., '.4f') → '2.0000'
- .rstrip('0') → '2.'
- .rstrip('.') → '2'
So .rstrip('.') ensures you don’t return a number with a dangling decimal point.

🧪 Example
total_time = 2.0000
formatted = format(round(total_time, 4), '.4f')  # '2.0000'
cleaned = formatted.rstrip('0').rstrip('.')      # '2'



🔍 Did the question require it?
No, the prompt didn’t explicitly mention this edge case. But it did say:
“Return a number rounded to 4 decimal places, with trailing zeros removed.”

So .rstrip('.') is a safe polish to prevent awkward outputs like '2.'.



"""
def send_message_edge(route):
    speed = 300_000  # km/s

    travel_time = sum(route) / speed
    satellite_delay = 0.5 * (len(route) - 1)
    total_time = travel_time + satellite_delay

    # The result is returning the string but we need the number with the decimal places
    refined_time = format(round(total_time,4), '.4f').rstrip('0').rstrip('.') if '.' in str(total_time) else str(total_time)

    return float(refined_time)

if __name__ == "__main__":

    print(send_message([300000,300000]))
    unittest.main()