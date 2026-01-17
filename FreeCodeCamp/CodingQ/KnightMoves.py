"""  

Knight Moves
Given the position of a knight on a chessboard, return the number of valid squares the knight can move to.

A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:

A8	B8	C8	D8	E8	F8	G8	H8
A7	B7	C7	D7	E7	F7	G7	H7
A6	B6	C6	D6	E6	F6	G6	H6
A5	B5	C5	D5	E5	F5	G5	H5
A4	B4	C4	D4	E4	F4	G4	H4
A3	B3	C3	D3	E3	F3	G3	H3
A2	B2	C2	D2	E2	F2	G2	H2
A1	B1	C1	D1	E1	F1	G1	H1
A knight moves in an "L" shape: two squares in one direction (horizontal or vertical), and one square in the perpendicular direction.

This means a knight can move to up to eight possible positions, but fewer when near the edges of the board. For example, if a knight was at A1, it could only move to B3 or C2.
"""

import unittest

class KnightMovesTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(knight_moves("A1"), 2)

    def test2(self):
        self.assertEqual(knight_moves("D4"), 8)

    def test3(self):
        self.assertEqual(knight_moves("G6"), 6)

    def test4(self):
        self.assertEqual(knight_moves("B8"), 3)

    def test5(self):
        self.assertEqual(knight_moves("H3"), 4)


def knight_moves(position):

    col = ord(position[0].upper()) - ord('A') + 1
    row = int(position[1])


    moves = [
        (2, 1) ,(2, -1), (-2, 1), (-2, -1),
        (1, -2), (1, 2), (-1, 2), (-1, -2)
    ]
    valid_moves = 0

    for dx, dy in moves:
        new_col = col + dx
        new_row = row + dy
        if 1 <= new_col <= 8 and 1 <= new_row <= 8:
            valid_moves += 1

    return valid_moves


""" 

=> Convert chess notation -> numeric coordinates.
=> apply knight's 8 possible moves.
=> count only those withn the 8x8 board. 


we can also extend it for show the valid squares rather than just showing only the count


"""


def knight_moves_positions(position):

    col = ord(position[0].upper()) - ord('A') + 1
    row = int(position[1])

    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, -2), (1, 2), (-1, 2), (-1, -2)
    ]

    valid_positions = []
    for dx, dy in moves:
        new_col = col + dx
        new_row = row + dy

        if 1 <= new_col <= 8 and 1 <= new_row <= 8:
            square = chr(ord('A') + new_col - 1) + str(new_row)
            valid_positions.append(square)


    return valid_positions

if __name__ == "__main__":
    print(knight_moves("D6"))

    print(knight_moves_positions("D6"))
    unittest.main()
