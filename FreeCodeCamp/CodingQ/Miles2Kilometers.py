"""

Miles to Kilometers
Given a distance in miles as a number, return the equivalent distance in kilometers.

The input will always be a non-negative number.
1 mile equals 1.60934 kilometers.
Round the result to two decimal places.

"""

import unittest

class MilesToKilometersTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(convert_to_km(1),1.61)

    def test2(self):
        self.assertEqual(convert_to_km(21),33.8)

    def test3(self):
        self.assertEqual(convert_to_km(3.5),5.63)
    
    def test4(self):
        self.assertEqual(convert_to_km(0),0)

    def test5(self):
        self.assertEqual(convert_to_km(0.621371),1)



def convert_to_km(miles):

    kilometers = miles * 1.60934

    return round(kilometers,2)

    # Or we can write it as return round(miles*1.60934,2)




if __name__ == "__main__":
    print(convert_to_km(10))
    unittest.main()