""" 

Duplicate Character Count
Given two strings, return a count of characters from the second string that can be found in the first.

Duplicate characters in the second string are counted separately.
"""



import unittest


class DuplicateCharacterCountTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(duplicate_character_count("aloha", "hei"), 1)

    def test2(self):
        self.assertEqual(duplicate_character_count("jambo", "bonjour"), 4)

    def test3(self):
        self.assertEqual(duplicate_character_count("hello", "hola"), 3)

    def test4(self):
        self.assertEqual(duplicate_character_count("ola", "hej"), 0)

    def test5(self):
        self.assertEqual(duplicate_character_count("ciao", "konnichiwa"), 5)

    def test6(self):
        self.assertEqual(duplicate_character_count("merhaba", "xin chao"), 2)

    def test7(self):
        self.assertEqual(duplicate_character_count("hello world", "hello to everyone around the world"), 26)


TESTCASES = [
    (("aloha", "hei",), 1),
    (("jambo", "bonjour",), 4),
    (("hello", "hola",), 3),
    (("ola", "hej",), 0),
    (("ciao", "konnichiwa",), 5),
    (("merhaba", "xin chao",), 2),
    (("hello world", "hello to everyone around the world",), 26)
]




def duplicate_character_count(str1, str2):

    set1 = set(str1)
    
    count = 0

    for char in str2:
        if char in set1:
            count += 1

    return count



from utils.benchmark import benchmark

if __name__ == "__main__":


    scores = benchmark({"first": duplicate_character_count}, TESTCASES, 10000)

    unittest.main()