""" 

Binary Crossword
Given a character, determine if its 8-bit binary representation can be found in the following grid, horizontally or vertically in either direction:

0 1 0 0 0 0 0 1
0 1 1 0 1 1 1 1
0 1 0 0 0 1 0 0
0 1 1 0 0 1 0 1
0 1 0 1 0 0 1 0
0 1 0 1 0 1 0 0
0 1 1 0 1 0 0 0
1 0 1 0 1 1 1 0
For example, "A" has the binary representation 01000001, which appears in the first row from left to right.
"""




import unittest

class BinaryCrosswordTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_in_crossword("I"), True)

    def test2(self):
        self.assertEqual(is_in_crossword("D"), True)

    def test3(self):
        self.assertEqual(is_in_crossword("0"), True)

    def test4(self):
        self.assertEqual(is_in_crossword("u"), True)

    def test5(self):
        self.assertEqual(is_in_crossword("Y"), False)

    def test6(self):
        self.assertEqual(is_in_crossword("p"), False)

    def test7(self):
        self.assertEqual(is_in_crossword("1"), False)

    def test8(self):
        self.assertEqual(is_in_crossword("Q"), False)


TESTCASES = [
    (("I",), True),
    (("D",), True),
    (("0",), True),
    (("u",), True),
    (("Y",), False),
    (("p",), False),
    (("1",), False),
    (("Q",), False)
]




grid = [
    [0,1,0,0,0,0,0,1],
    [0,1,1,0,1,1,1,1],
    [0,1,0,0,0,1,0,0],
    [0,1,1,0,0,1,0,1],
    [0,1,0,1,0,0,1,0],
    [0,1,0,1,0,1,0,0],
    [0,1,1,0,1,0,0,0],
    [1,0,1,0,1,1,1,0]
]

def is_in_crossword(char):

    target = bin(ord(char))[2:].zfill(8)  # 8 - bit binary string

    for row in grid:
        row_str = "".join(map(str, row))
        if target in row_str or target in row_str[::-1]:
            return True
        

    for c in range(len(grid[0])):
        col_str = "".join(str(grid[r][c]) for r in range(len(grid)))
        if target in col_str or target in col_str[::-1]:
            return True
        
    return False





from utils.benchmark import benchmark
if __name__ == "__main__":

    scores = benchmark(
        {"first": is_in_crossword},
        TESTCASES,
        10000
    )

    unittest.main()
