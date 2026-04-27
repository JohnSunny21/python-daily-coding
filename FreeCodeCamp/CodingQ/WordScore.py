""" 


Word Score
Given a word, return its score using a standard letter-value table:

Letter	Value
A	1
B	2
...	...
Z	26
Upper and lowercase letters have the same value.
"""



import unittest


class WordScoreTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_word_score("hi"), 17)

    def test2(self):
        self.assertEqual(get_word_score("hello"), 52)

    def test3(self):
        self.assertEqual(get_word_score("hippopotamus"), 169)

    def test4(self):
        self.assertEqual(get_word_score("freeCodeCamp"), 94)


TESTCASES = [
    (("hi",), 17),
    (("hello",), 52),
    (("hippopotamus",), 169),
    (("freeCodeCamp",), 94)
]




def get_word_score(word):

    score = 0

    char_map = {chr(i) : i - ord('A') + 1 for i in range(65, 91)}

    for char in word:
        score += char_map[char.upper()]

    return score

"""
The above code can be refined

1. Efficiency :
    Building char_map inside the function every call is fine for small inputs,
    but you could build it once outside the function.

2. safety:
    if the word contains non-letters (like punctuation), your current code will throw a KeyError.
    Adding a check avoids that:

    return sum[char_map[ch.upper()] for ch in word if ch.isalpha()]

3. Alternative without dictionary:
    You can compute directly using ord():

    def get_word_score(word):
    return sum(ord(ch.upper()) - ord('A') + 1 for ch in word if ch.isalpha())
"""


def word_score(word):

    score = 0
    for ch in word.upper():
        if 'A' <= ch <= 'Z':
            score += ord(ch) - ord('A') + 1

    return score







from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": get_word_score,
         "second": word_score},
        TESTCASES,
        10000
    )

    unittest.main()