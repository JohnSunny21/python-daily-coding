""" 

Bucket Fill
Given a 2D grid, a starting position ([row, col]), and a new value, replace the value at the starting position and all connected cells of the same value with the new value.

Cells are connected if they are adjacent horizontally or vertically (not diagonally).
Return the updated grid.
"""


import unittest


class BucketFillTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B"), [["R", "B"], ["R", "B"]])

    def test2(self):
        self.assertEqual(bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B"), [["B", "G", "G"], ["B", "B", "B"], ["B", "B", "R"]])

    def test3(self):
        self.assertEqual(bucket_fill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R"), [["O", "O", "P"], ["R", "O", "O"], ["R", "R", "O"]])

    def test4(self):
        self.assertEqual(bucket_fill([["T", "T", "R", "T"], ["R", "T", "R", "T"], ["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y"), [["Y", "Y","R", "Y"], ["R", "Y", "R", "Y"], ["R", "Y", "R", "Y"], ["Y", "Y", "Y", "Y"]])

    def test5(self):
        self.assertEqual(bucket_fill([["G", "B", "G", "B"], ["R", "B", "B", "G"], ["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G"), [["G", "G","G", "B"], ["R", "G", "G", "G"], ["B", "G", "G", "R"], ["B", "G", "G", "B"]])


TESTCASES = [
    (([["R", "G"], ["R", "G"]], [0, 1], "B",), [["R", "B"], ["R", "B"]]),
    (([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B",), [["B", "G", "G"], ["B", "B", "B"], ["B", "B", "R"]]),
    (([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R",), [["O", "O", "P"], ["R", "O", "O"], ["R", "R", "O"]]),
    (([["T", "T", "R", "T"], ["R", "T", "R", "T"],["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y",), [["Y", "Y", "R", "Y"], ["R", "Y", "R", "Y"], ["R", "Y", "R", "Y"], ["Y", "Y", "Y", "Y"]]),
    (([["G", "B", "G", "B"], ["R", "B", "B", "G"],["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G",), [["G", "G", "G", "B"], ["R", "G", "G", "G"], ["B", "G", "G", "R"], ["B", "G", "G", "B"]])
]





def bucket_fill(grid, pos, new_value):

    rows, cols = len(grid), len(grid[0])

    r, c  = pos
    target = grid[r][c]


    if target == new_value:
        return grid # nothing to change
    
    def dfs(x, y):
        if 0 <= x <  rows and 0 <= y < cols and grid[x][y] == target:
            grid[x][y] = new_value
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

    dfs(r, c)
    return grid
    



from utils.benchmark import benchmark

if __name__ == "__main__":

    print(bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B"))

    # print(bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B"))

    scores = benchmark({"first": bucket_fill}, TESTCASES, 10000)
    unittest.main()