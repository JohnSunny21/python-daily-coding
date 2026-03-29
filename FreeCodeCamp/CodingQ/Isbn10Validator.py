""" 
ISBN-10 Validator
Given a string, determine if it's a valid ISBN-10.

An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):

The first 9 characters must be digits, and
The final character may be a digit or the letter "X", which represents the number 10.
To validate it:

Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
Add all the results together.
If the total is divisible by 11, it's valid.
"""

import unittest


class Isbn10ValidatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_valid_isbn10("0-306-40615-2"), True)

    def test2(self):
        self.assertEqual(is_valid_isbn10("0-306-40615-1"), False)

    def test3(self):
        self.assertEqual(is_valid_isbn10("0-8044-2957-X"), True)

    def test4(self):
        self.assertEqual(is_valid_isbn10("X-306-40615-2"), False)

    def test5(self):
        self.assertEqual(is_valid_isbn10("0-6822-2589-4"), True)






def is_valid_isbn10(s):

    s = s.replace("-","")

    if len(s) != 10:
        return False
    
    digits = s[:-1]
    final_char = s[-1]

    if not digits.isdigit():
        return False
    
    if not final_char.isdigit() and final_char != "X":
        return False
    
    result = 0

    for index, value  in enumerate(digits, start =1):
        result += index * int(value)


    if final_char == "X":
        result += 10 * 10
    else:
        result += 10 * int(final_char)


    return result % 11 == 0


def is_valid_isbn10_second(isbn: str) -> bool:

    isbn = isbn.replace("-","")

    if len(isbn) != 10:
        return False
    
    if not isbn[:9].isdigit():
        return False
    
    if not(isbn[9].isdigit() or isbn[9] == "X"):
        return False
    

    total = 0
    for i in range(9):
        total += (i + 1) * int(isbn[i])

    if isbn[9] == "X":
        total += 10 * 10
    else:
        total += 10 * int(isbn[9])

    return total % 11 == 0

from utils.benchmark import benchmark
if __name__ == "__main__":


    TESTCASES = [
    (("0-306-40615-2",), True),
    (("0-306-40615-1",), False),
    (("0-8044-2957-X",), True),
    (("X-306-40615-2",), False),
    (("0-6822-2589-4",), True)
]
    scores = benchmark(
        {"first": is_valid_isbn10,
         "second": is_valid_isbn10_second},
        TESTCASES,
        10000
    )
    unittest.main()