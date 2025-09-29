import unittest

from LongestWord import get_longest_word

class LongestWordTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_longest_word("coding is fun"),"coding")

    def test2(self):
        self.assertEqual(get_longest_word("Coding challenges are fun and educational."),"educational")

    def test3(self):
        self.assertEqual(get_longest_word("This sentence has multiple long words."),"sentence")

if __name__ == "__main__":
    unittest.main()