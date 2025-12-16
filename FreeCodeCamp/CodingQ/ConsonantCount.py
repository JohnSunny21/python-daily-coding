"""  
Consonant Count
Given a string and a target number, determine whether the string contains exactly the target number of consonants.

Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
Ignore digits, punctuation, spaces, and other non-letter characters when counting.
"""

import unittest

class ConsonantCountTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(has_consonant_count("helloworld", 7), True)

    def test2(self):
        self.assertEqual(has_consonant_count("eieio", 5), False)

    def test3(self):
        self.assertEqual(has_consonant_count("freeCodeCamp Rocks!", 11), True)

    def test4(self):
        self.assertEqual(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24), False)

    def test5(self):
        self.assertEqual(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23), True)



def has_consonant_count(text, target):

    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char.lower() not in "aeiou":
                consonant_count += 1
    return consonant_count == target


def has_consonant_count(text, target):

    vowels = set("aeiouAEIOU")
    consonant_count = 0

    for char in text:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
        

    return consonant_count == target



if __name__ == "__main__":
    print(has_consonant_count("Hi hello world ",8))
    unittest.main()
