import unittest
from CsvHeaderParser import get_headings


class CsvHeaderParserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_headings("name,age,city"),["name","age","city"])

    def test2(self):
        self.assertEqual(get_headings("first name,last name,phone"),["first name", "last name", "phone"])

    def test3(self):
        self.assertEqual(get_headings("username , email , signup date "),["username", "email", "signup date"])


if __name__ == "__main__":
    unittest.main()