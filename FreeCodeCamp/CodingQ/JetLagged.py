"""
Jet Lagged
Given a departure city, an arrival city, a flight duration in hours, and a direction of travel, return the number of jet lag hours the traveller is experiencing.

The given cities will be from the following list that includes their UTC offset:

City	Offset
"Los Angeles"	-8
"New York"	-5
"London"	0
"Istanbul"	+3
"Dubai"	+4
"Hong Kong"	+8
"Tokyo"	+9
To calculate jet lag hours:

Find the timezone difference in hours between the two cities.
Determine the direction multiplier. If travelling "east", it's 1.5, otherwise, it's 1.0.
Get the jet lag hours with the formula: timezone difference + (flight duration * 0.1) * direction multiplier
Return the jet lag hours rounded to one decimal place.

"""


import unittest


class JetLaggedTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east"), 6.5)

    def test2(self):
        self.assertEqual(get_jet_lag_hours("London", "New York", 8, "west"), 5.8)

    def test3(self):
        self.assertEqual(get_jet_lag_hours("Hong Kong", "Tokyo", 4, "east"), 1.6)

    def test4(self):
        self.assertEqual(get_jet_lag_hours("Dubai", "London", 7, "west"), 4.7)

    def test5(self):
        self.assertEqual(get_jet_lag_hours("Los Angeles", "Hong Kong", 15, "west"), 17.5)

    def test6(self):
        self.assertEqual(get_jet_lag_hours("Tokyo", "Dubai", 9, "west"), 5.9)

    def test7(self):
        self.assertEqual(get_jet_lag_hours("New York", "Istanbul", 10, "east"), 9.5)


TESTCASES = [
    (("Istanbul", "Hong Kong", 10, "east",), 6.5),
    (("London", "New York", 8, "west",), 5.8),
    (("Hong Kong", "Tokyo", 4, "east",), 1.6),
    (("Dubai", "London", 7, "west",), 4.7),
    (("Los Angeles", "Hong Kong", 15, "west",), 17.5),
    (("Tokyo", "Dubai", 9, "west",), 5.9),
    (("New York", "Istanbul", 10, "east",), 9.5)
]





def get_jet_lag_hours(departure_city, arrival_city, flight_duration, direction):

    city_data = {
        "Los Angeles" : -8,
        "New York": -5,
        "London": 0,
        "Istanbul": 3,
        "Dubai": 4,
        "Hong Kong": 8,
        "Tokyo": 9
    }

    if departure_city not in city_data or arrival_city not in city_data:
        return "Invalid City"
    


    timezone_diff = abs(city_data[arrival_city] - city_data[departure_city])

    direction_multiplier = 1.5 if direction == "east" else 1.0

    return timezone_diff + (flight_duration * 0.1) * direction_multiplier
    # or we can use the return round(, 1) here
    


from utils.benchmark import benchmark

if __name__ == "__main__":


    scores = benchmark(
        {"first": get_jet_lag_hours},
        TESTCASES,
        10000
    )

    unittest.main()
        
