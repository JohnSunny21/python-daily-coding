""" 


Prank Number
Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.

The pattern will be one of:

The numbers increase from one to the next by a fixed amount (addition).
The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].
"""

import unittest

class PrankNumberTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(fix_prank_number([2, 4, 7, 8, 10]), [2, 4, 6, 8, 10])

    def test2(self):
        self.assertEqual(fix_prank_number([10, 10, 8, 7, 6]), [10, 9, 8, 7, 6])

    def test3(self):
        self.assertEqual(fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]), [12, 24, 36, 48, 60, 72, 84, 96])

    def test4(self):
        self.assertEqual(fix_prank_number([4, 1, -2, -5, -8, -5]), [4, 1, -2, -5, -8, -11])

    def test5(self):
        self.assertEqual(fix_prank_number([0, 100, 200, 300, 150, 500]), [0, 100, 200, 300, 400, 500])

    def test6(self):
        self.assertEqual(fix_prank_number([400, 425, 400, 375, 350, 325, 300]), [450, 425, 400, 375, 350, 325, 300])

    def test7(self):
        self.assertEqual(fix_prank_number([-5, 5, 10, 15, 20]), [0, 5, 10, 15, 20])


from collections import Counter

def fix_prank_number(arr):

    n = len(arr)

    # Step 1: compute diffs
    diffs = [arr[i+1] - arr[i] for i in range(n - 1)]

    # Step 2: most common diff
    diff = Counter(diffs).most_common(1)[0][0]

    # Step 3: find correct starting index
    start = 0
    for i in range(n - 1):
        if arr[i+1] - arr[i] == diff:
            start = i
            break

    # Step 4: rebuild correct sequence
    expected = [0] * n
    expected[start] = arr[start]

    # forward
    for i in range(start + 1, n):
        expected[i] = expected[i - 1] + diff

    
    # backward
    for i in range(start-1, -1, -1):
        expected[i] = expected[i+1] - diff

    return expected




from utils.benchmark import benchmark
if __name__ == "__main__":


    TESTCASES = [
    (([2, 4, 7, 8, 10],), [2, 4, 6, 8, 10]),
    (([10, 10, 8, 7, 6],), [10, 9, 8, 7, 6]),
    (([12, 24, 36, 48, 61, 72, 84, 96],), [12, 24, 36, 48, 60, 72, 84, 96]),
    (([4, 1, -2, -5, -8, -5],), [4, 1, -2, -5, -8, -11]),
    (([0, 100, 200, 300, 150, 500],), [0, 100, 200, 300, 400, 500]),
    (([400, 425, 400, 375, 350, 325, 300],), [450, 425, 400, 375, 350, 325, 300]),
    (([-5, 5, 10, 15, 20],), [0, 5, 10, 15, 20])
]
    
    scores = benchmark(
        {"first": fix_prank_number},
        TESTCASES,
        10000
    )

    unittest.main()