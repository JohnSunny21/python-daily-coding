"""


Permutation Count
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".
"""

from itertools import permutations
import unittest

class PermutationCount(unittest.TestCase):

    def test1(self):
        self.assertEqual(count_permutations("abb"),3)

    def test2(self):
        self.assertEqual(count_permutations("abc"),6)
    
    def test3(self):
        self.assertEqual(count_permutations("racecar"), 630)

    def test4(self):
        self.assertEqual(count_permutations("freecodecamp"),39916800)


def count_permutations_for_small(s):

    perm = permutations(s)
    lis = list(perm)
    
    """
    This solution generates all the permutations good for small inputs but not memory efficient
    for large inputs and the memory exceeds
    """
    seen = set(lis)
    # print(seen)
    return len(seen)

from math import factorial
from collections import Counter
def count_permutations(s):
    """
    Core idea
    => For a string of length n, the total number of permutations is n!.
    => If the characters repeat, we must divide by the factorial of each character's
    frequency to avoid counting duplicated.

    distinct permutatoins = n! / f1!. f2!....fn!

    where n= total characters
          fi = frequency of each distinct character

        ==> n = 3 -> 3! = 6
        Frequencies:        a:1, b:2
        Denominator =  1!.2! = 2
        Distinct permutations = 6/2 = 3
        Permutations: "abb", "bab", "bba"


    Key takeaway:
    The formula n!/pi*fi! is the most efficient way to count distinct permutations without generating them all

    """

    n = len(s)
    freq = Counter(s)
    denom = 1
    for count in freq.values():
        denom *= factorial(count)

    return factorial(n) // denom

if __name__ == "__main__":
    print(count_permutations("abb"))
    unittest.main()