"""   
Sorted Array?
Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

If the given array is:

In ascending order (lowest to highest), return "Ascending".
In descending order (highest to lowest), return "Descending".
Not sorted in ascending or descending order, return "Not sorted".
"""

import unittest

class SortedArrayTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_sorted([1, 2, 3, 4, 5]), "Ascending")
        
    def test2(self):
        self.assertEqual(is_sorted([10, 8, 6, 4, 2]), "Descending")
    
    def test3(self):
        self.assertEqual(is_sorted([1, 3, 2, 4, 5]), "Not sorted")

    def test4(self):
        self.assertEqual(is_sorted([3.14, 2.71, 1.61, 0.57]), "Descending")

    def test5(self):
        self.assertEqual(is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]), "Ascending")

    def test6(self):
        self.assertEqual(is_sorted([0.4, 0.5, 0.3]), "Not sorted")





def is_sorted(arr):
    
    sorting = ""

    for i in range(len(arr) - 1):
        if arr[i+1] >= arr[i]:
            pass
        else:
            break
    else:
        sorting = "Ascending"

    
    for i in range(len(arr) - 1):
        if arr[i+1] <= arr[i]:
            pass
        else:
            break
    else:
        sorting = "Descending"


    if sorting:
        return sorting
    
    if not sorting:
        return "Not sorted"
    
"""
=> Using <= and >= makes the check non-strict (so equal elements count as sorted).
=> If there is a need for the strictly increasing/decreasing, replace with < and >.

=> Double loop: runs both loops, even if the firsrt already succeeded. That not wrong. but its a bit redundant.
=> Readability: using for-else is a flex here .
"""
    


def is_sorted_optimized(arr):
    if all(arr[i] <= arr[i+1] for i in range(len(arr) -1)):
        return "Ascending"
    elif all(arr[i] >= arr[i+1] for i in range(len(arr) -1)):
        return "Descending"
    else:
        return "Not sorted"
    

if __name__ == "__main__":
    unittest.main()