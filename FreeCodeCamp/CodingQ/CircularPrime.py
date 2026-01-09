"""  

Circular Prime
Given an integer, determine if it is a circular prime.

A circular prime is an integer where all rotations of its digits are themselves prime.

For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.
"""

import unittest

class CircularPrimeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_circular_prime(197), True)

    def test2(self):
        self.assertEqual(is_circular_prime(23), False)

    def test3(self):
        self.assertEqual(is_circular_prime(13), True)

    def test4(self):
        self.assertEqual(is_circular_prime(89), False)

    def test5(self):
        self.assertEqual(is_circular_prime(1193), True)




def is_circular_prime(n):
    string_n = str(n)
    def is_prime(n):

        for i in range(2, n//2):
            if n % i == 0:
                return False
            
        return True
    
    num = ""
    real = list(str(n))
    numbers = []


    while num != string_n:
        num = ""
        real.append(real.pop(0))
        num += ''.join(real)
        numbers.append(num)


    # print(numbers)

    if all(is_prime(int(num)) for num in numbers):
        return True
    else:
        return False
    
""" 
Issues in your solution

1. Prime check inefficiency / correctness

    for i in range(2, n//2):
        if n % i == 0:
        return False
    return True

    -> This loop goes up to n//2, which is much more work than necessary.
    -> You only need to check divisors up to root n.
    -> Also, it incorrectly returns True for n = 1 (since the loop never runs). But 1 is not prime.

    we fixed that in the below solution.

2. Rotation Logic
    num = ""
    real = list(str(n))
    numbers = []
    while num != string_n:
        num = ""
        real.append(real.pop(0))
        num += "".join(real)
        numbers.append(num)


        -> This loop rotated digits until it cycles back to the original string.
        -> it works, but its a bit clunky.
        -> Also, it skips the original number because the num starts empty, so the first rotation happens before
           adding the original.
        -> Example: for 197, you'll collect 971, 719, 197 - but the original 197 only appears at the end, not at the start.
    
    The cleaner approach is below

3. Final check

if alL(is_prime(int(num)) for num in numbers):
    return True
else:
    return False

    -> This is fine, but you don't need th if/else.
    -> all(..) already returns True or False
"""
    


def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0 and num != 2:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
        
    return True

def rotations(n):
    s = str(n)

    return [int(s[i:] + s[:i]) for i in range(len(s))]

def is_circular_prime(n):
    return all(is_prime(rot) for rot in rotations(n))
    

""" 
=> Rotations: For 197, rotations are 197, 971, 719.
=> Prime check: Efficient up to root of n.
=> Edge cases:
    -> single-digit primes (2, 3, 5, 7) -> circular primes.
    -> Numbers with even digits or 5 (except single-digit primes) -> usually fail, because one rotation will end in an even number of 5.
"""
if __name__ == "__main__":
    print(is_circular_prime(512))
    unittest.main()