"""   
Array Swap
Given an array with two values, return an array with the values swapped.

For example, given ["A", "B"] return ["B", "A"].
"""

import unittest

class ArraySwapTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(array_swap(["A", "B"]), ["B", "A"])

    def test2(self):
        self.assertEqual(array_swap([25, 20]), [20, 25])

    def test3(self):
        self.assertEqual(array_swap([True, False]), [False, True])

    def test4(self):
        self.assertEqual(array_swap(["1", 1]), [1, "1"])



def array_swap(arr):

    a, b = arr

    return [b, a]


def array_swap(arr):

    return [arr[1], arr[0]]

"""  
---> Since the array always has exactly two values, you can directly return them in reversed order.

---> If you wanted to handle arrays of any length, you could use:
        -> Python: arr[::-1]
        -> JavaScript: arr.reverse()
"""



if __name__ == "__main__":
    print(array_swap(["B", "C"]))
    unittest.main()