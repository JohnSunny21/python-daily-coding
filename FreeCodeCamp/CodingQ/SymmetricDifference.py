"""
Symmetric Difference
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays.


"""

import unittest

class SymmetricDifferenceTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(difference([1, 2, 3], [3, 4, 5]), [1, 2, 4, 5])

    def test2(self):
        self.assertEqual(difference(["a", "b"],["c", "b"]),["a", "c"])

    def test3(self):
        self.assertEqual(difference([1, "a", 2],[2, "b", "a"]), [1, "b"])

    def test4(self):
        self.assertEqual(difference([1, 3, 5, 7, 9],[1, 2, 3, 4, 5, 6, 7, 8, 9]),[2, 4, 6, 8])

def difference(arr1, arr2):
    """
    The Limitations for this approach are
    The block of code will include duplicates if the same unique item appears multiple times in 
    one array but not in the other.
    example:
        print(difference([1, 1, 2],[2, 3]))
        # Output: [1, 1, 3] ( but expected [1, 3])

    1. Because both 1's from arr1 get appended.
    2. Efficiency : Each item not in arr2 check is an O(n) membership test on a list. For large arrays, this become slow.
    Using sets would be faster.

    """

    result = []

    for item in arr1:
        if item not in arr2:
            result.append(item)

    for item in arr2:
        if item not in arr1:
            result.append(item)

    return result

def difference(arr1, arr2):
    result = []
    seen = set()

    for item in arr1:
        if item not in arr2 and item not in seen:
            result.append(item)
            seen.add(item)

    for item in arr2:
        if item not in arr1 and item not in seen:
            result.append(item)
            seen.add(item)


    return result






if __name__ == "__main__":
    print(difference([1,1,3], [2, 3, 5]))
    # unittest.main()
