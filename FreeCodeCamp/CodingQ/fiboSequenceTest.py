import unittest
from fiboSequence import fibonacci_sequence


class fiboSequenceTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(fibonacci_sequence([0, 1], 20),[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])

    def test2(self):
        self.assertEqual(fibonacci_sequence([21, 32], 1),[21])

    def test3(self):
        self.assertEqual(fibonacci_sequence([0, 1], 0),[])

    def test4(self):
        self.assertEqual(fibonacci_sequence([10, 20], 2),[10,20])

    def test5(self):
        self.assertEqual(fibonacci_sequence([123456789, 987654321], 5),[123456789, 987654321, 1111111110, 2098765431, 3209876541])


if __name__ == "__main__":
    unittest.main()