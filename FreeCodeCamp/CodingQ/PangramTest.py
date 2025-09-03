import unittest
from Pangram import is_pangram_withEdgeCase


class PangramTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_pangram_withEdgeCase("hello","helo"),True)

    def test2(self):
        self.assertEqual(is_pangram_withEdgeCase("hello","hel"),False)

    def test3(self):
        self.assertEqual(is_pangram_withEdgeCase("hello","helow"),False)

    def test4(self):
        self.assertEqual(is_pangram_withEdgeCase("hello world","helowrd"),True)

    def test5(self):
        self.assertEqual(is_pangram_withEdgeCase("Hello World!","helowrd"),True)

    def test6(self):
        self.assertEqual(is_pangram_withEdgeCase("Hello World!","heliowrd"),False)

    def test7(self):
        self.assertEqual(is_pangram_withEdgeCase("freeCodeCamp","frcdmp"),False)

    def test8(self):
        self.assertEqual(is_pangram_withEdgeCase("The quick brown fox jumps over the lazy dog.","abcdefghijklmnopqrstuvwxyz"),True)


if __name__ == "__main__":
    unittest.main()