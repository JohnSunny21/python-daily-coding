""" 

Odd Words
Given a string of words, return only the words with an odd number of letters.

Words in the given string will be separated by a single space.
Return the words separated by a single space.

"""


import unittest

class OddWordsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_odd_words("This is a super good test"), "a super")

    def test2(self):
        self.assertEqual(get_odd_words("one two three four"), "one two three")

    def test3(self):
        self.assertEqual(get_odd_words("banana split sundae with rainbow sprinkles on top"), "split rainbow sprinkles top")

    def test4(self):
        self.assertEqual(get_odd_words("The quick brown fox jumped over the lazy river"), "The quick brown fox the river")


TESTCASES = [
    (("This is a super good test",), "a super"),
    (("one two three four",), "one two three"),
    (("banana split sundae with rainbow sprinkles on top",), "split rainbow sprinkles top"),
    (("The quick brown fox jumped over the lazy river",), "The quick brown fox the river")
]





def get_odd_words(s):

    result = []

    for word in s.split(" "):
        if len(word) % 2 != 0:
            result.append(word)

    return " ".join(result)


def get_odd_words_pythonic(s):

    return " ".join([word for word in s.split(" ") if len(word) % 2 != 0])






from utils.benchmark import benchmark

if __name__ == "__main__":
    

    scores = benchmark(
        {"first": get_odd_words,
         "second": get_odd_words_pythonic}, 
         TESTCASES,
         10000
    )

    unittest.main()