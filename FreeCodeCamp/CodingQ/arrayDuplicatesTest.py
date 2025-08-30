import unittest
from arrayDuplicates import find_duplicates


class arrayDuplicatesTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(find_duplicates([1, 2, 3, 4, 5]),[])

    def test2(self):
        self.assertEqual(find_duplicates([1, 2, 3, 4, 1, 2]),[1,2])

    def test3(self):
        self.assertEqual(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]),[-6, 0, 2, 4, 5, 23])


if __name__ == "__main__":
    unittest.main()