""" 


Sum of Differences
Given an array of numbers, return the sum of the differences between each number and the one that follows it.

For example, given [1, 3, 4], return 3 (2 + 1).
"""


import unittest

class SumOfDifferencesTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(sum_of_differences([1, 3, 4]), 3)

    def test2(self):
        self.assertEqual(sum_of_differences([5, -3, 3, 9, 10]), 5)

    def test3(self):
        self.assertEqual(sum_of_differences([9, 6, 15, -20, 33, 14, 25, 16, -7]), -16)

    def test4(self):
        self.assertEqual(sum_of_differences([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75]), 25)


TESTCASES = [
    (([1, 3, 4],), 3),
    (([5, -3, 3, 9, 10],), 5),
    (([9, 6, 15, -20, 33, 14, 25, 16, -7],), -16),
    (([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75],), 25)
]




def sum_of_differences(arr):

    diff = sum([arr[i] - arr[i-1] for i in range(1, len(arr))])
    return diff

"""
=> This solution is know as telescoping sum which is elegant, but it only matches the probblem if the array is sorted ascending.
=> But here the problem implies the negative result too so we go with this approach rather than absolute difference
=> The problem statement was a bit ambigious.
=> If interpreted as absolute differences, you'd never get negative results.
=> But the tests clearly show negative are valid, meaning the intended definition is the signed telescoping sum.
=> That reduces to simply arr[-1] - arr[0].
"""

# Simplified Version
def sum_of_differences(arr):
    if not arr:
        return 0
    
    return arr[-1] - arr[0]

# This is O(1) instead of O(n), since you don't need to loop.

""" 
Why arr[1] - arr[0] works

the original loop computes:
    (arr[1] - arr[0] ) + (arr[2] - arr[1]) + (arr[3] - arr[2]) +.... + (arr[n-1] - arr[n-2])

if we expand it, we'll notice something magical:

=> First term: arr[1] - arr[0]
=> Second term: arr[2] - arr[1]
=> Third term: arr[3] = arr[2]
=> ... and so on...

now line them up:

    (arr[i] - arr[0]) + (arr[2] = arr[1]) + (arr[3]  - arr[2]) + ... + (arr[n - 1] - arr[n - 2])

Every middle element cancels out:

=> + arr[1] and - arr[1] cancel.
=> + arr[2] and - arr[2] cancel.
=> .... all the way through.

What's leff is:

    arr[n = 1] = arr[0]

So the entire sum collapses to just the last element minus the first element.

Take = [9, 6, 15, -20]:

    (6 - 9) + (15 - 6) + (-20 - 15)

    = -3 + 9 - 35
    = -29

    now check directly:
     - 20 - 9 = - 29



=> This is called a telescoping sum: Intermediate terms cancel, leaving only the endpoints.
=> That's why you don't need a loop - the math guarntees the middle values don't matter.
=> If you don't spot the cancellation, you'd naturally write the loop. Once you expand a few examples, the pattern becomes obvious.
"""





from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark(
        {"first": sum_of_differences},
        TESTCASES,
        10000
    )

    unittest.main()