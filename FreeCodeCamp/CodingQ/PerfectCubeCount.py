"""  

Perfect Cube Count
Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

The lower number is not garanteed to be the first argument.
A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27.
"""


import unittest


class PerfectCubeCountTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(count_perfect_cubes(3, 30), 2)

      def test2(self):
          self.assertEqual(count_perfect_cubes(1, 30), 3)

      def test3(self):
          self.assertEqual(count_perfect_cubes(30, 0), 4)

      def test4(self):
          self.assertEqual(count_perfect_cubes(-64, 64), 9)

      def test5(self):
          self.assertEqual(count_perfect_cubes(9214, -8127), 41)


def count_perfect_cubes(a, b):

    if a > b:
        a, b = b, a

    def is_perfect_cube(n):

        # Hande negatives by searching absolute value
        
        low, high = (n, 0) if n < 0 else (0, n)

        

        while low <= high:
            mid = (low + high) // 2
            cubued = mid * mid * mid

            if cubued == n:
                return True
            elif cubued > n:
                high = mid - 1
            elif cubued < n:
                low = mid + 1

        return False
    

    counter = 0

    for i in range(a , b+1):
        if is_perfect_cube(i):
            counter += 1

    return counter


"""
This binary search approach works, but it's overkill  for this problem.
A simpler and faster way is to just computer cube roots directly shown below. because we only need to know how many cubes
fall in the range, not test each number individually.

=> One more thing to consider
    1. Negative ranges: the binary search is_perfect_cube only works for non-negative numbers, because you set low = 0, and high = n,
    For negative n, that logic breaks, but negative numbers can also be perfect cubes(e.g.. -64 = (-4)^3)

    2. Inefficienty: Looping through every number between a and b is very slow for large ranges (like -8127 to 9214). Instead, we should directly compute 
    the roots and count how many integers fall in that range.
"""

import math
def count_perfect_cubes(a, b):

    low, high = min(a, b), max(a, b)

    # smallest integer cube root >= low
    start = math.ceil(low ** (1/ 3)) if low >= 0 else math.ceil(- ((-low) ** (1 / 3)))

    # largest integer cube root <= high
    end = math.floor(high ** (1 / 3)) if high >= 0 else math.floor(-((-high) ** (1 / 3)))

    if start > end:
        return 0
    return end - start + 1


"""
This works
and efficient because
=> we don't check every number. instead:
    -> Compute the cube root of the lower bound -> round up (ceil) to find the first integer cube 
    root inside the range.
    -> Compute the cube root of the upper bound -> round down (floor) to find the last integer cude root
    inside the range.
    -> The count is simply end - start + 1
    -> Works for negative ranges because cube roots of negatives are negative integers.

    This version is O(1), handles huge ranges


"""




"""
===============================================================================
WHY THE PREVIOUS IMPLEMENTATIONS FAILED
===============================================================================

Two test cases were failing:

    1) count_perfect_cubes(-64, 64)         -> Expected: 9
    2) count_perfect_cubes(9214, -8127)     -> Expected: 41

-------------------------------------------------------------------------------
PROBLEM #1 — Floating Point Cube Root Precision
-------------------------------------------------------------------------------

Earlier we tried:

    start = ceil(low ** (1/3))
    end   = floor(high ** (1/3))

This works in theory, but fails in Python due to floating-point precision.

Example:

    (-64) ** (1/3)

This does NOT return exactly -4.
It returns something like:

    -3.999999999999

Then:

    ceil(-3.999999999999) -> -3   (WRONG)

But the correct cube root boundary should be -4.

This caused the counting range to shift incorrectly,
which made some test cases fail.

Key lesson:
Never use floating roots when exact integer boundaries matter.

-------------------------------------------------------------------------------
PROBLEM #2 — Incorrect Handling of Negative Floor Cube Roots
-------------------------------------------------------------------------------

We then tried to fix it with integer cube root logic:

    if n < 0:
        return -integer_cuberoot_floor(-n)

This is mathematically incorrect.

Why?

Because floor behaves differently for negative numbers.

Example:
We need the largest integer r such that:

    r³ <= -8127

Check:

    (-21)³ = -9261   <= -8127  ✓
    (-20)³ = -8000   >  -8127  ✗

So the correct floor cube root of -8127 is:

    -21

But our negation shortcut returned:

    -20   (WRONG)

This caused:

    count_perfect_cubes(9214, -8127)

to produce an incorrect result instead of 41.

Key lesson:
You cannot mirror positive floor logic for negatives.
You must compute cube roots over the full integer range.

-------------------------------------------------------------------------------
WHAT WE DID TO FIX IT
-------------------------------------------------------------------------------

We implemented a proper integer binary search that works
for both positive and negative numbers.

Instead of converting negative to positive and flipping sign,
we search across the full possible range:

    low  = -abs(n)  (if n is negative)
    high =  abs(n)

This guarantees correct floor behavior:

    floor cube root = largest r such that r³ <= n
    ceil cube root  = smallest r such that r³ >= n

Now:

    count_perfect_cubes(-64, 64)        -> 9
    count_perfect_cubes(9214, -8127)    -> 41

Both pass correctly.

-------------------------------------------------------------------------------
FINAL LESSON
-------------------------------------------------------------------------------

1) Avoid floating-point math for exact integer boundary problems.
2) Floor and ceil behave differently for negative numbers.
3) When in doubt, use integer binary search for mathematical precision.

This bug was not about math knowledge —
it was about precision and careful boundary handling.
===============================================================================
"""


def integer_cuberoot_floor(n):
    """ 
    Largest integer r such that r^3 <= n
    Works for negative and positive n.
    """

    low = -abs(n) if n < 0 else 0
    high = abs(n)

    while low <= high:
        mid = (low + high) // 2
        cube = mid ** 3

        if cube == n:
            return mid
        elif cube < n:
            low = mid + 1
        elif cube > n:
            high = mid - 1

    return high

def integer_cuberoot_ceil(n):

    """
    Smallest integer r such that r^3 >=n
    """

    floor_root = integer_cuberoot_floor(n)
    if floor_root ** 3 == n:
        return floor_root
    return floor_root + 1

def count_perfect_cubes(a, b):
    low = min(a, b)
    high = max(a, b)

    start = integer_cuberoot_ceil(low)
    end = integer_cuberoot_floor(high)

    return max(0, end- start + 1)

if __name__ == "__main__":
    print(count_perfect_cubes(3, 30))
    print(count_perfect_cubes(-64, 64))
    unittest.main()