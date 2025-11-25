"""
FizzBuzz
Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

3 with "Fizz".
5 with "Buzz".
3 and 5 with "FizzBuzz".
"""

import unittest


class FizzBuzzTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(fizz_buzz(2),[1, 2])

    def test2(self):
        self.assertEqual(fizz_buzz(4), [1, 2, "Fizz", 4])

    def test3(self):
        self.assertEqual(fizz_buzz(8), [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8])

    def test4(self):
        self.assertEqual(fizz_buzz(20), [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"])

    def test5(self):
        self.assertEqual(fizz_buzz(50), [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"])



def fizz_buzz(n):

    result = []

    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            result.append("FizzBuzz")
        elif i%3 == 0:
            result.append("Fizz")
        elif i%5 == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result


def fizz_buzz_optimized(n):

    return ["FizzBuzz" if i%3 == 0 and i%5 == 0 else "Fizz" if i%3 == 0 else "Buzz" if i%5 == 0 else i for i in range(1, n+1)]





if __name__ == "__main__":
    print(fizz_buzz(15))
    print(fizz_buzz_optimized(15))
    unittest.main()