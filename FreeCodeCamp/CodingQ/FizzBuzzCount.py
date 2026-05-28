""" 

FizzBuzz Count
Given a start and end number, count the number of fizz and buzz appearances in the range (inclusive).

Numbers divisible by 3 count as a fizz.
Numbers divisible by 5 count as a buzz.
Numbers divisible by both 3 and 5 count as both a fizz and a buzz.
Return an object or dictionary with the counts in the format: { fizz, buzz }.
"""



import unittest


class FizzBuzzCountTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(fizz_buzz_count(1, 11), {"fizz": 3, "buzz": 2})

    def test2(self):
        self.assertEqual(fizz_buzz_count(14, 41), {"fizz": 9, "buzz": 6})

    def test3(self):
        self.assertEqual(fizz_buzz_count(24, 100), {"fizz": 26, "buzz": 16})

    def test4(self):
        self.assertEqual(fizz_buzz_count(-635, -14), {"fizz": 207, "buzz": 125})

    def test5(self):
        self.assertEqual(fizz_buzz_count(-5432, 6789), {"fizz": 4074, "buzz": 2444})


TESTCASES = [
    ((1, 11,), {"fizz": 3, "buzz": 2}),
    ((14, 41,), {"fizz": 9, "buzz": 6}),
    ((24, 100,), {"fizz": 26, "buzz": 16}),
    ((-635, -14,), {"fizz": 207, "buzz": 125}),
    ((-5432, 6789,), {"fizz": 4074, "buzz": 2444})
]






def fizz_buzz_count(start, end):

    fizz = 0
    buzz = 0

    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz += 1
            buzz += 1
        elif i % 3 == 0:
            fizz += 1
        elif i % 5 == 0:
            buzz += 1

    return {"fizz": fizz, "buzz": buzz}


def fizzbuzz_count(start, end):

    result = {"fizz": 0, "buzz": 0}

    for num in range(start, end + 1):

        if num % 3 == 0:
            result["fizz"] += 1
        if num % 5 == 0:
            result["buzz"] += 1

    return result






from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark(
        {"first": fizz_buzz_count,
         "second": fizzbuzz_count},
        TESTCASES,
        10000
    )

    unittest.main()