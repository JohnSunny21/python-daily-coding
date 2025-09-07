import unittest
from RomanNumeralParser import parse_roman_numeral

class RomanNumeralParserTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(parse_roman_numeral("III"),3)

    def test2(self):
        self.assertEqual(parse_roman_numeral("IV"),4)

    def test3(self):
        self.assertEqual(parse_roman_numeral("XXVI"),26)

    def test4(self):
        self.assertEqual(parse_roman_numeral("XCIX"),99)

    def test5(self):
        self.assertEqual(parse_roman_numeral("CDLX"),460)

    def test6(self):
        self.assertEqual(parse_roman_numeral("DIV"),504)

    def test7(self):
        self.assertEqual(parse_roman_numeral("MMXXV"),2025)


if __name__ == "__main__":
    unittest.main()