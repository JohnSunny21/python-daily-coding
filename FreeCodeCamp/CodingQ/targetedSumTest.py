import unittest
from targetedSum import find_target

class targetedSumTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(find_target([2,7,11,15],9),[0,1])

    def test2(self):
        self.assertEqual(find_target([3,2,4,5],6),[1,2])

    def test3(self):
        self.assertEqual(find_target([1,3,5,6,7,8],15),[4,5])

    def test4(self):
        self.assertEqual(find_target([1,3,5,7],14),"Target not found")



if __name__ == "__main__":
    unittest.main()