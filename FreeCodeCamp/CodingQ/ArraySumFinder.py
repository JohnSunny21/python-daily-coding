"""

Array Sum Finder
Given an array of numbers and a target number, return the first subset of two or more numbers that adds up to the target.

The "first" subset is the one whose elements have the lowest possible indices, prioritizing the earliest index first.
Each number in the array may only be used once.
If no valid subset exists, return "Sum not found".
Return the matching numbers as an array in the order they appear in the original array.
"""


import unittest

class ArraySumFinderTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(find_sum([1, 3, 5, 7], 6), [1, 5])

    def test2(self):
        self.assertEqual(find_sum([1, 2, 3, 4, 5], 5), [1, 4])

    def test3(self):
        self.assertEqual(find_sum([1, 2, 3, 4, 5], 6), [1, 2, 3])

    def test4(self):
        self.assertEqual(find_sum([-1, -2, 3, 4], 1), [-1, -2, 4])

    def test5(self):
        self.assertEqual(find_sum([3, 1, 4, 1, 5, 9, 2, 6], 10), [3, 1, 4, 2])

    def test6(self):
        self.assertEqual(find_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 20), [1, 2, 3, 5, 9])

    def test7(self):
        self.assertEqual(find_sum([7, 9, 4, 2, 5], 10), "Sum not found")


TESTCASES = [
    (([1, 3, 5, 7], 6,), [1, 5]),
    (([1, 2, 3, 4, 5], 5,), [1, 4]),
    (([1, 2, 3, 4, 5], 6,), [1, 2, 3]),
    (([-1, -2, 3, 4], 1,), [-1, -2, 4]),
    (([3, 1, 4, 1, 5, 9, 2, 6], 10,), [3, 1, 4, 2]),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 20,), [1, 2, 3, 5, 9]),
    (([7, 9, 4, 2, 5], 10,), "Sum not found")
]





def find_sum_first(arr, target):
    n = len(arr)

    # Try subsets starting from the earliest index

    for start in range(n):
        total = arr[start]
        subset = [arr[start]]

        for end in range(start + 1, n):
            total += arr[end]
            subset.append(arr[end])

            if total == target and len(subset) >= 2:
                return subset
            
    return "Sum not found"

""" 
The solution above only checks contiguous forward slices (like [start, start+1, ...] ) and never "drops" elements once the sum overshoots. That's why 
cases like [1, 3, 5, 7] target = 6 fail 

=> we must check all subsets of size >= 2 not just contiguous ones.
=> The "first" subset means:
    1. Prioritize the lowest possible starting index.
    2. Within that, the earliest possible combination.

=> This requires either backtracking or brute force enumeration of subsets.

"""

def find_sum(arr, target):

    n = len(arr)

    # Try subsets starting from the earliest index

    for start in range(n):

        # Explore all subsets beginning at 'start'
        
        for end in range(start + 1, n):

            # Now we need to try combinations that include arr[start] and arr[end]
            # use a simple backtracking search

            def backtrack(idx, subset, total):
                if total == target and len(subset) >= 2:
                    return subset
                if idx >= n or total > target and all(x >= 0 for x in arr):
                    return None
                
                for j in range(idx, n):
                    res = backtrack(j + 1, subset + [arr[j]], total+arr[j])
                    if res:
                        return res
                
                return None
            
            result = backtrack(end, [arr[start]], arr[start])
            if result:
                return result
            
        return "Sum not found"
    



# This is simpler but BRUTE FORCE version

# If preformance isn't criical (arrays are small), you can brute force all subsets.

import itertools

def find_sum_brute(arr, target):
    n = len(arr)


    for size in range(2, n+1):
        for indices in itertools.combinations(range(n), size):
            subset = [arr[i] for i in indices]
            if sum(subset) == target:
                return subset
    
    return "Sum not found"







from utils.benchmark import benchmark

if __name__ == "__main__":

    print(find_sum([1, 2, 3, 4, 5], 5))
    # scores = benchmark(
    #     {"first": find_sum,
    #      "second": find_sum_brute},
    #     TESTCASES,
    #     10000
    # )

    unittest.main()