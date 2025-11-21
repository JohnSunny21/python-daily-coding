"""
LCM
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

Multiples of 4 are 4, 8, 12 and so on.
Multplies of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both.


FOR ADDITIONAL REFERENCE : https://www.geeksforgeeks.org/python/python-program-to-find-lcm-of-two-numbers/
"""

import unittest,math

class LCMTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(lcm(4,6),12)
    
    def test2(self):
        self.assertEqual(lcm(9,6),18)

    def test3(self):
        self.assertEqual(lcm(10,100),100)
    
    def test4(self):
        self.assertEqual(lcm(13,17),221)

    def test5(self):
        self.assertEqual(lcm(45,70),630)




def lcm(a,b):
    gcd = math.gcd(a,b)
    lcm = (a* b) // gcd

    return lcm

def gcd(a,b):

    while b:
        a , b = b, a% b
    return a

def lcm_using_gcd(a,b):
    gcd = gcd(a,b)

    return abs(a * b) // gcd

"""
The GCD ensures we don't double-count common factors
Multiplying  a * b gives a common multiple, but dividng by GCD(a, b) reduces it to the smallest common multiple
Efficient: runs O(logmin(a,b))


Edge cases:
If either number is 0, the LCM is conventionally 0 (since no positive multiple exists).
Words for negative inputs too, because of abs(a * b).
"""

if __name__ == "__main__":
    print(lcm(9,6))
    unittest.main()