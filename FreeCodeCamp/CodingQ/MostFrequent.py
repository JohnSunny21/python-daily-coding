"""
Most Frequent
Given an array of elements, return the element that appears most frequently.

There will always be a single most frequent element.
"""

import unittest

class MostFrequentTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(most_frequent(["a","b","a","c"]), "a")

    def test2(self):
        self.assertEqual(most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]), 2)

    def test3(self):
        self.assertEqual(most_frequent([True, False, "False", "True", False]), False)
        
    def test4(self):
        self.assertEqual(most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]), 40)

from collections import Counter
def most_frequent(arr):

    freq = Counter(arr)
    # Here we dont' need the lambda explicitly - Counter has a .get() , so you can write:
    # return max(freq, key=freq.get)
    return max(freq, key=lambda i : freq[i])
    """
    Guarantee: Since the problem states there will always be a single most frequent element, we don't need to handle ties.
    If ties were possible, we'd need extra logic.
    """




if __name__ == "__main__":
    print(most_frequent(["S","u","n","n","y"]))
    unittest.main()

