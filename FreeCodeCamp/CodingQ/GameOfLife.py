"""  
Game of Life
Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

Each cell is either 1 (alive) or 0 (dead).
A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
Cells on the edges have fewer than eight neighbors.
Rules for updating each cell:

Any live cell with fewer than two live neighbors dies (underpopulation).
Any live cell with two or three live neighbors lives on.
Any live cell with more than three live neighbors dies (overpopulation).
Any dead cell with exactly three live neighbors becomes alive (reproduction).
For example, given:

[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]
return:

[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]
Each cell updates according to the number of live neighbors. For instance, [0][0] stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on.
"""

import unittest


class GameOfLifeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]),[[0, 1, 1], [0, 0, 1], [1, 1, 1]])

    def test2(self):
        self.assertEqual(game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]),[[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]])

    def test3(self):
        self.assertEqual(game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),[[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    def test4(self):
        self.assertEqual(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]),[[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]])



"""
The algorithm is O(n x m) where n and m are dimensions of the board.
Each cell is updated based on its neighbors, producing a new board state.
Works for any rectangular grid, not just square ones.

"""
def game_of_life(grid):

    rows, cols = len(grid), len(grid[0])

    def count_neighbors(r, c):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),    (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                count += grid[nr][nc]

        return count
    
    new_board = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(r, c)
            if grid[r][c] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_board[r][c] = 0
                else:
                    new_board[r][c] = 1
            else:
                if neighbors == 3:
                    new_board[r][c] = 1

    return new_board



if __name__ == "__main__":
    print(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]))
    unittest.main()


