"""

Array Shift
Given an array and an integer representing how many positions to shift the array, return the shifted array.

A positive integer shifts the array to the left.
A negative integer shifts the array to the right.
The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].
"""

import unittest

class ArrayShiftTest(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(shift_array([1,2,3], 1),[2,3,1])

    def test2(self):
        self.assertEqual(shift_array([1, 2, 3], -1), [3, 1, 2])

    def test3(self):
        self.assertEqual(shift_array(["alpha", "bravo", "charlie"], 5),["charlie", "alpha", "bravo"])

    def test4(self):
        self.assertEqual(shift_array(["alpha", "bravo", "charlie"], -11),["bravo", "charlie", "alpha"])

    def test5(self):
        self.assertEqual(shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15),[5, 6, 7, 8, 9, 0, 1, 2, 3, 4])




def shift_array(arr,n):

    """
    This code also works but it has its own strengths and weakness:

    Strengths:
    => Correct behviour for both left and rifht shifts.
    => Wraps around the array as expected.
    => Handles negative and positive shifts.


    Weaknesses:

    => 1. Inefficient for large shifts
        - insert(0,...) and remove(0) are O(n) operations.
        - For large arrays or large n, this becomes slow.

    => 2. Modulus not used
        - looping abs(n) times even if n is much larger than the array length
        - can reduce n using n % len(arr).

    => 3. Mutates input
        - This function modifies the original array in-place. That's fine if intended, but not always desirable

        The new version is added below.
        => It uses slicing (fast and clean)
        => Avoids mutation
        => Hanldes all edge cases.
    """
    if n < 0:
        direction = "forward"
    else:
        direction = "backward"

    for i in range(0, abs(n)):
        if direction == "forward":
            arr.insert(0,arr.pop())
        else:
            arr.append(arr[0])
            arr.remove(arr[0])

    return arr

def shift_array(arr,k):


    """
        This code works as follows:

        => k % n ensures the shift wraps correctly even for large or negative values
        => For positive k, slice from k to end, then from start to k.
        => for negative k , slice from n + k to end, then from start to n+k.
        """
    n = len(arr)
    if n == 0 or k == 0:
        return arr
    
    k = k%n

    return arr[k:] + arr[:k] if k >= 0 else arr[n+k:] + arr[:n+k]

    







if __name__ == "__main__":
    print(shift_array([1,2,3],1))
    unittest.main()