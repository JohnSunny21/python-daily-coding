""" 

No Consecutive Repeats
Given a string, determine if it has no repeating characters.

A string has no repeats if it does not have the same character two or more times in a row.
"""

import unittest


class NoConsecutiveRepeatsTest(unittest.TestCase):
    
    
    def test1(self):
        self.assertEqual(has_no_repeats("hi world"), True)

    def test2(self):
        self.assertEqual(has_no_repeats("hello world"), False)

    def test3(self):
        self.assertEqual(has_no_repeats("abcdefghijklmnopqrstuvwxyz"), True)

    def test4(self):
        self.assertEqual(has_no_repeats("freeCodeCamp"), False)

    def test5(self):
        self.assertEqual(has_no_repeats("The quick brown fox jumped over the lazy dog."), True)

    def test6(self):
        self.assertEqual(has_no_repeats("Mississippi"), False)


def has_no_repeats(s):

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
        
    return True


from utils.benchmark import benchmark
if __name__ == "__main__":

    TESTCASES = [
    (("hi world",), True),
    (("hello world",), False),
    (("abcdefghijklmnopqrstuvwxyz",), True),
    (("freeCodeCamp",), False),
    (("The quick brown fox jumped over the lazy dog.",), True),
    (("Mississippi",), False)
]
    
    scores = benchmark(
        {"optimal": has_no_repeats},
        TESTCASES,
        10000
    )
    print(scores)
    unittest.main()