import unittest
from FillTheTank import fill_the_tank

class FillTheTankTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(fill_the_tank(20,0,4.00),"$80.00")
    
    def test2(self):
        self.assertEqual(fill_the_tank(15,10,3.50),"$17.50")
    
    def test3(self):
        self.assertEqual(fill_the_tank(18,9,3.25),"$29.25")

    def test4(self):
        self.assertEqual(fill_the_tank(12,12,4.99),"$0.00")

    def test5(self):
        self.assertEqual(fill_the_tank(15,9.5,3.98),"$21.89")

    
if __name__ == "__main__":
    unittest.main()