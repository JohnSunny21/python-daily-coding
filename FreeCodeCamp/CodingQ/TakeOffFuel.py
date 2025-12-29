"""  

Takeoff Fuel
Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your destination, determine how many additional gallons of fuel you should add.

1 gallon equals 3.78541 liters.
If the airplane already has enough fuel, return 0.
You can only add whole gallons.
Do not include decimals in the return number.
"""

import unittest

class TakeOffFuelTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(fuel_to_add(0,1), 1)
    
    def test2(self):
        self.assertEqual(fuel_to_add(5, 40), 6)

    def test3(self):
        self.assertEqual(fuel_to_add(10, 30), 0)
    
    def test4(self):
        self.assertEqual(fuel_to_add(896, 20500), 4520)

    def test5(self):
        self.assertEqual(fuel_to_add(1000,50000), 12209)

import math
def fuel_to_add(current_gallons, required_liters):

    # Converting current gallons to liters

    current_liters = current_gallons * 3.78541

    # If already enough fuel, return 0

    if current_liters >= required_liters:
        return 0
    
    needed_liters = required_liters - current_liters

    needed_gallons = needed_liters / 3.78541

    return math.ceil(needed_gallons)



if __name__ == "__main__":
    print(fuel_to_add(10, 50))
    unittest.main()