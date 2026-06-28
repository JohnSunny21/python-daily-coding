""" 


Connect 3
Given a matrix of strings representing pieces on a game grid, determine if any player has three in a row.

Each cell contains "R", "Y", or "" (empty string).
Three in a row means three consecutive non-empty cells of the same type horizontally, vertically, or diagonally.
Return:

A flat array with the winner and the coordinates of their three winning cells in the format: ["R", [0,2], [1,3], [2,4]]. Coordinates are returned top-to-bottom, then left-to-right.
An empty array if there is no winner.
"""


import unittest


class Connect3Test(unittest.TestCase):



    def test1(self):
        self.assertEqual(connect_three([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]]), ["R", [3, 1], [3, 2], [3, 3]])

    def test2(self):
        self.assertEqual(connect_three([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]]), ["Y", [1, 1], [2, 1], [3, 1]])

    def test3(self):
        self.assertEqual(connect_three([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"],["", "R", "Y", "R"]]), ["R", [0, 3], [1, 2], [2, 1]])

    def test4(self):
        self.assertEqual(connect_three([["", "Y", "", ""], ["", "Y", "Y", ""], ["", "R", "R", "Y"], ["R", "R", "Y", "R"]]), ["Y", [0, 1], [1, 2], [2, 3]])

    def test5(self):
        self.assertEqual(connect_three([["Y", "R","R", "Y"], ["R", "Y", "Y", "R"], ["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]]), [])


TESTCASES = [
    (([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]],), ["R", [3, 1], [3, 2], [3, 3]]),
    (([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]],), ["Y", [1, 1], [2, 1], [3, 1]]),
    (([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"], ["", "R", "Y", "R"]],), ["R", [0, 3], [1, 2], [2, 1]]),
    (([["", "Y", "", ""], ["", "Y", "Y", ""], ["","R", "R", "Y"], ["R", "R", "Y", "R"]],), ["Y", [0,1], [1, 2], [2, 3]]),
    (([["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"],["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]],), [])
]



def connect_three(matrix):

    rows, cols = len(matrix) , len(matrix[0])

    # directions right, down, diag down-right, diag down-left
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]


    for r in range(rows):
        for c in range(cols):

            player = matrix[r][c]

            if player == "":
                continue

            for dr, dc in directions:
                coords = [[r, c]]
                nr, nc = r, c
                valid = True
                

                for _ in range(2):
                    nr += dr
                    nc += dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == player:
                        coords.append([nr, nc])
                    else:
                        valid = False
                        break

                if valid:
                    return [player] + coords
            
    return []




from utils.benchmark import benchmark


if __name__ == "__main__":


    scores = benchmark({
        "first": connect_three
    }, TESTCASES, 10000)

    unittest.main()
