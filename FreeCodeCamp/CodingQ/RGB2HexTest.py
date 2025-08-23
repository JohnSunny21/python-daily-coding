import unittest
from RGB2Hex import rgb_to_hex

class RGB2HexTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(rgb_to_hex("rgb(255,255,255)"),"#ffffff")

    def test2(self):
        self.assertEqual(rgb_to_hex("rgb(1,11,111)"),"#010b6f")

    def test3(self):
        self.assertEqual(rgb_to_hex("rgb(173,216,230)"),"#add8e6")

    def test4(self):
        self.assertEqual(rgb_to_hex("rgb(79,123,201)"),"#4f7bc9")

if __name__ == "__main__":
    unittest.main()