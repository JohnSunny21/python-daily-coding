import unittest
from vowelRepeater import repeat_vowels


class vowelRepeaterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(repeat_vowels("hello world"),"helloo wooorld")

    def test2(self):
        self.assertEqual(repeat_vowels("freeCodeCamp"),"freeeCooodeeeeCaaaaamp")

    def test3(self):
        self.assertEqual(repeat_vowels("AEIOU"),"AEeIiiOoooUuuuu")

    def test4(self):
        self.assertEqual(repeat_vowels("I like eating ice cream in Iceland"),"I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand")


if __name__ == "__main__":
    unittest.main()