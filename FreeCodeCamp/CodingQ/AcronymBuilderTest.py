import unittest
from AcronymBuiler import build_acronym

class AcronymBuilerTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(build_acronym("Search Engine Optimization"),"SEO")
    
    def test2(self):
        self.assertEqual(build_acronym("Frequently Asked Questions"),"FAQ")

    def test3(self):
        self.assertEqual(build_acronym("National Aeronautics and Space Administration"),"NASA")

    def test4(self):
        self.assertEqual(build_acronym("Federal Bureau of Investigation"),"FBI")

    def test5(self):
        self.assertEqual(build_acronym("For your information"),"FYI")
    
    def test6(self):
        self.assertEqual(build_acronym("By the way"),"BTW")

    def test7(self):
        self.assertEqual(build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily"),"AUHWPOTIMSH")


if __name__ == "__main__":

    unittest.main()