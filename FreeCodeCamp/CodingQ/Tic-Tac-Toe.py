"""  

Tic-Tac-Toe
Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

Each element in the given matrix is either an "X" or "O".
A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

Return:

"X wins" if player X has three in a row.
"O wins" if player O has three in a row.
"Draw" if no player has three in a row.
"""

import unittest

class TicTacToeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]), "X wins")

    def test2(self):
        self.assertEqual(tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]), "O wins")

    def test3(self):
        self.assertEqual(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]), "Draw")

    def test4(self):
        self.assertEqual(tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]), "O wins")

    def test5(self):
        self.assertEqual(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]), "X wins")

    def test6(self):
        self.assertEqual(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]), "Draw")



def tic_tac_toe(board):
    
    # Check rows

    for row in board:
        if row.count("X") == 3:
            return "X wins"
        if row.count("O") == 3:
            return "O wins"
        

    # Check columns
    for col in range(3):
        columns = [board[row][col] for row in range(3)]

        if columns.count("X") == 3:
            return "X wins"
        if columns.count("O") == 3:
            return "O wins"
        

    # Check diagonals

    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2-i] for i in range(3)]


    if diag1.count("X") == 3 or diag2.count("X") == 3:
        return "X wins"
    if diag2.count("O") == 3 or diag2. count("O") == 3:
        return "O wins"
    
    return "Draw"
    


if __name__ == "__main__":
    unittest.main()