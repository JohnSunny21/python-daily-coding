"""  
vOwElcAsE
Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

Vowels are "a", "e", "i", "o", and "u" in any case.
Non-alphabetical characters should remain unchanged.
"""

import unittest

class vowelcaseTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(vowel_case("vowelcase"), "vOwElcAsE")

    def test2(self):
        self.assertEqual(vowel_case("coding is fun"), "cOdIng Is fUn")

    def test3(self):
        self.assertEqual(vowel_case("HELLO, world!"), "hEllO, wOrld!")

    def test4(self):
        self.assertEqual(vowel_case("git cherry-pick"), "gIt chErry-pIck")

    def test5(self):
        self.assertEqual(vowel_case("HEAD~1"), "hEAd~1")


def vowel_case(s):

    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels:
            result += char.upper()
        else:
            if char.isalpha():
                result += char.lower()
            else:
                result += char


    return result


""" 

The above solution is correcct and nicely structures it does exactly what the problem asks.


but we can make some refinments as well.

=> Efficiency: String concatenation (result += ...) in a loop is less efficient in Python because strings are immutable. A common 
pattern is to collect pieces in a list and ".join() at the end:
=> The below soltuion is functionally identical, but faster for long strings.
=> Simplification: You could avoid storing both uppercase and lowercase vowels by just checking char.lower()
The above solution is correct but the only improvement is performance (using a list instead of repeated string concatenation) and possibly simplifying the vowel check.
Otherwise, it's spot-on.
"""

def vowel_case(s: str) -> str:
    vowels = "aeiou"
    result = []
    for ch in s:
        if ch.isalpha():
            if ch.lower() in vowels:
                result.append(ch.upper())
            else:
                result.append(ch.lower())
        else:
            result.append(ch)

    return "".join(result)
            
"""
=> ch.isalpha() in Python ensures we only transform letters.
=> in Javascript, /[a-zA-Z]/.test(ch) checks if the character is alphabetic.
=> Non-alphabetic characters (digits, punctuation, spaces) remain unchanges.
=> The tranformation is consistent regardless of the original case.
"""

def vowel_case_one_liner(s):
    vowels = "aeiou"
    return "".join(
        char.upper() if char.lower() in vowels else char.lower() if char.isalpha() else char
        for char in s
    )

import re

def vowel_case_regex(s: str) -> str:

    def replacer(match):
        ch = match.group(0)
        return ch.upper() if ch.lower() in "aeiou" else ch.lower()
    return re.sub(r"[A-Za-z]", replacer,s)


""" 

=> re.sub(r"[A-Za-z]", replacer, s) finds all alphabetic characters.
=> The replace function: 
    -> Checks if the character is a vowel (aeiou).
    -> If yes -> uppercase
    -> If not -> lowercase
=> Non-alphabetic characters are untouched because the regex only matches [A-Za-z].

This is concise , efficient, leverages regex's ability to target only the chararcters you care about.
"""

if __name__ == "__main__":

    print(vowel_case("Where there is a will there is a way"))
    unittest.main()