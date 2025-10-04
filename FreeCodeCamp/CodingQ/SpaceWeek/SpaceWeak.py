"""
Space Week Day 1: Stellar Classification
October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:

"O": 30,000 K or higher

"B": 10,000 K - 29,999 K

"A": 7,500 K - 9,999 K

"F": 6,000 K - 7,499 K

"G": 5,200 K - 5,999 K

"K": 3,700 K - 5,199 K

"M": 0 K - 3,699 K

Return the classification of the given star.
"""
import unittest
class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(classification(5778),"G")

    def test2(self):
        self.assertEqual(classification(2400),"M")
    
    def test3(self):
        self.assertEqual(classification(9999),"A")
    
    def test4(self):
        self.assertEqual(classification(3700),"K")

    def test5(self):
        self.assertEqual(classification(3699),"M")

    def test6(self):
        self.assertEqual(classification(210000),"O")

    def test7(self):
        self.assertEqual(classification(6000),"F")

    def test8(self):
        self.assertEqual(classification(11432),"B")









def classification(temp):

    if temp <= 3699:
        temp = 'M'
    elif 3700 <= temp <= 5199:
        temp = 'K'
    elif 5200 <= temp <= 5999:
        temp = 'G'
    elif 6000 <= temp <= 7499:
        temp = 'F'
    elif 7500 <= temp <= 9999:
        temp ='A'
    elif 10000 <= temp <= 29999:
        temp = 'B'
    else:
        temp = 'O'

    return temp

# Alternate method
def classify_star(temp):

    if temp >= 30000:
        return 'O'
    elif temp >= 10000:
        return 'B'
    elif temp >= 7500:
        return 'A'
    elif temp >= 6000:
        return 'F'
    elif temp >= 5200:
        return 'G'
    elif temp >= 3700:
        return 'K'
    elif temp >= 0:
        return 'M'
    else:
        raise ValueError("Temperature must be a non-negative numder.")

if __name__ == "__main__":
    print(classification(5778))
    unittest.main()