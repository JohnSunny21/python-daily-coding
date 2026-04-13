"""
Name Initials
Given a full name as a string, return their initials.

Names to initialize are separated by a space.
Initials should be made uppercase.
Initials should be separated by dots.
For example, "Tommy Millwood" returns "T.M.".
"""


import unittest

class NameInitialsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_initials("Tommy Millwood"), "T.M.")

    def test2(self):
        self.assertEqual(get_initials("Savanna Puddlesplash"), "S.P.")

    def test3(self):
        self.assertEqual(get_initials("Frances Cowell Conrad"), "F.C.C.")

    def test4(self):
        self.assertEqual(get_initials("Dragon"), "D.")

    def test5(self):
        self.assertEqual(get_initials("Dorothy Vera Clump Haverstock Norris"), "D.V.C.H.N.")








def get_initials(name):

    result = []

    for n in name.split():
        result.append(n[0].upper())

    return ".".join(result) + "."

def get_initials_second(name):

    parts = name.strip().split()
    initials = [p[0].upper() for p in parts]
    return ".".join(initials) + "."


from utils.benchmark import benchmark
if __name__ == "__main__":


    
    TESTCASES = [
    (("Tommy Millwood",), "T.M."),
    (("Savanna Puddlesplash",), "S.P."),
    (("Frances Cowell Conrad",), "F.C.C."),
    (("Dragon",), "D."),
    (("Dorothy Vera Clump Haverstock Norris",), "D.V.C.H.N.")]

    scores = benchmark(
        {"first" : get_initials,
         "second": get_initials_second},
        TESTCASES,
        10000
    )

    unittest.main()