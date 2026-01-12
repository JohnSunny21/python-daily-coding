"""  
Plant the Crop
Given an integer representing the size of your farm field, and "acres" or "hectares" representing the unit for the size of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.

1 acre equals 4046.86 square meters.
1 hectare equals 10,000 square meters.
Here's a list of crops that will be given as input and how much space a single plant takes:

Crop	Space per plant
"corn"	1 square meter
"wheat"	0.1 square meters
"soybeans"	0.5 square meters
"tomatoes"	0.25 square meters
"lettuce"	0.2 square meters
Return the number of plants that fit in the field, rounded down to the nearest whole plant.
"""

import unittest

class PlantTheCropTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_number_of_plants(1, "acres", "corn"), 4046)

    def test2(self):
        self.assertEqual(get_number_of_plants(2, "hectares", "lettuce"), 100000)
        
    def test3(self):
        self.assertEqual(get_number_of_plants(20, "acres", "soybeans"), 161874)

    def test4(self):
        self.assertEqual(get_number_of_plants(3.75, "hectares", "tomatoes"), 150000)

    def test5(self):
        self.assertEqual(get_number_of_plants(16.75, "acres","tomatoes"), 271139)



def get_number_of_plants(field_size, unit, crop):

    field_in_sq_meters = field_size * 4046.86 if unit == "acres" else field_size * 10000

    no_of_plants = 0
    if crop == "corn":
        no_of_plants = field_in_sq_meters // 1
    elif crop == "wheat":
        no_of_plants = field_in_sq_meters / 0.1
    elif crop == "soybeans":
        no_of_plants = field_in_sq_meters / 0.5
    elif crop == "tomatoes":
        no_of_plants = field_in_sq_meters // 0.25
    else:
        no_of_plants = field_in_sq_meters / 0.2

    return round(no_of_plants)


"""  
The above code passes the test cases but there are some issues in the above code

=> The floor division (//) and true division (/) mixed inconsistently, and then applying round() at the end.That combination is what makes the lettuce case behave differently.

=> For "corn" and "tomatoes" used // (floor division).That already produces an integer result, so round() doesn't change anything.
=> For "wheat", "soybeans", and "lettuce" used / (true division). That produces a float, and then round() rounds it to the nearest integer - not always down.
=> The problem here is : 
        We have a requirement of "rounded down to the nearest whole plant", round() does banker's rounding (to nearest, with ties to even), not floor.
        Example:

            >>> round(5.5) # rounds to nearest even
            6
            >>> round(5.1)
            5


        -> So if the division gives something like 12345.5, round() may round up, which violates the "always down" rule.
=> That's why lettuce fails when we try to use the // -- because you're inconsistently applying floor vs round.


===> You should always floor the result, regardless of crop. That means:
        -> Use / for division (so you get the float).
        -> Then apply math.floor() (or // consistently).
        The below is the clean version.
===> Here the mistake is using the round instead of flooring.
===> round() sometimes rounds up, but the problem statement requires always rounding down.
===> Fix: use math.floor() or consistent // division for all crops.
"""

import math
def get_number_of_plants(field_size, unit,crop):

    if unit == "acres":
        area_m2 = field_size * 4046.86
    elif unit == "hectares":
        area_m2 = field_size * 10000
    else: 
        raise ValueError("Unit must be 'acres' or 'hectares'")
    
    crop_space = {
        "corn": 1.0,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2
    }

    if crop not in crop_space:
        raise ValueError("Invalid crop type")
    
    plants = math.floor(area_m2 / crop_space[crop])

    return plants


""" 
=> Convert field size -> square meters.
=> Divide by crop's space requirements.
=> Round down with math.floor(Python) or Math.floor(JS).
"""

def get_number_of_plants_refined(field_size, unit, crop):

    field_in_sq_meters = field_size * 4046.86 if unit == "acres" else field_size * 10000

    crop_space = {
        "corn": 1.0,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2
    }

    return math.floor(field_in_sq_meters / crop_space[crop])

def get_number_of_plants_one_liner(field_size, unit, crop):

    return math.floor((field_size * (4046.86 if unit == "acres" else 10000)) / {
        "corn": 1.0,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2
    }[crop])




if __name__== "__main__":
    unittest.main()