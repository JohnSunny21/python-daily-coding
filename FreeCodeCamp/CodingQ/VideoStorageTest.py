import unittest
from VideoStorage import number_of_videos

class VideoStorageTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(number_of_videos(500,"MB",100,"GB"),200)

    def test2(self):
        self.assertEqual(number_of_videos(2000,"B",1,"TB"),"Invalid video unit")

    def test3(self):
        self.assertEqual(number_of_videos(2000,"MB",100000,"MB"),"Invalid drive unit")

    def test4(self):
        self.assertEqual(number_of_videos(500000,"KB",2,"TB"),4000)

    def test5(self):
        self.assertEqual(number_of_videos(1.5,"GB",2.2,"TB"),1466)


if __name__ == "__main__":
    unittest.main()