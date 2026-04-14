"""
Last Letter
Given a string, return the letter from the string that appears last in the alphabet.

If two or more letters tie for the last in the alphabet, return the first one.
Ignore all non-letter characters.
"""

import unittest

class LastLetterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_last_letter("world"), "w")

    def test2(self):
        self.assertEqual(get_last_letter("Hello World"), "W")

    def test3(self):
        self.assertEqual(get_last_letter("The quick brown fox jumped over the lazy dog."), "z")

    def test4(self):
        self.assertEqual(get_last_letter("HeLl0"), "L")

    def test5(self):
        self.assertEqual(get_last_letter("!#$ er@R asd fT.,> 2t0e9"), "T")








def get_last_letter(s):

    strength = 0

    result_char = ""
    order = 0
    for char in s:
        if char.isupper():
            order = ord(char) - ord('A') + 1
        elif char.islower():
            order = ord(char) - ord('a') + 1

        if order > strength:
            strength = order
            result_char = char

    return result_char

def get_last_letter_refined(s):

    strength = 0
    result_char = ""

    for char in s:
        if char.isalpha():

            order = ord(char.lower()) - ord('a') + 1

            if order > strength:
                strength = order
                result_char = char

    return result_char



def get_last_letter_third(s: str) -> str:

    letters = [ch for ch in s if ch.isalpha()]

    if not letters:
        return ""
    

    max_letter = letters[0]
    for ch in letters[1:]:
        # Compare letters in upper case so case doesn't matter.
        if ch.upper() > max_letter.upper():
            max_letter = ch

    return max_letter










from utils.benchmark import benchmark

if __name__ == "__main__":

    # print(get_last_letter("world"))
    print(get_last_letter("!#$ er@R asd fT.,> 2t0e9"))
    TESTCASES = [
    (("world",), "w"),
    (("Hello World",), "W"),
    (("The quick brown fox jumped over the lazy dog.",), "z"),
    (("HeLl0",), "L"),
    (("!#$ er@R asd fT.,> 2t0e9",), "T")
]
    scores = benchmark(
        {
            "first": get_last_letter,
            "second": get_last_letter_refined,
            "third": get_last_letter_third
        },
        TESTCASES,
        10000
    )

    unittest.main()