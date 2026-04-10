""" 

Rook Attack
Given two strings for the location of two rooks on a chess board, determine if they can attack each other.

A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:

A8	B8	C8	D8	E8	F8	G8	H8
A7	B7	C7	D7	E7	F7	G7	H7
A6	B6	C6	D6	E6	F6	G6	H6
A5	B5	C5	D5	E5	F5	G5	H5
A4	B4	C4	D4	E4	F4	G4	H4
A3	B3	C3	D3	E3	F3	G3	H3
A2	B2	C2	D2	E2	F2	G2	H2
A1	B1	C1	D1	E1	F1	G1	H1
Rooks can move as many squares as they want in a horizontal or vertical direction. So if they are on the same row or column, they can attack each other.
"""

import unittest

class RookAttackTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(rook_attack("A1", "A8"), True)

    def test2(self):
        self.assertEqual(rook_attack("B4", "F4"), True)

    def test3(self):
        self.assertEqual(rook_attack("E3", "D4"), False)

    def test4(self):
        self.assertEqual(rook_attack("H7", "F6"), False)




def rook_attack_first(rook1, rook2):

    rook1_char, rook1_num = rook1[0], rook1[1] # use rook#[1:] for larger boards like "A10" to get full digits

    rook2_char, rook2_num = rook2[0], rook2[1]

    if rook1_char == rook2_char:
        return True
    
    if rook1_char != rook2_char and rook2_num == rook1_num:
        return True
    

    return False

""" 
The above solution works in principle. But it's a bit more complicated than it needs to be, 
and it has one subtle limitation: you're assuming the row is always a single character (rook1[1]). That's fine for a standard 8x8 board ( 1 - 8), but if you ever extend to 
larger board (like "A10"), it would break.


"""



def rook_attack(rook1, rook2):

    col1, row1 = rook1[0], rook1[1]
    col2, row2 = rook2[0], rook2[1]

    # Rooks attack if same column or same row
    return col1 == col2 or row1 == row2








from utils.benchmark import benchmark
if __name__ == "__main__":

    
    TESTCASES = [
    (("A1", "A8",), True),
    (("B4", "F4",), True),
    (("E3", "D4",), False),
    (("H7", "F6",), False)
]
    scores = benchmark(
        {"first": rook_attack_first,
         "second": rook_attack},
        TESTCASES,
        10000
    )

    unittest.main()