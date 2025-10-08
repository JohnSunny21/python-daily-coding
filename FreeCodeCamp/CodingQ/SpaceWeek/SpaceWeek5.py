"""
Space Week Day 5: Goldilocks Zone
For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.

Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:

Find the luminosity of the star by raising its mass to the power of 3.5.
The start of the zone is 0.95 times the square root of its luminosity.
The end of the zone is 1.37 times the square root of its luminosity.
Return the distances rounded to two decimal places.
For example, given 1 as a mass, return [0.95, 1.37].
"""

import unittest
import math

class SpaceWeek5(unittest.TestCase):

    def test1(self):
        self.assertEqual(goldilocks_zone(1),[0.95,1.37])
    
    def test2(self):
        self.assertEqual(goldilocks_zone(0.5),[0.28,0.41])

    def test3(self):
        self.assertEqual(goldilocks_zone(6),[21.85,31.51])

    def test4(self):
        self.assertEqual(goldilocks_zone(3.7),[9.38,13.52])

    def test5(self):
        self.assertEqual(goldilocks_zone(20),[179.69,259.13])


def goldilocks_zone(mass):

    luminosity = mass ** 3.5

    start_zone = (luminosity**0.5) * 0.95
    end_zone = (luminosity**0.5) * 1.37

    return [round(start_zone,2),round(end_zone,2)]

def goldilocks_zone_refined(mass):

    luminosity = mass ** 3.5
    sqrt_luminosity = math.sqrt(luminosity)
    start = round(0.95 * sqrt_luminosity, 2)
    end = round(1.37 * sqrt_luminosity, 2)
    return [start, end]


if __name__ == "__main__":
    print(goldilocks_zone(0.5))
    unittest.main()