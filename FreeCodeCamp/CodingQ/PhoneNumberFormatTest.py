import unittest
from PhoneNumberFormatter import format_number,format_number_optimized


class PhoneNumberFormatterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(format_number("05552340182"),"+0 (555) 234-0182")

    
    def test2(self):
        self.assertEqual(format_number("15554354792"),"+1 (555) 435-4792")

    def test3(self):
        self.assertEqual(format_number_optimized("05552340182"),"+0 (555) 234-0182")

    def test4(self):
        self.assertEqual(format_number_optimized("15554354792"),"+1 (555) 435-4792")


if __name__ == "__main__":
    unittest.main()