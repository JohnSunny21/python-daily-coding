"""
Nth Prime
A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.
"""

import unittest

class NthPrimeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(nth_prime(5),11)
    
    def test2(self):
        self.assertEqual(nth_prime(10),29)
    
    def test3(self):
        self.assertEqual(nth_prime(16),53)
    
    def test4(self):
        self.assertEqual(nth_prime(99),523)

    def test5(self):
        self.assertEqual(nth_prime(1000),7919)






def nth_prime(n):
    """
    First need to find out the prime numbers upto the given "n" 
    But NOTE the given "n" is not the range for the loop to run .
    This problem can be solved by finding all the primes upto the specified "n" numbers.

    and then the last numbers which the upto the specified 'nth' index can be returned.

    """
    primes = [2]

    def is_prime(num):
        if num < 2:
            return False
        
        for i in range(2, int(num**0.5) + 1):
            if num%i == 0:
                return False
        return True
    

    candidate = 3
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 2 # Skipping the even numbers because they are not prime.

    # print(primes)
    return primes[-1]


def nth_prime_optimized(n):
    """
    In this solution eliminated the use of array or list which is a space complexity of O(n) 
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num%i == 0:
                return False
        return True
    

    count = 0
    candidate = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
            
        candidate += 1




if __name__ == "__main__":
    print(nth_prime(10))
    unittest.main()