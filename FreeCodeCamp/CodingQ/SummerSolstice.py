""" 



Summer Solstice
Today is the summer solstice, the longest day of the year in the Northern Hemisphere and the shortest in the Southern. Given a latitude, return a string representing daytime and nighttime hours.

The latitude will be between 90 (north pole) and -90 (south pole), inclusive
The number of daytime hours = 12 + (latitude / 90) * 12
Round the daytime hours to the nearest even number
Return a 24-character string using "☀️" for daytime hours and "🌑" for nighttime hours, where:

Each character represents one hour, starting at midnight (hour 0)
Sunrise and sunset fall symmetrically around noon
For example, a latitude of 0 (the equator) has 12 hours of daylight, so sunrise is at 6:00 AM and sunset is at 6:00 PM. Return: "🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑".
"""


import unittest


class SummerSolsticeTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_daytime_hours(0), "🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑")

    def test2(self):
        self.assertEqual(get_daytime_hours(90), "☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️")

    def test3(self):
        self.assertEqual(get_daytime_hours(-90),"🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑")

    def test4(self):
        self.assertEqual(get_daytime_hours(-33),"🌑🌑🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑🌑🌑")

    def test5(self):
        self.assertEqual(get_daytime_hours(66.5), "🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑")

    def test6(self):
        self.assertEqual(get_daytime_hours(40), "🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑")

    def test7(self):
        self.assertEqual(get_daytime_hours(-50),"🌑🌑🌑🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑🌑🌑🌑")


TESTCASES = [
    ((0,), "🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑"),
    ((90,), "☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️"),
    ((-90,), "🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑"),
    ((-33,), "🌑🌑🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑🌑🌑"),
    ((66.5,), "🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑"),
    ((40,), "🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑"),
    ((-50,), "🌑🌑🌑🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑🌑🌑🌑")
]

"""

we want to simulate how long the daylight lasts depending on your latitude on the summer solstice:

=> At the North Pole(90deg) -> 24 hours of daylight.
=> At the south Pole(-90deg) -> 0 hours of daylight.
=> At the Equator (0deg) -> 12 hours of daylight.

So the formula:
        daytime hours = 12 + latitude / 90 * 12

        gives us the number of daylight hours for the latitude

        

How the hours are placed
We have a 24‑hour day, represented as a string of 24 characters.

"☀️" = daytime hour, "🌑" = nighttime hour.

Sunrise and sunset are symmetric around noon (12:00).

Example: 12 hours of daylight → sunrise at 6 AM, sunset at 6 PM.

Example: 16 hours of daylight → sunrise at 4 AM, sunset at 8 PM.

Example: 20 hours of daylight → sunrise at 2 AM, sunset at 10 PM.


Latitude = 0 (Equator):

Daytime = 
12
+
(
0
/
90
)
×
12
=
12
.

Round to nearest even → 12.

Nighttime = 24 − 12 = 12.

Sunrise = 12/2 = 6 AM.

Sunset = 6 + 12 = 18 (6 PM).

String =
"🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑"




1. Why daytime = int(round(daytime / 2.0) * 2)
The formula gives you a floating‑point number of daylight hours.
Example: latitude 45° → 
12
+
(
45
/
90
)
×
12
=
18
.
Example: latitude 30° → 
12
+
(
30
/
90
)
×
12
=
16
.
Example: latitude 10° → 
12
+
(
10
/
90
)
×
12
≈
13.33
.

But we need the number of daylight hours to be an even integer so that sunrise and sunset can be placed symmetrically around noon.

If you had 13 hours of daylight, sunrise would be at 5.5 AM and sunset at 6.5 PM — half hours don’t fit into our “one character = one hour” string.

By rounding to the nearest even number, we guarantee symmetry.




So:

python
daytime = int(round(daytime / 2.0) * 2)
Divide by 2 → round to nearest integer → multiply back by 2.

This forces the result to be an even number.

Example: 13.33 → 6.67 → round → 7 → ×2 → 14.

Example: 11.9 → 5.95 → round → 6 → ×2 → 12.


2. Why sunrise = nighttime // 2
Total hours = 24.

Nighttime hours = 
24
−
daytime
.

To place sunrise and sunset symmetrically around noon, we split the nighttime evenly:

Half before sunrise.

Half after sunset.

So:

python
sunrise = nighttime // 2
sunset = sunrise + daytime


Example: Equator (latitude 0)
Daytime = 12 → Nighttime = 12.

Sunrise = 12 // 2 = 6 → Sunset = 6 + 12 = 18.

Daylight runs from 6 AM to 6 PM.

Example: Latitude 60° North
Daytime = 20 → Nighttime = 4.

Sunrise = 4 // 2 = 2 → Sunset = 2 + 20 = 22.

Daylight runs from 2 AM to 10 PM.
"""


def get_daytime_hours(latitude):

    # Calculate daytiime hours
    daytime = 12 + (latitude / 90) * 12

    # Round to nearest even number
    daytime = int(round(daytime / 2.0) * 2)

    # Nighttime hours
    nighttime = 24 - daytime
    
    # Sunrise hour = (nightime // 2)
    sunrise = nighttime // 2
    sunset = sunrise + daytime

    result = []

    for hour in range(24):
        if sunrise <= hour < sunset:
            result.append("☀️")
        else:
            result.append("🌑")

    return "".join(result)


""" 

=> Rounding to even ensures we can split the day symmetrically into whole hours.
=> Nightime // 2 ensures, sunrise and sunset are centered around noon.
"""


from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({
        "first": get_daytime_hours
    },TESTCASES, 10000)

    unittest.main()