"""

Fingerprint Test
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.
"""

import unittest

class FingerPrintTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_match("helloworld","helloworld"),True)

    def test2(self):
        self.assertEqual(is_match("helloworld","helloworlds"), False)

    def test3(self):
        self.assertEqual(is_match("helloworld","jelloworld"),True)

    def test4(self):
        self.assertEqual(is_match("thequickbrownfoxjumpsoverthelazydog","thequickbrownfoxjumpsoverthelazydog"),True)

    def test5(self):
        self.assertEqual(is_match("theslickbrownfoxjumpsoverthelazydog","thequickbrownfoxjumpsoverthehazydog"),True)

    def test6(self):
        self.assertEqual(is_match("thequickbrownfoxjumpsoverthelazydog","thequickbrownfoxjumpsoverthehazycat"),False)

    


def is_match(fingerprint_a,fingerprint_b):

    if len(fingerprint_a) != len(fingerprint_b):
        return False
    
    if not all(char.islower() for char in fingerprint_a):
        return False
    
    if not all(char.islower() for char in fingerprint_b):
        return False
    
    differ_characters = 0
    for char, check in zip(fingerprint_a, fingerprint_b):
        if char != check:
            differ_characters += 1

    if differ_characters > int(len(fingerprint_a) * 10 / 100):
        return False
    

    return True


def is_match_optimized(fingerprint_a, fingerprint_b):

    if len(fingerprint_a) != len(fingerprint_b):
        return False
    
    differences = sum(1 for a, b, in zip(fingerprint_a, fingerprint_b) if a!=b)
    threshold = len(fingerprint_a) * 0.1 # len(finger...)*10/100
    return differences <= threshold

if __name__ == "__main__":
    print(is_match("helloworld","helloworld"))
    print(is_match("abcdefghi","abcxefghi"))
    
    unittest.main()