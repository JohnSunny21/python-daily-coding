"""  

Valid Pawn Moves
Given the position of one of your pawns on a chessboard, return an array of all the valid squares it can move to in ascending order.

A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:

A8	B8	C8	D8	E8	F8	G8	H8
A7	B7	C7	D7	E7	F7	G7	H7
A6	B6	C6	D6	E6	F6	G6	H6
A5	B5	C5	D5	E5	F5	G5	H5
A4	B4	C4	D4	E4	F4	G4	H4
A3	B3	C3	D3	E3	F3	G3	H3
A2	B2	C2	D2	E2	F2	G2	H2
A1	B1	C1	D1	E1	F1	G1	H1
For this challenge:

You are the player on the bottom of the board.
Pawns can only move one square "up".
Unless the pawn is in the starting row (row 2), then it can move one or two squares up.
For example, given "D4", return ["D5"], the only square your pawn can move to. Given "B2", return ["B3", "B4"], because it's on the starting row and needs to be in ascending order.
"""


import unittest


class PawnMovesTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(findPawnMoves("D4"), ["D5"])

      def test2(self):
          self.assertEqual(findPawnMoves("B2"), ["B3", "B4"])

      def test3(self):
          self.assertEqual(findPawnMoves("A7"), ["A8"])

      def test4(self):
          self.assertEqual(findPawnMoves("G2"), ["G3", "G4"])

      def test5(self):
          self.assertEqual(findPawnMoves("E3"), ["E4"])



def findPawnMoves(position):

    col, row = position[0], int(position[1])

    moves = []

    if row == 2:
        moves.append(f"{col}{row + 1}")
        moves.append(f"{col}{row + 2}")
    elif row < 8:
        moves.append(f"{col}{row + 1}")

    return moves


if __name__ == "__main__":
    unittest.main()