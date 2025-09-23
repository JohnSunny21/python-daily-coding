import unittest

from StringMirror import is_mirror

class StringMirrorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_mirror("helloworld","helloworld"),False)

    def test2(self):
        self.assertEqual(is_mirror("Hello World", "dlroW olleH"),True)

    def test3(self):
        self.assertEqual(is_mirror("RaceCar", "raCecaR"),True)

    def test4(self):
        self.assertEqual(is_mirror("RaceCar", "RaceCar"),False)

    def test5(self):
        self.assertEqual(is_mirror("Mirror", "rorrim"),False)

    def test6(self):
        self.assertEqual(is_mirror("Hello World", "dlroW-olleH"),True)

    def test7(self):
        self.assertEqual(is_mirror("Hello World", "!dlroW !olleH"),True)

        

if __name__ == "__main__":
    unittest.main()