import unittest
from arrayDiff import array_diff

class ArrayDiffTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]),["cherry"])

    def test2(self):
        self.assertEqual(array_diff(["apple", "banana", "cherry"], ["apple", "banana"]),["cherry"])

    def test3(self):
        self.assertEqual(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]),["eight", "four", "six", "two"])

    def test4(self):
        self.assertEqual(array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]),["five", "one", "seven", "three"])

    def test5(self):
        self.assertEqual(array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]),["freeCodeCamp", "rocks"])

if __name__ == "__main__":

    unittest.main()