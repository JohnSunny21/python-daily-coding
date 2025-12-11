"""
Roman Numeral Builder
Given an integer, return its equivalent value in Roman numerals.

Roman numerals use these symbols:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are written from largest to smallest, left to right using the following rules:

Addition is used when a symbol is followed by one of equal or smaller value. For example, 18 is written as XVIII (10 + 5 + 1 + 1 + 1 = 18).
Subtraction is used when a smaller symbol appears before a larger one, to represent 4 or 9 in any place value. For example, 19 is written as XIX (10 + (10 - 1)).
No symbol may be repeated more than three times in a row. Subtraction is used when you would otherwise need to write a symbol more than three times in a row. So the largest number you can write is 3999.
Here's one more example: given 1464, return "MCDLXIV" (1000 + (500 - 100) + 50 + 10 + (5 - 1)).

"""

import unittest

class RomanNumeralBuliderTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(to_roman(18), "XVIII")

    def test2(self):
        self.assertEqual(to_roman(19), "XIX")

    def test3(self):
        self.assertEqual(to_roman(1464), "MCDLXIV")

    def test4(self):
        self.assertEqual(to_roman(2025), "MMXXV")

    def test5(self):
        self.assertEqual(to_roman(3999), "MMMCMXCIX")



def to_roman(num):
    
    # Mapping of values to symbols

    val = [1000, 900, 500, 400,
           100, 90, 50, 40,
           10, 9, 5, 4, 
           1]

    syms = [
        "M","CM","D","CD",
        "C","XC","L","XL",
        "X","IX","V","IV",
        "I"
    ]

    roman = []
    i = 0
    while num > 0:
        count = num // val[i]
        roman.append(syms[i]* count)
        num -= val[i] * count
        i += 1
    return "".join(roman)








if __name__ == "__main__":
    print(to_roman(48))
    unittest.main()