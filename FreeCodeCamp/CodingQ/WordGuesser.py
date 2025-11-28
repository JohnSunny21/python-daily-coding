"""
Word Guesser
Given two strings of the same length, a secret word and a guess, compare the guess to the secret word using the following rules:

The secret word and guess will only consist of uppercase letters ("A" to "Z");
For each letter in the guess, replace it with a number according to how it matches the secret word:
"2" if the letter is in the secret word and in the correct position.
"1" if the letter is in the secret word but in the wrong position.
"0" if the letter is not in the secret word.
Each letter in the secret word can be used at most once.
Exact matches ("2") are assigned first, then partial matches ("1") are assigned from left to right for remaining letters.
If a letter occurs multiple times in the guess, it can only match as many times as it appears in the secret word.
For example, given a secret word of "APPLE" and a guess of "POPPA", return "10201":

The first "P" is not in the correct location ("1"), the "O" isn't in the secret word ("0"), the second "P" is in the correct location ("2"), the third "P" is a zero ("0") because the two "P"'s in the secret word have been used, and the "A" is not in the correct location ("1").
"""


import unittest

class WordGuesserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(compare("APPLE","POPPA"),"10201")

    def test2(self):
        self.assertEqual(compare("REACT","TRACE"),"11221")

    def test3(self):
        self.assertEqual(compare("DEBUGS","PYTHON"),"000000")
    
    def test4(self):
        self.assertEqual(compare("JAVASCRIPT","TYPESCRIPT"),"0000222222")

    def test5(self):
        self.assertEqual(compare("ORANGE","ROUNDS"),"110200")

    def test6(self):
        self.assertEqual(compare("WIRELESS","ETHERNET"),"10021000")


def compare(word, guess):
    n = len(word)
    result = ["0"] * n
    used = [False] * n

    # Step 1: Exact matches ("2")
    for i in range(n):
        if guess[i] == word[i]:
            result[i] = "2"
            used[i] = True

    
    # Step 2: Partial matches ("1")

    for i in range(n):
        if result[i] == "0":    # Not already exact

            for j in range(n):
                if not used[j] and guess[i] == word[j]:
                    result[i] = "1"
                    used[j] = True
                    break


    return "".join(result)


if __name__ == "__main__":
    print(compare("APPLE","POPPA"))
    unittest.main()
