import unittest
from factorializer import factorial

class factorializerTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(factorial(0),1)

    def test2(self):
        self.assertEqual(factorial(5),120)

    def test3(self):
        self.assertEqual(factorial(20),2432902008176640000)


if __name__ == "__main__":
    unittest.main()