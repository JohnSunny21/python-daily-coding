"""

FizzBuzz Validator
Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

In a valid FizzBuzz sequence:

Multiples of 3 are replaced with "Fizz".
Multiples of 5 are replaced with "Buzz".
Multiples of both 3 and 5 are replaced with "FizzBuzz".
All other numbers remain as integers.
"""

import unittest


class FizzBuzzValidatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]), True)

    def test2(self):
        self.assertEqual(is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]), True)

    def test3(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, 5]), False)

    def test4(self):
        self.assertEqual(is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]), True)

    def test5(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", "Buzz", 5]), False)

    def test6(self):
        self.assertEqual(is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]), False)

    def test7(self):
        self.assertEqual(is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]), True)






def is_fizz_buzz_first(arr):
    
    start = None
    for x in arr:
        if isinstance(x, int):
            start = x
            break

    if start is None:
        return False
    
    for i, val in enumerate(arr):
        num = start + i
        expected = None

        if num % 3 == 0 and num % 5 == 0:
            expected = "FizzBuzz"
        elif num % 3 == 0:
            expected = "Fizz"
        elif num % 5 == 0:
            expected = "Buzz"
        else:
            expected = num

        if val != expected:
            return False
        
    return True

"""
is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]) should return True

is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]) should return True.
These two test cases are failing but the above solution .

The earlier solution assumed the first element was always a number, but in your failing cases the sequence start
with "Fizz", "Buzz", or "FizzBuzz". We need to handle that by deriving the starting integer from the position of the first numeric element 
and then back-calculating what the earlier string(s) should have been.
"""





def is_fizz_buzz(arr):

    first_num_index = None
    first_num_value = None

    for i, val in enumerate(arr):
        if isinstance(val, int):
            first_num_index = i
            first_num_value = val
            break

    if first_num_index is None:
        return False
    
    start = first_num_value - first_num_index

    for i , value in enumerate(arr):
        num = start + i
        if num % 3 == 0 and num % 5 == 0:
            expected = "FizzBuzz"
        elif num % 3 == 0:
            expected = "Fizz"
        elif num % 5 == 0:
            expected = "Buzz"
        else:
            expected = num
        

        if value != expected:
            return False
        

    return True








from utils.benchmark import benchmark

if __name__ == "__main__":

    TESTCASES = [
    (([1, 2, "Fizz", 4, "Buzz"],), True),
    (([13, 14, "FizzBuzz", 16, 17],), True),
    (([1, 2, "Fizz", 4, 5],), False),
    ((["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"],), True),
    (([1, 2, "Fizz", "Buzz", 5],), False),
    (([97, 98, "Buzz", "Fizz", 101, "Fizz", 103],), False),
    ((["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"],), True)
]
    scores = benchmark(
        {"first": is_fizz_buzz},
        TESTCASES,
        10000
    )


    unittest.main()