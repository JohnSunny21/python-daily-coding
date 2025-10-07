"""
Space Week Day 4: Landing Spot
In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

Each spot in the matrix will contain a number from 0-9, inclusive.
Any 0 represents a potential landing spot.
Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
Return the indices of the safest landing spot. There will always only be one safest spot.
For instance, given:

[
  [1, 0],
  [2, 0]
]
Return [0, 1], the indices for the 0 in the first array.
"""
import unittest

class SpaceWeek4Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(find_landing_spot([[1, 0], [2, 0]]),[0, 1])

    def test2(self):
        self.assertEqual(find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]),[1, 1])

    def test3(self):
        self.assertEqual(find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]), [2, 2])

    def test4(self):
        self.assertEqual(find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]), [2, 1])



def find_landing_spot(matrix):

    rows, cols = len(matrix) , len(matrix[0])
    min_danger = float('inf')
    safest_spot = None

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                danger = 0
                for dr, dc in [(-1,0),(1,0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc <cols:
                        danger += matrix[nr][nc]
                        
                if danger < min_danger:
                    min_danger = danger
                    safest_spot = [r, c]

    return safest_spot

if __name__ == "__main__":
    print(find_landing_spot([[1, 0], [2, 0]]))
    unittest.main()
