import unittest
from DecToBinary import to_binary

class DecToBinaryTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(to_binary(5),"101")

    def test2(self):
        self.assertEqual(to_binary(12),"1100")

    def test3(self):
        self.assertEqual(to_binary(50),"110010")

    def test4(self):
        self.assertEqual(to_binary(99),"1100011")

    

if __name__ == "__main__":
    unittest.main()