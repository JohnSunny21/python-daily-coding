"""
Space Week Day 2: Exoplanet Search
For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
Characters 0-9 correspond to luminosity levels 0-9.
Characters A-Z correspond to luminosity levels 10-35.
A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.

"""
import unittest

class SpaceWeekTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(has_exoplanet("665544554"),False)

    def test2(self):
        self.assertEqual(has_exoplanet("FGFFCFFGG"),True)

    def test3(self):
        self.assertEqual(has_exoplanet("MONOPLONOMONPLNOMPNOMP"),False)

    def test4(self):
        self.assertEqual(has_exoplanet("FREECODECAMP"),True)

    def test5(self):
        self.assertEqual(has_exoplanet("9AB98AB9BC98A"),False)

    def test6(self):
        self.assertEqual(has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE"),True)




def has_exoplanet(readings):

    def char_to_luminus(c):
        if c.isdigit():
            return int(c)
        else:
            return ord(c.upper()) - ord('A') + 10
        
    values = [char_to_luminus(c) for c in readings]
    average = sum(values) / len(values)
    threshold = 0.8 * average

    return any( v <= threshold for v in values)


if __name__ == "__main__":

    print(has_exoplanet("665544554"))
    unittest.main()