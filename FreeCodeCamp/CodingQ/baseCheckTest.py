import unittest
from baseCheck import is_valid_number


class baseCheckTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_valid_number("10101",2),True)

    def test2(self):
        self.assertEqual(is_valid_number("10201",2),False)

    def test3(self):
        self.assertEqual(is_valid_number("76543210",8),True)

    def test4(self):
        self.assertEqual(is_valid_number("9876543210",8),False)

    def test5(self):
        self.assertEqual(is_valid_number("9876543210", 10),True)

    def test6(self):
        self.assertEqual(is_valid_number("ABC", 10),False)

    def test7(self):
        self.assertEqual(is_valid_number("ABC", 16),True)

    def test8(self):
        self.assertEqual(is_valid_number("Z", 36),True)

    def test9(self):
        self.assertEqual(is_valid_number("ABC", 20),True)

    def test10(self):
        self.assertEqual(is_valid_number("4B4BA9", 16),True)
    
    def test11(self):
        self.assertEqual(is_valid_number("5G3F8F", 16),False)

    def test12(self):
        self.assertEqual(is_valid_number("5G3F8F", 17),True)

    def test13(self):
        self.assertEqual(is_valid_number("abc", 10),False)

    def test14(self):
        self.assertEqual(is_valid_number("abc", 16),True)
    
    def test15(self):
        self.assertEqual(is_valid_number("AbC", 16),True)
        
    def test16(self):
        self.assertEqual(is_valid_number("z", 36),True)



if __name__ == "__main__":
    unittest.main()