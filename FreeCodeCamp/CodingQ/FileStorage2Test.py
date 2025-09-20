import unittest
from FileStorage2 import number_of_files

class FileStorge2Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(number_of_files(500,"KB",1),2000)
    
    def test2(self):
        self.assertEqual(number_of_files(50000,"B",1),20000)

    def test3(self):
        self.assertEqual(number_of_files(5,"MB",1),200)

    def test4(self):
        self.assertEqual(number_of_files(4096,"B",1.5),366210)

    def test5(self):
        self.assertEqual(number_of_files(220.5,"KB",100),453514)

    def test6(self):
        self.assertEqual(number_of_files(4.5,"MB",750),166666)


if __name__ == "__main__":
    unittest.main()