import unittest
from CaughtSpeeding import speeding,speeding_optimized

class CaughtSpeedingTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(speeding([50,60,55],60),[0,0])

    def test2(self):
        self.assertEqual(speeding([58,50,60,55],55),[2,4])

    def test3(self):
        self.assertEqual(speeding([61,81,74,88,65,71,68],70),[4,8.5])

    def test4(self):
        self.assertEqual(speeding([100,105,95,102],100),[2,3.5])

    def test5(self):
        self.assertEqual(speeding([40,45,44,50,112,39],55),[1,57])

    def test6(self):
        self.assertEqual(speeding_optimized([50,60,55],60),[0,0])

    def test7(self):
        self.assertEqual(speeding_optimized([58,50,60,55],55),[2,4])

    def test8(self):
        self.assertEqual(speeding_optimized([61,81,74,88,65,71,68],70),[4,8.5])

    def test9(self):
        self.assertEqual(speeding_optimized([100,105,95,102],100),[2,3.5])

    def test10(self):
        self.assertEqual(speeding_optimized([40,45,44,50,112,39],55),[1,57])


if __name__ == "__main__":
    unittest.main()