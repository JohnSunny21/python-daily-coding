"""  
Checkerboard
Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

The characters should alternate like a checkerboard.
The top-left cell must always be "X".
For example, given [3, 3], return:

[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]
"""

import unittest

class CheckboardTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(create_board([3, 3]), [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]])

    def test2(self):
        self.assertEqual(create_board([6, 1]), [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]])

    def test3(self):
        self.assertEqual(create_board([2, 10]), [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]])

    def test4(self):
        self.assertEqual(create_board([5, 4]), [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]])



def create_board(dimenstions):

    rows, cols = dimenstions
    spot = "X"
    checker_board = []
    for r in range(rows):
        row_board = []
        for c in range(cols):
            if spot == "X":
                row_board.append(spot)
                spot = "O"
            else:
                row_board.append(spot)
                spot = "X"
        checker_board.append(row_board)

    return checker_board


"""
Checkerboard bug :

This is close, but the core bug is that the variable spot is global across the entire board.
It flips with every cell, including across row boundaries, so the start of each new row depends on how
the previous row ended. That breaks the rule "top-left is X and characters alternate like a checkerboard, because every row must start with
X if the number of columns is odd, and with alternating X/O if even, based on row party.

=> Root cause: spot isn't reset at the start of each row.
=> Symptom: Rows may start with O when they should start with X (or vice versa,) depending on the last cell of teh previous row.

=> Correct rule: Cell (r, c) is X if (r + c) % 2 == 0, else O.
Alternatively, recompute the row's starting spot per row from parity.


"""

# Parity-based (cleanest)
def create_board(dimensions):
    rows , cols = dimensions
    checker_board = []

    for r in range(rows):
        row_board = []
        for c in range(cols):
            row_board.append("X" if (r + c) % 2 == 0 else "O")

        checker_board.append(row_board)

    return checker_board


"""
Edge cases:

Top-left constraint: with either fix, (0, 0) is always "X". 

=> Odd vs even columns:
    => if ccols is odd, each new row must start with the opposite of the previous row to
        maintain the checkerboard. The parity formula handles this automatically.

    => if cols is even, each row starts with the same as the previous row, parity formula also handles this.
"""
# Reset spot each row(previous flip style)
def create_board_flip(dimensions):

    rows, cols = dimensions

    checker_board = []

    for r in range(rows):
        # Start each row based on row parity: even rows start with "X", odd tiwh "O"
        spot = "X" if r % 2 == 0 else "O"
        row_board = []
        for _ in range(cols):
            row_board.append(spot)
            spot = "O" if spot == "X" else "X"
        checker_board.append(row_board)


    return checker_board
