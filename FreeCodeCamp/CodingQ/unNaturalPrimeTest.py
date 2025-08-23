import unittest
from unNaturalPrime import is_unnatural_prime

class unNaturalPrimeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_unnatural_prime(1),False)
    
    def test2(self):
        self.assertEqual(is_unnatural_prime(-1),False)

    def test3(self):
        self.assertEqual(is_unnatural_prime(19),True)

    def test4(self):
        self.assertEqual(is_unnatural_prime(-23),True)

    def test5(self):
        self.assertEqual(is_unnatural_prime(0),False)
    
    def test6(self):
        self.assertEqual(is_unnatural_prime(97),True)
    
    def test7(self):
        self.assertEqual(is_unnatural_prime(-61),True)
    
    def test8(self):
        self.assertEqual(is_unnatural_prime(99),False)
    
    def test9(self):
        self.assertEqual(is_unnatural_prime(-44),False)


if __name__ == "__main__":
    unittest.main()