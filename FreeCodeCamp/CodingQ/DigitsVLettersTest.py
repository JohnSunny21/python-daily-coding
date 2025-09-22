import unittest

from DigitsVLetters import digits_or_letters

class DigitsVLettersTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(digits_or_letters("abc123"),"tie")
    
    def test2(self):
        self.assertEqual(digits_or_letters("a1b2c3d"),"letters")

    def test3(self):
        self.assertEqual(digits_or_letters("1a2b3c4"),"digits")
    
    def test4(self):
        self.assertEqual(digits_or_letters("abc123!@#DEF"),"letters")

    def test5(self):
        self.assertEqual(digits_or_letters("H3110 W0R1D"),"digits")

    def test6(self):
        self.assertEqual(digits_or_letters("P455W0RD"),"tie")


if __name__ == "__main__":
    unittest.main()