"""

BuzzFizz
Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

Numbers that are multiples of 3 are replaced with "Fizz"
Numbers that are multiples of 5 are replaced with "Buzz"
Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
All other numbers remain as integers in ascending order, starting from 1.
The array must start at 1 and have no missing or extra elements.
"""

import unittest

class BuzzFizzTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4]),True)

    def test2(self):
        self.assertEqual(is_fizz_buzz([1, 2, 3, 4]),False)
    
    def test3(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]), False)

    def test4(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]),False)

    def test5(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]),False)

    def test6(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]), False)

    def test7(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]),True)




def is_fizz_buzz(sequence):
    sequence.insert(0, 0)
    """
    Areas to refine
    1). sequence.insert(0, 0) side effect
    => This is mutating the input list by inserting a dummy 0 at the start
    => This works for indexing convenience, but it changes the caller's list permanently.
    => Better: avoid modifying the input and just adjust your loop.

    for index, value in enumerate(sequence, start = 1):
    

    2). Integer vs string comparison
        - we're checking elif index != sequence[index].
        - This assumes non-FizzBuzz entries are integers. That’s fine, but if someone passes "1" instead of 1, it fails.
        - we might want to enforce type consistency or document that only integers are valid.
        - Readability
        - The nested if checks are correct but verbose. we can simplify with a helper function that generates the expected value and compare directly.


    """
    

    for index in range(1, len(sequence)):

        if index%3 == 0 and index%5 ==0:
            if sequence[index] != "FizzBuzz":
                return False
        elif index%3 == 0:
            if sequence[index] != "Fizz":
                return False
        elif index%5 == 0:
            if sequence[index] != "Buzz":
                return False
        elif index != sequence[index]:
            return False
   
    return True


def is_fizz_buzz(sequence):
    for index, value in enumerate(sequence, start=1):
        if index % 3 == 0 and index % 5 == 0:
            expected = "FizzBuzz"
        elif index % 3 == 0:
            expected = "Fizz"
        elif index % 5 == 0:
            expected = "Buzz"
        else:
            expected = index

        if value != expected:
            return False
    return True



if __name__ == "__main__":
    print(is_fizz_buzz([1, 2, "Fizz", 4]))
    unittest.main()