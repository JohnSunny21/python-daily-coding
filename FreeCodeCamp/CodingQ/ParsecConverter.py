""" 

Parsec Converter
In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its equivalent in time or distance.

If the given integer is odd, it represents time. If it's even, it represents distance.
Use these conversion rates:

Parsecs	Time/Distance
1	2 hours
2	6 light years
Return the converted value as an integer.
"""


import unittest


class ParsecConverterTest(unittest.TestCase):
    

    def test1(self):
        self.assertEqual(convert_parsecs(1), 2)

    def test2(self):
        self.assertEqual(convert_parsecs(2), 6)

    def test3(self):
        self.assertEqual(convert_parsecs(31), 62)

    def test4(self):
        self.assertEqual(convert_parsecs(88), 264)

    def test5(self):
        self.assertEqual(convert_parsecs(17), 34)

    def test6(self):
        self.assertEqual(convert_parsecs(14), 42)


TESTCASES = [
    ((1,), 2),
    ((2,), 6),
    ((31,), 62),
    ((88,), 264),
    ((17,), 34),
    ((14,), 42)
]



def convert_parsecs(parsecs):


    if parsecs % 2 == 1:
        return  parsecs * 2
    else:
        return (parsecs // 2) * 6
    

"""
=> The use of why (n // 2) * 6 is
    The problem statement defines the conversion rated like this:
        -> 1 parsec (odd) -> 2 hours
        -> 2 parsecs (even) -> 6 light years

Notice that the distance converstion is given per 2 parsecs, not per 1 parsec.
So the formula is:
    light years = n // 2 * 6



That's why we use (n // 2) *  6 in code - it groups the parsecs into pairs, then multiplies by 6.
"""



from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": convert_parsecs},
        TESTCASES,
        10000
    )

    unittest.main()