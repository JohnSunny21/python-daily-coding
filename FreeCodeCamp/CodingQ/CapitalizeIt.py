"""  
Capitalize It
Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space.
"""


import unittest

class CapitalizeItTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(title_case("hello world"), "Hello World")

    def test2(self):
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")
    
    def test3(self):
        self.assertEqual(title_case("JAVASCRIPT AND PYTHON"),"Javascript And Python")

    def test4(self):
        self.assertEqual(title_case("AvOcAdO tOAst fOr brEAkfAst"),"Avocado Toast For Breakfast")


def title_case(title):

    lis = [word.capitalize() for word in title.split()]

    return " ".join(lis)


if __name__ == "__main__":
    print(title_case("iam the shadows"))
    unittest.main()