import unittest
from strDecode import decode


class strDecodeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(decode("(f(b(dc)e)a)"),"abcdef")

    def test2(self):
        self.assertEqual(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"),"Can you read this?")
    def test3(self):
        self.assertEqual(decode("f(Ce(re))o((e(aC)m)d)p"),"freeCodeCamp")


if __name__ == "__main__":
    unittest.main()