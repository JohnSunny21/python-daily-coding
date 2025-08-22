import unittest
from tribonacciSequence import tribonacci_sequence

class tribonacciSequenceTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(tribonacci_sequence([0, 0, 1], 20), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513])

    def test2(self):
        self.assertEqual(tribonacci_sequence([21, 32, 43], 1),[21])

    def test3(self):
        self.assertEqual(tribonacci_sequence([0, 0, 1], 0),[])

    def test4(self):
        self.assertEqual(tribonacci_sequence([10,20,30],2),[10,20])

    def test5(self):
        self.assertEqual(tribonacci_sequence([10, 20, 30], 3),[10, 20, 30])

    def test6(self):
        self.assertEqual(tribonacci_sequence([123, 456, 789], 8),[123, 456, 789, 1368, 2613, 4770, 8751, 16134])




if __name__ == "__main__":
    unittest.main()