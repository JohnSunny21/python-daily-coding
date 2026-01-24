"""  


Bingo! Letter
Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:

Letter	Number Range
"B"	1-15
"I"	16-30
"N"	31-45
"G"	46-60
"O"	61-75


"""

import unittest

class BingoLetterTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_bingo_letter(75), "O")

    def test2(self):
        self.assertEqual(get_bingo_letter(54), "G")

    def test3(self):
        self.assertEqual(get_bingo_letter(25), "I")

    def test4(self):
        self.assertEqual(get_bingo_letter(38), "N")

    def test5(self):
        self.assertEqual(get_bingo_letter(11), "B")




def get_bingo_letter(n):


    if 61 <= n <= 75:
        return "O"
    elif 46 <= n <= 60:
        return "G"
    elif 31 <= n <= 45:
        return "N"
    elif 16 <= n <= 30:
        return "I"
    elif 1 <= n <= 15:
        return "B"
    else: 
        return None
"""
These are simple range checks map directly to letters.

Strengths:

Very clear and easy to read.
directly shows the ranges, so anyonne reading the code knows the exact mapping.
no hidden logic - explicit boundaries.

Weaknesses of the both solutions
These both solutions (above and below) are slightly repetitive.
If range change, you must edit multiple conditions.
Doesn't handle invalid inputs(like n = 0 or n = 100) - it just returns None so we handlied it using None
"""
    
def get_bingo_letter(n):

    if 1 <= n <= 15:
        return "B"
    elif 16 <= n <= 30:
        return "I"
    elif 31 <= n <= 45:
        return "N"
    elif 46 <= n <= 60:
        return "G"
    elif 61 <= n <= 75:
        return "O"
    else:
        return None
    




def get_bingo_letter(n):

    if not (1 <= n <= 75):
        return None
    
    bingo_map = {
        75: "O",
        60: "G",
        45: "N",
        30: "I",
        15: "B"
    }

    for limit, letter in sorted(bingo_map.items()):
        if n <= limit:
            return letter
        
# More compact version
def get_bingo_letter(n):

    if not (1 <= n <= 75):
        return None
    bingo_map = {75: "O", 60: "G", 45: "N", 30: "I", 15: "B"}

    return next(letter for limit, letter in sorted(bingo_map.items()) if n <= limit)
        
"""
More compact.
Easy to extend - just add new cutoffs to the dictionary .
avoids multiple elif chains

but still need to handle invalid inputs so added the checks.

"""


"""

=> Bingo numbers go from 1 to 75, split into 5 groups of 15.
=> Formula:     index = (n - 1) / 15

=> (integer division)
-> Then map index 0 -> B, 1 -> I, 2 -> N, 3 -> G, 4 -> O.


"""

def get_bingo_letter(n):

    if not (1 <= n <= 75):
        return None
    
    letters = ["B", "I","N","G","O"]
    index = (n - 1) // 15
    return letters[index]
"""
=> NO conditionals or lookup tables.
=> Just math -> array indexing.
=> Easy to maintain: if the ranges ever change, adjust the divisor.

"""
        
if __name__ == "__main__":
    unittest.main()