import unittest
from SecondLargest import second_largest_optimized


class SecondLargestTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(second_largest_optimized([1,2,3,4]),3)

    def test2(self):
        self.assertEqual(second_largest_optimized([20,139,94,67,31]),94)

    def test3(self):
        self.assertEqual(second_largest_optimized([2,3,4,6,6]),4)

    def test4(self):
        self.assertEqual(second_largest_optimized([10,-17,55.5,44,91,0]),55.5)

    def test5(self):
        self.assertEqual(second_largest_optimized([1,0,-1,0,1,0,-1,1,0]),0)


if __name__ == "__main__":
    unittest.main()