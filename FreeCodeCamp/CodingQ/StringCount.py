"""
String Count
Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.
"""

import unittest

class StringCountTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(count("abcdefg","def"),1)

    def test2(self):
        self.assertEqual(count("hello","world"),0)
    
    def test3(self):
        self.assertEqual(count("mississippi","iss"),2)

    def test4(self):
        self.assertEqual(count("she sells seashells by the seashore","sh"),3)

    def test5(self):
        self.assertEqual(count('101010101010101010101', '101'),10)




def count(text,parameter):

    count = 0

    for i in range(len(text) - len(parameter) + 1):
        if text[i:i+len(parameter)] == parameter:
            count += 1
        

    return count




if __name__ == "__main__":
    print(count("abcdefg","def"))
    print(count("hello","world"))
    print(count("mississippi","iss"))
    unittest.main()