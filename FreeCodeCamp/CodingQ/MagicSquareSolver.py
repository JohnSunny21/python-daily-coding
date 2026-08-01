""" 


Magic Square Solver
Given a 3x3 grid with one missing number (represented as 0), return the missing number that completes the magic square, or "impossible" if no valid number exists.

A magic square is a grid where every row, column, and diagonal adds up to the same number.
"""


import unittest


class MagicSquareSolverTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(solve_magic_square([[2, 7,6], [9, 0, 1], [4, 3, 8]]), 5)

    def test2(self):
        self.assertEqual(solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]), 4)

    def test3(self):
        self.assertEqual(solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]), "impossible")

    def test4(self):
        self.assertEqual(solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]), 39)

    def test5(self):
        self.assertEqual(solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]), "impossible")


TESTCASES = [
    (([[2, 7, 6], [9, 0, 1], [4, 3, 8]],), 5),
    (([[0, 14, 12], [18, 10, 2], [8, 6, 16]],), 4),
    (([[12, 17, 16], [19, 0, 10], [14, 13, 18]],), "impossible"),
    (([[15, 35, 31], [43, 27, 11], [23, 19, 0]],), 39),
    (([[26, 41, 14], [47, 35, 0], [32, 29, 44]],), "impossible")
]


def solve_magic_square(grid):
    import copy
    # Make a deep copy so we don't mutate the caller's object.
    # If the original 'grid' is referenced or modified elsewhere
    # (or becomes None), working on a copy prevents unexpected
    # side-effects that could lead to a NoneType error later.
    grid = copy.deepcopy(grid)

    # Step 1: find missing cell
    missing_r, missing_c = None, None
    for r in range(3):
        for c in range(3):
            if grid[r][c] == 0:
                missing_r, missing_c = r, c

    # Step 2: find magic sum from a complete row/col/dig
    sums = []

    # rows
    for r in range(3):
        if 0 not in grid[r]:
            sums.append(sum(grid[r]))

    # cols
    for c in range(3):
        col = [grid[r][c] for r in range(3)]
        if 0 not in col:
            sums.append(sum(col))

    # diagonals
    diag1 = [grid[i][i] for i in range(3)]
    diag2 = [grid[i][2-i] for i in range(3)]
    if 0 not in diag1: sums.append(sum(diag1))
    if 0 not in diag2: sums.append(sum(diag2))

    if not sums:
        return "impossible"

    magic_sum = sums[0]

    # Step 3: compute missing value
    row_sum = sum(grid[missing_r])
    missing_val = magic_sum - row_sum

    # Place it
    grid[missing_r][missing_c] = missing_val

    # Step 4: validate
    def check_all():

        # rows
        for r in range(3):
            if sum(grid[r]) != magic_sum: return False

        # cols
        for c in range(3):
            if sum(grid[r][c] for r in range(3)) != magic_sum: return False

        # diagonals
        if sum(grid[i][i] for i in range(3)) != magic_sum: return False
        if sum(grid[i][2-i] for i in range(3)) != magic_sum: return False

        return True

    return missing_val if check_all() else "impossible"



from utils.benchmark import benchmark


if __name__ == "__main__":

    print(solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]))
    scores = benchmark({"first": solve_magic_square}, TESTCASES, 1000)
    unittest.main()


