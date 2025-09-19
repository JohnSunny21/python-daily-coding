import unittest
from PhotoStorage import number_of_photos

class PhotoStorageTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(number_of_photos(1,1),1000)

    def test2(self):
        self.assertEqual(number_of_photos(2,1),500)

    def test3(self):
        self.assertEqual(number_of_photos(4,256),64000)

    def test4(self):
        self.assertEqual(number_of_photos(3.5,750),214285)

    def test5(self):
        self.assertEqual(number_of_photos(3.5,5.5),1571)

if __name__ == "__main__":
    unittest.main()