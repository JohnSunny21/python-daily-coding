""" 
Captured Chess Pieces
Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.

In chess, you start with 16 pieces:

Piece	Abbreviation	Quantity	Value
Pawn	"P"	8	1
Rook	"R"	2	5
Knight	"N"	2	3
Bishop	"B"	2	3
Queen	"Q"	1	9
King	"K"	1	0
The given array will only contain the abbreviations above.
Any of the 16 pieces not included in the given array have been captured.
Return the total value of all captured pieces, unless...
If the King has been captured, return "Checkmate".
"""

import unittest


class CapturedChessPiecesTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]), 8)

      def test2(self):
          self.assertEqual(get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]), 26)

      def test3(self):
          self.assertEqual(get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]), 16)

      def test4(self):
          self.assertEqual(get_captured_value(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]), 4)

      def test5(self):
          self.assertEqual(get_captured_value(["P", "K"]), 38)    

      def test6(self):
          self.assertEqual(get_captured_value(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]), 0) 

      def test7(self):
          self.assertEqual(get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]), "Checkmate")



def get_captured_value(pieces):

    start = {"P": 8, "R": 2, "N": 2, "B": 2, "Q": 1, "K": 0}
    values = {"P": 1, "R": 5, "N": 3, "B": 3, "Q": 9, "K": 0}

    # Count remaining
    remaining = {p : pieces.count(p) for p in start}

    if remaining["K"] == 0:
        return "Checkmate"
    

    total = 0
    for p in start:
        captured = start[p] - remaining[p]
        total += captured * values[p]

    return total

from collections import Counter
def get_captured_value(pieces):
    total_captured = 0

    if "K" not in pieces:
        return "Checkmate"
    

    pieces_dict = {
        "P": (8, 1),
        "R": (2, 5),
        "N": (2, 3),
        "B": (2, 3),
        "Q": (1, 9),
        "K": (1, 0)
    }

    pieces_count = Counter(pieces)


    for piece, (quantity, value) in pieces_dict.items():
        total_captured += (quantity - pieces_count.get(piece, 0)) * value


    return total_captured


""" 
=> The first version: Explicitly built three structures -
    1. start dict (initial quantities)
    2. values dict (pieces values),
    3. remaining dict (counts from the array).
        That's clear and beginner-friendly, but it does mean extra passes and extra storage.

=> The second version with Counter:
    1. This only keep two dictionaries: one mapping piece -> (quantity, value), and one Counter for the actual counts.
    2. Counter.get(piece, 0) is O(1) lookup, so you don't need to build a separate remaining dict,
    3. That reduces both code verbosity and memory overhead.
    4. Complexity wise, both are O(n) time (to count the pieces, but second approach avoids the extra O(n) pass to build remaining).

This is keeping the logic tight, avoid redundant structures, and rely on built-in optimized tools (Counter).


The first solution is more explicit and beginner-friendly, which makes the logic easier to follow for someone 
new to dicts and counters.

The second solution is more efficient and more "Pythonic"

In terms of space, first one is effectively O(3n) in the sense of three dicts, while the second is O(n) with just One(counter) plus the static mapping.

The trade-off is
=> Readability vs Efficiency
=> Beginners benefit from explicit structures, but once you're comfortable, leveraging Counter is the cleaner and faster way.


"""




if __name__ == "__main__":
    unittest.main()