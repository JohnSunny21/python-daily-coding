"""

GCD
Given two positive integers, return their greatest common divisor (GCD).

The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.
For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6. So given 4 and 6, return 2, the largest number that appears in both sets of divisors.
"""

import unittest

class GCDTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(gcd(4, 6),2)

    def test2(self):
        self.assertEqual(gcd(20, 15),5)

    def test3(self):
        self.assertEqual(gcd(13, 17), 1)

    def test4(self):
        self.assertEqual(gcd(654, 456), 6)
    
    def test5(self):
        self.assertEqual(gcd(3456, 4320), 864)




def gcd(x, y):
    min_div = 0
    for i in range(1, y):
        if x%i == 0 and y%i == 0:
            min_div = i

    return min_div

def gcd(x, y):

    while (y!=0):
        x , y = y , x%y
        
    return x



if __name__ == "__main__":
    print(gcd(20, 15))
    unittest.main()