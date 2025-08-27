import unittest
from unOrderOperations import evaluate

class unOrderOperationsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(evaluate([5, 6, 7, 8, 9], ['+', '-']),3)

    def test2(self):
        self.assertEqual(evaluate([17, 61, 40, 24, 38, 14], ['+', '%']),38)

    def test3(self):
        self.assertEqual(evaluate([20, 2, 4, 24, 12, 3], ['*', '/']),60)

    def test4(self):
        self.assertEqual(evaluate([11, 4, 10, 17, 2], ['*', '*', '%']),30)

    def test5(self):
        self.assertEqual(evaluate([33, 11, 29, 13], ['/', '-']),-2)

if __name__ == "__main__":
    unittest.main()