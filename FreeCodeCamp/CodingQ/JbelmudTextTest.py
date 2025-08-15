import unittest
from JbelmudText import jbelmu

class JbelmudTextTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(jbelmu("hello world"),"hello wlord")

    def test2(self):
        self.assertEqual(jbelmu("i love jumbled text"),"i love jbelmud text")

    def test3(self):
        self.assertEqual(jbelmu("freecodecamp is my favorite place to learn to code"),"faccdeeemorp is my faiortve pacle to laern to cdoe")

    def test4(self):
        self.assertEqual(jbelmu("the quick brown fox jumps over the lazy dog"),"the qciuk borwn fox jmpus oevr the lazy dog")



if __name__ == "__main__":
    unittest.main()