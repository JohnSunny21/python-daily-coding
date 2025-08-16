import unittest
from AnagramChecker import are_anagrams


class AnagramCheckerTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(are_anagrams("listen", "silent"),True)

    def test2(self):
        self.assertEqual(are_anagrams("School master", "The classroom"),True)

    def test3(self):
        self.assertEqual(are_anagrams("A gentleman", "Elegant man"),True)

    def test4(self):
        self.assertEqual(are_anagrams("Hello", "World"),False)

    def test5(self):
        self.assertEqual(are_anagrams("apple", "banana"),False)

    def test6(self):
        self.assertEqual(are_anagrams("cat", "dog"),False)



if __name__ == "__main__":
    unittest.main()