""" 

Sorted Array Swap
Given an array of integers, return a new array using the following rules:

Sort the integers in ascending order
Then swap all values whose index is a multiple of 3 with the value before it.
"""

import unittest

class SortedArraySwapTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(sort_and_swap([3, 1, 2, 4, 6, 5]), [1, 2, 4, 3, 5, 6])

    def test2(self):
        self.assertEqual(sort_and_swap([9, 7, 5, 3, 1, 2, 4, 6, 8]), [1, 2, 4, 3, 5, 7, 6, 8, 9])

    def test3(self):
        self.assertEqual(sort_and_swap([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 4, 3, 5, 7, 6, 8, 9])

    def test4(self):
        self.assertEqual(sort_and_swap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11]), [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 11, 12])

    def test5(self):
        self.assertEqual(sort_and_swap([100, -50, 0, 75, -25, 50, -75, 25]), [-75, -50, 0, -25, 25, 75, 50, 100])

    def test6(self):
        self.assertEqual(sort_and_swap([5, 9, 13, 77, 88, 313, -10, -65, 0, 8, 99, 101, -4, 2]), [-65, -10, 0, -4, 2, 8, 5, 9, 77, 13, 88, 101, 99, 313])


TESTCASES = [
    (([3, 1, 2, 4, 6, 5],), [1, 2, 4, 3, 5, 6]),
    (([9, 7, 5, 3, 1, 2, 4, 6, 8],), [1, 2, 4, 3, 5, 7, 6, 8, 9]),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9],), [1, 2, 4, 3, 5, 7, 6, 8, 9]),
    (([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11],), [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 11, 12]),
    (([100, -50, 0, 75, -25, 50, -75, 25],), [-75, -50, 0, -25, 25, 75, 50, 100]),
    (([5, 9, 13, 77, 88, 313, -10, -65, 0, 8, 99, 101, -4, 2],), [-65, -10, 0, -4, 2, 8, 5, 9, 77, 13, 88, 101, 99, 313])
]




def sort_and_swap(arr):

    arr = sorted(arr)

    i = 1
    while i < len(arr):
        if i % 3 == 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        i += 1

    return arr

def sort_and_swap_for(arr):
    arr = sorted(arr)
    # Also we can use the range(1, len(arr)) to cause 0 % 3 == 0 and there is no prev element for it.
    for i in range(len(arr)):
        if i % 3 == 0 and i > 0:
            arr[i] , arr[i-1] = arr[i-1], arr[i]

    return arr





from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark(
       { "first": sort_and_swap,
        "second": sort_and_swap_for},
       TESTCASES,
       10000
    )

    unittest.main()