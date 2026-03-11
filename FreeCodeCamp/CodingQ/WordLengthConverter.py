""" 
Word Length Converter
Given a string of words, return a new string where each word is replaced by its length.

Words in the given string will be separated by a single space
Keep the spaces in the returned string.
For example, given "hello world", return "5 5".
"""

import unittest

class WordLengthConverterTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(convert_words("hello world"), "5 5")

      def test2(self):
          self.assertEqual(convert_words("Thanks and happy coding"), "6 3 5 6")

      def test3(self):
          self.assertEqual(convert_words("The quick brown fox jumps over the lazy dog"), "3 5 5 3 5 4 3 4 3")       

      def test4(self):
          self.assertEqual(convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl"), "5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4")



def convert_words(s):

    result = []

    for word in s.split():
        result.append(str(len(word)))

    return " ".join(result)

def convert_words(s):

    return " ".join(str(len(word)) for word in s.split())


if __name__ == "__main__":
    unittest.main()