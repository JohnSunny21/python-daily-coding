import unittest
from candleLight import burn_candles


class candleLightTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(burn_candles(7,2),13)

    def test2(self):
        self.assertEqual(burn_candles(10,5),12)
    
    def test3(self):
        self.assertEqual(burn_candles(20,3),29)

    def test4(self):
        self.assertEqual(burn_candles(17,4),22)

    def test5(self):
        self.assertEqual(burn_candles(2345,3),3517)



if __name__ == "__main__":
    unittest.main()


