"""  
Nth Fibonacci Number
Given an integer n, return the nth number in the fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
"""

import unittest

class NthFibonacciNumberTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(nth_fibonacci(4), 2)
    
    def test2(self):
        self.assertEqual(nth_fibonacci(10), 34)

    def test3(self):
        self.assertEqual(nth_fibonacci(15), 377)

    def test4(self):
        self.assertEqual(nth_fibonacci(40), 63245986)

    def test5(self):
        self.assertEqual(nth_fibonacci(75), 1304969544928657)


def nth_fibonacci(n):

    fibo_series = [0, 1]

    for i in range(2, n+1):
        fibo_series.append(fibo_series[-1] + fibo_series[-2])

    return fibo_series[n-1]

def nth_fibonacci(n):

    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1

    for _ in range(2, n+1):
        a, b = b , a + b
    
    return a

""" 
=> This is an iterative approach (efficient O(n) time, O(1) space)
=> Recursive approach solutions are simpler but inefficient forlarge n (exponential time).
=> For very large n, you'd use matrix exponentiation or fast doubling methods(O(log n)).
"""



if __name__ == "__main__":
    print(nth_fibonacci(10))

    # print(nth_fibonacci_test(10))
    unittest.main()