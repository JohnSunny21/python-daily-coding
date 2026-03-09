"""

Array Sum
Given an array of numbers, return the sum of all the numbers.
"""

import unittest

class ArraySumTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(sum_array([1, 2, 3, 4, 5]), 15)

      def test2(self):
          self.assertEqual(sum_array([42]), 42)

      def test3(self):
          self.assertEqual(sum_array([5, -2, 7, -3]), 7)

      def test4(self):
          self.assertEqual(sum_array([203, 145, -129, 6293, 523, -919, 845, 2434]), 9395)

      def test5(self):
          self.assertEqual(sum_array([0, 0]), 0)


def sum_array(numbers):

    return sum(numbers)


if __name__ == "__main__":
    unittest.main()