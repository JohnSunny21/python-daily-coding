""" 

Character Frequency
Given a string, return an object (JavaScript) or dictionary (Python) mapping each character to the number of times it appears.
"""


import unittest


class CharacterFrequencyTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_frequency("test"), {"t": 2, "e": 1, "s": 1})

    def test2(self):
        self.assertEqual(get_frequency("mississippi"), {"m": 1, "i": 4, "s": 4, "p": 2})

    def test3(self):
        self.assertEqual(get_frequency("hello world"), {"h": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1})

    def test4(self):
        self.assertEqual(get_frequency("She sells seashells by the seashore."), {"S": 1, "h": 4, "e": 7, " ": 5, "s": 7, "l": 4, "a": 2, "b": 1, "y": 1, "t": 1, "o": 1, "r": 1, ".": 1})

    def test5(self):
        self.assertEqual(get_frequency("The quick brown fox jumps over the lazy dog."), {"T": 1, "h": 2, "e": 3, " ": 8, "q": 1, "u": 2, "i": 1, "c": 1, "k": 1, "b": 1, "r": 2, "o": 4, "w": 1, "n": 1, "f": 1, "x": 1, "j": 1, "m": 1, "p": 1, "s": 1, "v": 1, "t": 1, "l": 1, "a": 1, "z": 1, "y": 1, "d": 1, "g": 1, ".": 1})


TESTCASES = [
    (("test",), {"t": 2, "e": 1, "s": 1}),
    (("mississippi",), {"m": 1, "i": 4, "s": 4, "p": 2}),
    (("hello world",), {"h": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1}),
    (("She sells seashells by the seashore.",), {"S": 1, "h": 4, "e": 7, " ": 5, "s": 7, "l": 4, "a": 2, "b": 1, "y": 1, "t": 1, "o": 1, "r": 1, ".": 1}),
    (("The quick brown fox jumps over the lazy dog.",), {"T": 1, "h": 2, "e": 3, " ": 8, "q": 1, "u": 2, "i": 1, "c": 1, "k": 1, "b": 1, "r": 2, "o": 4, "w": 1, "n": 1, "f": 1, "x": 1, "j": 1, "m": 1, "p": 1, "s": 1, "v": 1, "t": 1, "l": 1, "a": 1, "z": 1, "y": 1, "d": 1, "g": 1, ".": 1})
]






def get_frequency(s):

    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq



from collections import Counter
def get_frequency_second(s):

    return Counter(s)





from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark(
        {"first": get_frequency,
         "second": get_frequency_second},
         TESTCASES,
         10000
    )

    unittest.main()