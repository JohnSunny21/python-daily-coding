import unittest
from secondBest import get_laptop_cost

class secondBestTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_laptop_cost([1500, 2000, 1800, 1400], 1900),1800)

    def test2(self):
        self.assertEqual(get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900),1800)

    def test3(self):
        self.assertEqual(get_laptop_cost([2099, 1599, 1899, 1499], 2200),1899)
    
    def test4(self):
        self.assertEqual(get_laptop_cost([2099, 1599, 1899, 1499], 1000),0)

    def test5(self):
        self.assertEqual(get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450),1400)

if __name__ == "__main__":
    unittest.main()