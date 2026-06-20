""" 


Prime Factorization
Given an integer greater than 1, return its prime factorization as an array of numbers in ascending order.

A prime factorization is the set of prime numbers that multiply together to produce the given integer. Each number has exactly one set. For example, the prime factorization of 20 is [2, 2, 5] because 2 * 2 * 5 = 20.

If the given integer is itself prime, return it in a single-element array.
"""


import unittest


class PrimeFactorizationTest(unittest.TestCase):




    def test1(self):
        self.assertEqual(prime_factorization(20), [2, 2, 5])

    def test2(self):
        self.assertEqual(prime_factorization(17), [17])

    def test3(self):
        self.assertEqual(prime_factorization(15), [3, 5])

    def test4(self):
        self.assertEqual(prime_factorization(35), [5, 7])

    def test5(self):
        self.assertEqual(prime_factorization(999), [3, 3, 3, 37])

    def test6(self):
        self.assertEqual(prime_factorization(360), [2, 2, 2, 3, 3, 5])

    def test7(self):
        self.assertEqual(prime_factorization(510510), [2, 3, 5, 7, 11, 13, 17])


TESTCASES = [
    ((20,), [2, 2, 5]),
    ((17,), [17]),
    ((15,), [3, 5]),
    ((35,), [5, 7]),
    ((999,), [3, 3, 3, 37]),
    ((360,), [2, 2, 2, 3, 3, 5]),
    ((510510,), [2, 3, 5, 7, 11, 13, 17])
]



def prime_factorization(n):
    factors = []

    divisor = 2

    while n > 1:
        while n % divisor == 0:

            factors.append(divisor)
            n //= divisor

        divisor += 1

    return factors

import math

def prime_factorization2(n):

    factors = []

    # Handle factor 2 separately    
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check odd divisors up to sqrt(n)

    divisor = 3
    while divisor <= math.isqrt(n): # integer square root
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2 # skipping even numbers

    # If n is still > 1, it's prime
    if n > 1:
        factors.append(n)

    return factors


""" 
=> This is faster because After removing all factors of 2, only odd numbers need checking.
=> You only need to check divisors up to root n.
=> If n is still > 1 after the loop, it must be prime.

This reduces the number of divisions dramatically for large numbers.

"""




from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark(
        {"first": prime_factorization,
         "second": prime_factorization2}, 
        TESTCASES,
        10000
    )

    unittest.main()