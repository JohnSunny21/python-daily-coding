"""

Vowels and Consonants
Given a string, return an array with the number of vowels and number of consonants in the string.

Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].
"""

import unittest

class VowAndConsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(count("Hello World"),[3, 7])

    def test2(self):
        self.assertEqual(count_refined("JavaScript"),[3, 7])
    
    def test3(self):
        self.assertEqual(count_refined("Python"),[1, 5])

    def test4(self):
        self.assertEqual(count_refined("freeCodeCamp"), [5, 7])
    
    def test5(self):
        self.assertEqual(count_refined("Hello, World!"), [3, 7])

    def test6(self):
        self.assertEqual(count_refined("The quick brown fox jumps over the lazy dog."), [11, 24])





def count(s):
    vowels = 0
    consonants = 0
    for char in s:
        if char.isalpha():
            if char in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    
    return [vowels, consonants]


def count_refined(s):
    vowels = set("aeiouAEIOU")
    vowel_count = consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return [vowel_count, consonant_count]



if __name__ == "__main__":
    print(count_refined("Able to run"))
    # In this second call for the first method which is not refined 
    # didn't added the check for the lower case so when the upper case vowel comes
    # It is treated as consonant as it is filtered in the else block so we need to use both uppercase and lowercase for checking.
    print(count("Able to run"))
    unittest.main()