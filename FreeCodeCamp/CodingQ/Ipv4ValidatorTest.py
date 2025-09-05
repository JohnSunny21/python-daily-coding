import unittest
from Ipv4Validator import is_valid_ipv4

class Ipv4ValidatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_valid_ipv4("192.168.1.1"),True)

    def test2(self):
        self.assertEqual(is_valid_ipv4("0.0.0.0"),True)

    def test3(self):
        self.assertEqual(is_valid_ipv4("255.01.50.11"),False)

    def test4(self):
        self.assertEqual(is_valid_ipv4("255.00.50.11"),False)

    def test5(self):
        self.assertEqual(is_valid_ipv4("256.101.50.1"),False)

    def test6(self):
        self.assertEqual(is_valid_ipv4("192.168.101."),False)

    def test7(self):
        self.assertEqual(is_valid_ipv4("192168145213"),False)


if __name__ == "__main__":

    unittest.main()