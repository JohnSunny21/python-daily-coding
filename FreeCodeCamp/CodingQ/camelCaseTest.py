import unittest
from camelCase import to_camel_case

class camelCaseTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(to_camel_case("Hi this-is_good"),"hiThisIsGood")

    def test_2(self):
        self.assertEqual(to_camel_case("hello world"),"helloWorld")

    def test_3(self):
        self.assertEqual(to_camel_case("HELLO WORLD"),"helloWorld")

    def test_4(self):
        self.assertEqual(to_camel_case("secret agent-X"),"secretAgentX")
    def test_5(self):
        self.assertEqual(to_camel_case("FREE cODE cAMP"),"freeCodeCamp")
    def test_6(self):
        self.assertEqual(to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"),"yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk")


if __name__ == "__main__":
    unittest.main()