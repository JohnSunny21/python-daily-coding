import unittest
from threeStrikes import squares_with_three

class threeStrikesTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(squares_with_three(1),0)

    def test2(self):
        self.assertEqual(squares_with_three(10),1)

    def test3(self):
        self.assertEqual(squares_with_three(100),19)

    def test4(self):
        self.assertEqual(squares_with_three(1000),326)

    def test5(self):
        self.assertEqual(squares_with_three(10000),4531)


if __name__ == "__main__":
    unittest.main()