""" 

Array Chunks
Given an array and a chunk size, return the array split into sub-arrays of that size.

The last chunk may be smaller if the array doesn't divide evenly.
"""


import unittest


class ArrayChunksTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(chunk_array([1, 2, 3, 4, 5, 6], 3), [[1, 2, 3], [4, 5, 6]])

    def test2(self):
        self.assertEqual(chunk_array([1, "two", 3,"four", 5, "six", 7, "eight"], 2), [[1, "two"], [3, "four"], [5, "six"], [7, "eight"]])

    def test3(self):
        self.assertEqual(chunk_array([1, 2, 3, 4, 5], 3), [[1, 2, 3], [4, 5]])

    def test4(self):
        self.assertEqual(chunk_array(["a", "b", "c", "d", "e"], 1), [["a"], ["b"], ["c"], ["d"], ["e"]])

    def test5(self):
        self.assertEqual(chunk_array([1, 2, 3], 5), [[1, 2, 3]])


TESTCASES = [
    (([1, 2, 3, 4, 5, 6], 3,), [[1, 2, 3], [4, 5, 6]]),
    (([1, "two", 3, "four", 5, "six", 7, "eight"],2,), [[1, "two"], [3, "four"], [5, "six"], [7, "eight"]]),
    (([1, 2, 3, 4, 5], 3,), [[1, 2, 3], [4, 5]]),
    ((["a", "b", "c", "d", "e"], 1,), [["a"], ["b"], ["c"], ["d"], ["e"]]),
    (([1, 2, 3], 5,), [[1, 2, 3]])
]


def chunk_array(arr, size):

    new_array = []

    while arr:
        new_array.append(arr[:size])

        arr = arr[size:]

    return new_array


def array_chunk(arr, size):

    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [arr[i: i+size] for i in range(0, len(arr), size)]

"""

=> This is solved with dynamic programming.
    -> ways[i] = number of ways to make i cents.
    -> For each coin, update the ways array.

=> Ensures combinations are counted without duplication.
-> Efficient: runs in O(amount * number_of_coins).

For example, amount = 10:

    -> Using only pennis -> 1 way.
    -> Using nickels -> 2 ways( 10, 5 + 5)
    -> Using dimes -> 1 way( 10), Total 4 ways.
    
"""


from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": chunk_array, "second": array_chunk}, TESTCASES, 10000)
    unittest.main()