import unittest
from vowelBalance import is_balanced


class vowelBalanceTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_balanced("racecar"),True)

    def test2(self):
        self.assertEqual(is_balanced("Lorem Ipsum"),True)

    def test3(self):
        self.assertEqual(is_balanced("Kitty Ipsum"),False)

    def test4(self):
        self.assertEqual(is_balanced("string"),False)

    def test5(self):
        self.assertEqual(is_balanced(" "),True)

    def test6(self):
        self.assertEqual(is_balanced("abcdefghijklmnopqrstuvwxyz"),False)

    def test7(self):
        self.assertEqual(is_balanced("123A#b!E&#x26;*456-o.U"),True)

if __name__ == "__main__":
    unittest.main()