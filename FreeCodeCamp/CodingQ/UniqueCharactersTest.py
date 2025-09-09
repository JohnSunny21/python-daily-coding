import unittest
from UniqueCharacter import all_unique


class UniqueCharacterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(all_unique("abc"),True)

    def test2(self):
        self.assertEqual(all_unique("aA"),True)

    def test3(self):
        self.assertEqual(all_unique("QwErTy123!@"),True)

    def test4(self):
        self.assertEqual(all_unique("~!@#$%^&*()_+"),True)

    def test5(self):
        self.assertEqual(all_unique("hello"),False)

    def test6(self):
        self.assertEqual(all_unique("freeCodeCamp"),False)

    def test7(self):
        self.assertEqual(all_unique("!@#*$%^&*()aA"),False)

if __name__ == "__main__":

    unittest.main()