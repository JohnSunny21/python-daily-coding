import unittest
from SlugGenerator import generate_slug


class SlugGeneratorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(generate_slug("helloWorld"),"helloworld")

    def test2(self):
        self.assertEqual(generate_slug("hello world!"),"hello%20world")

    def test3(self):
        self.assertEqual(generate_slug(" hello-world "),"helloworld")

    def test4(self):
        self.assertEqual(generate_slug("hello  world"),"hello%20world")

    def test5(self):
        self.assertEqual(generate_slug("  ?H^3-1*1]0! W[0%R#1]D  "),"h3110%20w0r1d")


if __name__ == "__main__":
    unittest.main()