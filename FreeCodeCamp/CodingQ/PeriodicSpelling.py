""" 

Periodic Spelling
Given a word, determine if it can be spelled using element symbols from the periodic table.

Ignore casing when spelling a word. "neon" can be spelled with the symbols "Ne", "O", and "N".
Here's a full list of the element symbols:

["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"];
Return an array of the elements used to spell the word, in their original casing and in the order to spell the word. Or, an empty array if it can't be spelled.
"""


import unittest

class PeriodicSpellingTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_periodic_spelling("neon"), ["Ne", "O", "N"])

    def test2(self):
        self.assertEqual(get_periodic_spelling("rational"), ["Ra", "Ti", "O", "N", "Al"])

    def test3(self):
        self.assertEqual(get_periodic_spelling("yarn"), ["Y", "Ar", "N"])

    def test4(self):
        self.assertIn(get_periodic_spelling("carbon"),
                    [["C", "Ar", "B", "O", "N"], ["Ca", "Rb", "O", "N"]])

    def test5(self):
        self.assertIn(get_periodic_spelling("noisy"),
                    [["N", "O", "I", "S", "Y"], ["No", "I", "S", "Y"]])

    def test6(self):
        self.assertIn(get_periodic_spelling("bicycles"),
                    [["B", "I", "C", "Y", "Cl", "Es"], ["Bi", "C", "Y", "Cl", "Es"]])

    def test7(self):
        self.assertIn(get_periodic_spelling("optics"),
                    [["O", "P", "Ti", "C", "S"],
                    ["O", "P", "Ti", "Cs"],
                    ["O", "Pt", "I", "C", "S"],
                    ["O", "Pt", "I", "Cs"]])

    def test8(self):
        self.assertEqual(get_periodic_spelling("value"), [])



TESTCASES = [
    (("neon",), [["Ne", "O", "N"]]),
    (("rational",), [["Ra", "Ti", "O", "N", "Al"]]),
    (("yarn",), [["Y", "Ar", "N"]]),
    (("carbon",), [["C", "Ar", "B", "O", "N"], ["Ca", "Rb", "O", "N"]]),
    (("noisy",), [["N", "O", "I", "S", "Y"], ["No", "I", "S", "Y"]]),
    (("bicycles",), [["B", "I", "C", "Y", "Cl", "Es"], ["Bi", "C", "Y", "Cl", "Es"]]),
    (("optics",), [["O", "P", "Ti", "C", "S"], ["O", "P", "Ti", "Cs"], ["O", "Pt", "I", "C", "S"], ["O", "Pt", "I", "Cs"]]),
    (("value",), [[]])
]



ELEMENTS = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]


def get_periodic_spelling(word):

    word = word.lower()
    symbols = {s.lower(): s for s in ELEMENTS}
    n = len(word)


    memo = {}

    def dfs(i):

        if i == n:
            return []
        
        if i in memo:
            return memo[i]
        
        # Try 1-letter and 2-letter symbols
        for length in [1, 2]:
            if i + length <= n:
                piece = word[i: i+length]
                if piece in symbols:
                    rest = dfs(i+length)
                    if rest is not None:
                        memo[i] = [symbols[piece]] + rest
                        return memo[i]
                    
        memo[i] = None

        return None


    result = dfs(0)
    return result if result is not None else []




from utils.benchmark import benchmark


if __name__ == "__main__":

    # scores = benchmark({
    #     "first": get_periodic_spelling
    # }, TESTCASES, 10000)
    print(get_periodic_spelling("neon"))
    unittest.main()