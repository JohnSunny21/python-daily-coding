""" 


Word Blender
Given two words, return a new word by combining the first half of the first word with the second half of the second word.

For odd-length words, the first half is the shorter half.
"""

import unittest

class WordBlenderTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(blend_words("turtle", "toucan"), "turcan")

    def test2(self):
        self.assertEqual(blend_words("chipmunk", "flamingo"), "chipingo")

    def test3(self):
        self.assertEqual(blend_words("falcon", "pelican"), "falican")

    def test4(self):
        self.assertEqual(blend_words("hyena", "iguana"), "hyana")

    def test5(self):
        self.assertEqual(blend_words("scorpion", "gorilla"), "scorilla")

    def test6(self):
        self.assertEqual(blend_words("platypus", "wolverine"), "platerine")


TESTCASES = [
    (("turtle", "toucan",), "turcan"),
    (("chipmunk", "flamingo",), "chipingo"),
    (("falcon", "pelican",), "falican"),
    (("hyena", "iguana",), "hyana"),
    (("scorpion", "gorilla",), "scorilla"),
    (("platypus", "wolverine",), "platerine")
]


def blend_words(word1, word2):

    mid1 = len(word1) // 2
    mid2 = len(word2) // 2

    result = word1[:mid1] + word2[mid2:]

    return result



from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": blend_words}, TESTCASES, 1000)
    unittest.main()