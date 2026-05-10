""" 

ISBN-13 Validator
Given a string, determine if it is a valid ISBN-13 number.

A valid ISBN-13:

Contains only digits and hyphens
Has exactly 13 digits after removing hyphens
Passes the following check:
Multiply each digit by 1 or 3, alternating (multiply the first digit by 1, the second by 3, the third by 1, and so on).
The sum of the results must be divisible by 10.
"""


import unittest


class ISBN13ValidatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_valid_isbn_13("9780306406157"), True)

    def test2(self):
        self.assertEqual(is_valid_isbn_13("97803064061570"), False)

    def test3(self):
        self.assertEqual(is_valid_isbn_13("978-0-13-595705-9"), True)

    def test4(self):
        self.assertEqual(is_valid_isbn_13("978-030-64061A-4"), False)

    def test5(self):
        self.assertEqual(is_valid_isbn_13("9-7-8-0-1-3-4-7-5-7-5-9-9"), True)


TESTCASES = [
    (("9780306406157",), True),
    (("97803064061570",), False),
    (("978-0-13-595705-9",), True),
    (("978-030-64061A-4",), False),
    (("9-7-8-0-1-3-4-7-5-7-5-9-9",), True)
]





def is_valid_isbn_13(s):

    digits = s.replace("-", "")

    if not digits.isdigit():
        return False
    
    if len(digits) != 13:
        return False
    
    summ = 0

    for i, num in enumerate(digits, start=1):
        if i % 2 == 0:
            summ += int(num) * 3
        else:
            summ += int(num) * 1

    return summ % 10 == 0




from utils.benchmark import benchmark


if __name__ == "__main__":
    scores = benchmark(
        {"first": is_valid_isbn_13},
        TESTCASES,
        10000
    )

    unittest.main()