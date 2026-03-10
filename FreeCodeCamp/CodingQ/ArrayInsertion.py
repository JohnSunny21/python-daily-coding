""" 

Array Insertion
Given an array, a value to insert into the array, and an index to insert the value at, return a new array with the value inserted at the specified index.
"""


import unittest

class ArrayInsertionTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(insert_into_array([2, 4, 8, 10], 6, 2), [2, 4, 6, 8, 10])

      def test2(self):
          self.assertEqual(insert_into_array(["the", "quick", "fox"], "brown", 2), ["the", "quick", "brown", "fox"])

      def test3(self):
          self.assertEqual(insert_into_array([], 0, 0), [0])

      def test4(self):
          self.assertEqual(insert_into_array([0, 1, 1, 2, 3, 8, 13], 5, 5), [0, 1, 1, 2, 3, 5, 8, 13])




def insert_into_array(arr, value,index):


    arr.insert(index, value)

    return arr

# This solution works because list.insert() mutates the list in place. It's simple
# efficient. Just note if you want a new array without mutating the original, you'd need slicing.


def insert_into_array(arr, value,index):

    return arr[:index] + [value] + arr[index:]




if __name__ == "__main__":
    unittest.main()