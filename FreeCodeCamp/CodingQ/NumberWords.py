""" 


Number Words
Given an integer from 0 to 99, return its English word representation.

0 returns "zero".
Numbers 1-19 have unique names ("one", "two", ..., "ten", "eleven", ..., "eighteen", "nineteen").
Multiples of 10 from 20-90 have their own names ("twenty", "thirty", ..., "eighty", "ninety").
Numbers 21-99 that are not multiples of 10 are written as two words joined by a hyphen. For example "forty-two" and "fifty-three".
"""


import unittest


class NumberWordsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_number_words(0), "zero")

    def test2(self):
        self.assertEqual(get_number_words(10), "ten")

    def test3(self):
        self.assertEqual(get_number_words(19), "nineteen")

    def test4(self):
        self.assertEqual(get_number_words(30), "thirty")

    def test5(self):
        self.assertEqual(get_number_words(53), "fifty-three")

    def test6(self):
        self.assertEqual(get_number_words(7), "seven")

    def test7(self):
        self.assertEqual(get_number_words(12), "twelve")

    def test8(self):
        self.assertEqual(get_number_words(60), "sixty")

    def test9(self):
        self.assertEqual(get_number_words(67), "sixty-seven")

    def test10(self):
        self.assertEqual(get_number_words(98), "ninety-eight")


TESTCASES = [
    ((0,), "zero"),
    ((10,), "ten"),
    ((19,), "nineteen"),
    ((30,), "thirty"),
    ((53,), "fifty-three"),
    ((7,), "seven"),
    ((12,), "twelve"),
    ((60,), "sixty"),
    ((67,), "sixty-seven"),
    ((98,), "ninety-eight")
]





def get_number_words(n):

    ones = ["zero","one","two","three","four","five","six","seven","eight","nine",
            "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
            "seventeen","eighteen","nineteen"]
    
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n < 100:
        if n % 10 == 0:
            return tens[n // 10]
        else:
            return tens[n // 10] + "-" + ones[n % 10]
    
    else:
        raise ValueError("Number out of range (0 - 99)")
    




from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark(
        {"first": get_number_words},
        TESTCASES,
        10000
    )

    unittest.main()