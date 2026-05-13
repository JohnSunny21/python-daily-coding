""" 

Offending Element
Given an array of integers that is sorted in ascending order except for one out-of-place element, return the index of that element.

If more than one element could be considered out of place, return the index of the first one.
"""



import unittest


class OffendingElementTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(find_offender([1, 6, 2, 3, 4, 5]), 1)

    def test2(self):
        self.assertEqual(find_offender([1, 2, 3, 5, 4, 5]), 3)

    def test3(self):
        self.assertEqual(find_offender([2, 1]), 0)

    def test4(self):
        self.assertEqual(find_offender([2, 4, 1, 6, 8]), 2)

    def test5(self):
        self.assertEqual(find_offender([5, 18, 24, 33, 40, 55, 15, 68, 84, 91]), 6)


TESTCASES = [
    (([1, 6, 2, 3, 4, 5],), 1),
    (([1, 2, 3, 5, 4, 5],), 3),
    (([2, 1],), 0),
    (([2, 4, 1, 6, 8],), 2),
    (([5, 18, 24, 33, 40, 55, 15, 68, 84, 91],), 6)
]




def find_offender(arr):

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return i if (i == 0 or arr[i-1] <= arr[i+1]) else i + 1
        
    return -1




from utils.benchmark import benchmark


if __name__ == "__main__":
    scores = benchmark(
        {"first": find_offender},
        TESTCASES,
        10000
    )

    unittest.main()