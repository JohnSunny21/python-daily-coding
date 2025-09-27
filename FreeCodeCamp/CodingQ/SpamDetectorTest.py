import unittest
from SpamDetector import is_spam


class SpamDetectorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_spam("+0 (200) 234-0182"),False)

    def test2(self):
        self.assertEqual(is_spam("+091 (555) 309-1922"),True)

    def test3(self):
        self.assertEqual(is_spam("+1 (555) 435-4792"),True)

    def test4(self):
        self.assertEqual(is_spam("+0 (955) 234-4364"),True)

    def test5(self):
        self.assertEqual(is_spam("+0 (155) 131-6943"),True)

    def test6(self):
        self.assertEqual(is_spam("+0 (555) 135-0192"),True)

    def test7(self):
        self.assertEqual(is_spam("+0 (555) 564-1987"),True)

    def test8(self):
        self.assertEqual(is_spam("+00 (555) 234-0182"),False)


if __name__ == "__main__":
    unittest.main()