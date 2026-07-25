""" 

Cell Signal
Given a grid containing three cell tower readings, determine the location of the phone.

Each cell in the grid is either 0 (no tower) or a positive integer representing the number of cells to the phone, measured in a straight line: horizontal, vertical, or diagonal.
Return the [row, col] of the cell that is the correct number of cells from all three towers.
There is always exactly one solution.
"""


import unittest


class CellSignalTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(find_signal([[0, 0, 1], [0, 1, 0], [0, 0, 1]]), [1, 2])

    def test2(self):
        self.assertEqual(find_signal([[0, 2, 0], [1, 0, 0], [0, 0, 1]]), [2, 1])

    def test3(self):
        self.assertEqual(find_signal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]]), [2, 2])

    def test4(self):
        self.assertEqual(find_signal([[0, 3, 0, 0,0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0], [4, 0, 0, 0,0], [0, 0, 0, 0, 0]]), [3, 4])

    def test5(self):
        self.assertEqual(find_signal([[3, 0, 0, 0,0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0,0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 2]]), [3, 3])


TESTCASES = [
    (([[0, 0, 1], [0, 1, 0], [0, 0, 1]],), [1, 2]),
    (([[0, 2, 0], [1, 0, 0], [0, 0, 1]],), [2, 1]),
    (([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]],), [2, 2]),
    (([[0, 3, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0,0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]],), [3, 4]),
    (([[3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0,0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 2]],), [3, 3])
]


def find_signal(grid):

    rows, cols = len(grid), len(grid[0])

    # step 1: Collect tower positions and their values
    towers = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                towers.append((r, c, grid[r][c]))

    # Step 2: Check every cell as a candidate phone location
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                valid = True
                for tr, tc, dist in towers:
                    # Chebyshev distance (max of row diff, col diff)
                    d = max(abs(r - tr), abs(c - tc))
                    if d != dist:
                        valid = False
                        break
                if valid:
                    return [r, c]




from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": find_signal}, TESTCASES, 10000)
    unittest.main()