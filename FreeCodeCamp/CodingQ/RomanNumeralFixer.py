""" 

Roman Numeral Fixer
Given a string of malformed Roman numerals, return the value in standard Roman numeral notation.

The input will only use additive notation, so each symbol adds its value to the total. As a reminder, here are the symbols and values:

Symbol	Value
"I"	1
"V"	5
"X"	10
"L"	50
"C"	100
"D"	500
"M"	1000
When re-encoding, use the largest possible symbol at each step, using subtractive pairs ("IV", "IX", "XL", "XC", "CD", "CM") where needed.
"""



import unittest


class RomanNumeralFixerTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(fix_numerals("XIIIII"), "XV")

    def test2(self):
        self.assertEqual(fix_numerals("IIIILX"), "LXIV")

    def test3(self):
        self.assertEqual(fix_numerals("XXVVVIIIII"), "XL")

    def test4(self):
        self.assertEqual(fix_numerals("MDCCLXXXXVIIII"), "MDCCXCIX")

    def test5(self):
        self.assertEqual(fix_numerals("IIIIVVVVXXXXLLLLCCDD"), "MCDLXIV")

    def test6(self):
        self.assertEqual(fix_numerals("ILCDMIVDIIXLCVCXDL"), "MMCMLXXXIV")


TESTCASES = [
    (("XIIIII",), "XV"),
    (("IIIILX",), "LXIV"),
    (("XXVVVIIIII",), "XL"),
    (("MDCCLXXXXVIIII",), "MDCCXCIX"),
    (("IIIIVVVVXXXXLLLLCCDD",), "MCDLXIV"),
    (("ILCDMIVDIIXLCVCXDL",), "MMCMLXXXIV")
]





def roman_to_int(s):

    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    return sum(values[ch] for ch in s)


def int_to_roman(num):

    mapping = [
        (1000,"M"), (900,"CM"), (500,"D"), (400,"CD"),
        (100,"C"), (90,"XC"), (50,"L"), (40,"XL"),
        (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")
    ]

    result = []

    for val, sym in mapping:
        while num >= val:
            result.append(sym)
            num -= val
    return "".join(result)


def fix_numerals(s):

    return int_to_roman(roman_to_int(s))





from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark({
        "first": fix_numerals
    },
    TESTCASES,
    10000)
    unittest.main()