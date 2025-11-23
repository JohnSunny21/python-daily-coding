"""
Character Count
Given a sentence string, return an array with a count of each character in alphabetical order.

Treat upper and lowercase letters as the same letter when counting.
Ignore numbers, spaces, punctuation, etc.
Return the count and letter in the format "letter count". For instance, "a 3".
All returned letters should be lowercase.
Do not return a count of letters that are not in the given string.
"""

import unittest

class CharacterCountTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(count_characters("hello world"), ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"])

    def test2(self):
        self.assertEqual(count_characters("I love coding challenges!"), ["a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3", "n 2", "o 2", "s 1", "v 1"])

    def test3(self):
        self.assertEqual(count_characters("// TODO: Complete this challenge ASAP!"), ["a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3", "m 1", "n 1", "o 3", "p 2", "s 2", "t 3"])


def count_characters(sentence):

    sentence = sentence.lower()
    seen = dict()
    res = []

    for char in sentence:
        if char.isalpha() and char not in seen:
            char_count = sentence.count(char)
            seen[char] = char_count
        

    for char, count in seen.items():
        res.append(f"{char} {count}")
        
    return sorted(res)

"""
The above code can be improved 
Areas for improvement
1. Efficiency
=>  use of sentence.count(char) inside the loop.
=> That scans the entire string for each new character => O(n^2) time complexity.
=> for long sentences, this is inefficient

1. Better: count characters in one pass.

"""

def count_characters_refined(sentence):
    sentence = sentence.lower()
    counts = Counter(c for c in sentence if c.isalpha())
    return [f"{char} {counts[char]}" for char in sorted(counts)]

'''
This refined solution 
is much cleaner 
=> This is O(n) and much cleaner
=> Sorting 
    -> sorted(res) sorts the formatted strings, not the dictionary keys directly.
    -> It works because "a 3" < "b 2", but sorting by keys before formatting is clearer.

    for char in sorted(seen):
        res.append(f"{char} {seen[char]}")

=> empty input handling
    -> The previous code returns [] for empty strings, which is fine.
    -> Just worth noting that it behaves gracefully.


This version is correct and readable
-> The main drawback is efficiency due to repeated .count() calls
-> Using Counter or a sinlge-pass dictionary update makes it more scalable.


'''


import re
from collections import Counter

def character_count(sentence):
    # Keey only letters, convert to lowercase

    # extracts only letters ignoring digits spaces, punctuation

    letters = re.findall(r'[a-zA-Z]',sentence.lower())
    # Efficiently counts occurences.
    # Count occurrences
    counts = Counter(letters)

    # Sort alphabetically and format
    result = [f"{char} {counts[char]}" for char in sorted(counts)]

    print(counts)

if __name__ == "__main__":
    print(count_characters("hello world"))
    print(character_count("hello world"))
    unittest.main()