"""  

Flattened
Given an array, determine if it is flat.

An array is flat if none of its elements are arrays.

"""


import unittest



class FlattendTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(is_flat([1, 2, 3, 4]), True)

      def test2(self):
          self.assertEqual(is_flat([1, [2, 3], 4]), False)

      def test3(self):
          self.assertEqual(is_flat([1, 0, False, True, "a", "b"]), True)

      def test4(self):
          self.assertEqual(is_flat(["a", [0], "b", True]), False)  

      def test5(self):
          self.assertEqual(is_flat([1, [2, [3, [4, [5]]]], 6]), False)



def is_flat(arr):

    for item in arr:
        if isinstance(item, list):
            return False
        
    return True


def is_flat(arr):

    return all(not isinstance(el, list) for el in arr)



if __name__ == "__main__":
    unittest.main()