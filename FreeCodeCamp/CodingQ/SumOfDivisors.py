"""  
Sum of Divisors
Given a positive integer, return the sum of all its divisors.

A divisor is any integer that divides the number evenly (the remainder is 0).
Only count each divisor once.
For example, given 6, return 12 because the divisors of 6 are 1, 2, 3, and 6, and the sum of those is 12.

"""

import unittest

class SumOfDivisorsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(sumDivisors(6), 12)

    def test2(self):
        self.assertEqual(sumDivisors(13), 14)

    def test3(self):
        self.assertEqual(sumDivisors(28), 56)

    def test4(self):
        self.assertEqual(sumDivisors(84), 224)

    def test5(self):
        self.assertEqual(sumDivisors(549), 806)

    def test6(self):
        self.assertEqual(sumDivisors(9348), 23520)



def sumDivisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

import math
def sumDivisors_optimized(n):
    total = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:     # avoid double-counting square roots
                total += n // i
    return total 


"""  

When finding divisors of a number n, they always come in pairs:
    => if i divides n, then n / i is also a divisor.
    => Example: for n = 36:
        -> i = 2 -> divisor pair (2, 18)
        -> i = 3 -> divisor pair (3, 12)
        -> i = 6 -> divisor pair (6, 6) (special case)

    => So instead of looping all the way up to n, you only need to loop up to sqrt(n):
        -> Because beyond sqrt(n), divisors are just the "other half" of the pairs you already found.
        -> This reduces complexity from O(n) to O(√n), which is much faster for large numbers.

=> Brute force: loop from 1 to n.
=> Optimized: loop to sqrt(n) and add divisor pairs.
=> Both approaches give the correct sum, but the optimized one is much faster for large numbers.
"""



if __name__ == "__main__":
    print(sumDivisors(15))
    unittest.main()
