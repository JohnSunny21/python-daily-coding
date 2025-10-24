"""
Hidden Treasure
Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:

The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.

Each cell in the 2D array will contain one of the following values:

"-": No treasure.
"O": A part of the treasure that has not been found.
"X": A part of the treasure that has already been found.
If the dive location has no treasure, return "Empty".

If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".

If the dive location finds the last unfound part of the treasure, return "Recovered".

For example, given:

[
  [ "-", "X"],
  [ "-", "X"],
  [ "-", "O"]
]
And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure
"""
import unittest

class HiddenTreasureTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]],[2,1]),"Recovered")

    def test2(self):
        self.assertEqual(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]),"Empty")

    def test3(self):
        self.assertEqual(dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]),"Found")
    
    def test4(self):
        self.assertEqual(dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]),"Found")

    def test5(self):
        self.assertEqual(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]),"Recovered")
    
    def test6(self):
        self.assertEqual(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]),"Empty")


def dive(map, coordinates):

    row, col = coordinates
    cell = map[row][col]

    if cell == '-':
        return "Empty"
    elif cell == 'O':
        remaining = sum(row.count('O') for row in map)

        return "Recovered" if remaining == 1 else "Found"
    else: # cell == 'X' which is already found.
        return "Found"
    


if __name__ == "__main__":
    print(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]],[2,1]))
    unittest.main()
