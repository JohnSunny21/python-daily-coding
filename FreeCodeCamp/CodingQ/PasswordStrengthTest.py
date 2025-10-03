import unittest

from PasswordStrength import check_strength

class PasswordStrengthTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(check_strength("123456"),"weak")

    def test2(self):
        self.assertEqual(check_strength("pass!!!"),"weak")
    
    def test3(self):
        self.assertEqual(check_strength("Qwerty"),"weak")

    def test4(self):
        self.assertEqual(check_strength("PASSWORD"),"weak")

    def test5(self):
        self.assertEqual(check_strength("PASSWORD!"),"medium")

    def test6(self):
        self.assertEqual(check_strength("PassWord%^!"),"medium")

    def test7(self):
        self.assertEqual(check_strength("qwerty12345"),"medium")

    def test8(self):
        self.assertEqual(check_strength("PASSWORD!"),"medium")

    def test9(self):
        self.assertEqual(check_strength("PASSWORD!^&"),"medium")
    
    def test10(self):
        self.assertEqual(check_strength("S3cur3P@ssw0rd"),"strong")

    def test11(self):
        self.assertEqual(check_strength("C0d3&Fun!"),"strong")


if __name__ == "__main__":
    unittest.main()

    