""" 

Palindrome Characters
Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

A palindrome is a string that is the same forward and backward.
If it's not a palindrome, return "none".
"""

import unittest


class PalindromeCharactersTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(palindrome_locator("racecar"), "e")      

    def test2(self):
        self.assertEqual(palindrome_locator("level"), "v")        

    def test3(self):
        self.assertEqual(palindrome_locator("freecodecamp"), "none")

    def test4(self):
        self.assertEqual(palindrome_locator("noon"), "oo")        

    def test5(self):
        self.assertEqual(palindrome_locator("11100111"), "00")



def palindrome_locator(s):

    if s != s[::-1]:
        return "none"
    
    mid = len(s) // 2

    if len(s) % 2 == 0:
        return s[mid-1: mid+1]
    else:
        return s[mid]
    




from utils.benchmark import benchmark

if __name__ == "__main__":
    TESTCASES = [
    (("racecar",), "e"),
    (("level",), "v"),
    (("freecodecamp",), "none"),
    (("noon",), "oo"),
    (("11100111",), "00")
]
    scores = benchmark(
        {"first": palindrome_locator},
        TESTCASES,
        10000
    )
    unittest.main()