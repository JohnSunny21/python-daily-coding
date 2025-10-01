import unittest
from BinaryToDec import to_decimal


class BinaryToDecTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(to_decimal("101"),5)

    def test2(self):
        self.assertEqual(to_decimal("1010"),10)

    def test3(self):
        self.assertEqual(to_decimal("10010"),18)

    def test4(self):
        self.assertEqual(to_decimal("1010101"),85)

if __name__ == "__main__":
    unittest.main()