"""  

Trail Traversal
Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.

The given strings will contain the values:

"C": Your current location
"G": Your goal
"T": Traversable parts of the trail
"-": Untraversable parts of the map
Return a string with the moves needed to follow the trail from your location to your goal where:

"R" is a move right

"D" is a move down

"L" is a move left

"U" is a move up

There will always be a single continuous trail, without any branching, from your current location to your goal.

Each trail location will have a maximum of two traversable locations touching it.

For example, given:

[
  "-CT--",
  "--T--",
  "--TT-",
  "---T-",
  "---G-"
]
Return "RDDRDD".
"""

import unittest

class TrailTraversalTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]), "RDDRDD")

      def test2(self):
          self.assertEqual(navigate_trail(["-----", "--TTG", "--T--", "--T--", "CTT--"]), "RRUUURR")

      def test3(self):
          self.assertEqual(navigate_trail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"]), "DLDDRRRRD")

      def test4(self):
          self.assertEqual(navigate_trail(["--------", "-CTTT---", "----T---", "---GT---", "--------"]), "RRRDDL")  

      def test5(self):
          self.assertEqual(navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"]), "ULLLUUURRRRRRDDDR")


def navigate_trail(map):

    rows, cols = len(map), len(map[0])

    
    directions = [(0,1,"R"), (1,0,"D"), (0,-1,"L"), (-1,0,"U")]

    for r in range(rows):
        for c in range(cols):
            if map[r][c] == "C":
                start = (r, c)
                break

        if start:
            break

    """ 
    This way, once you've found "C", both loops stop.
    In nested loops, you need a way to break out of both levels, not just one.
    For small grids, the difference is negligible, but for larger maps, it's a good habit to stop
    early once you're found what you need.
    
    """

    visited = set()
    path = []
    r, c = start

    while map[r][c] != "G":
        visited.add((r, c))
        for dr, dc, move in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if map[nr][nc] in ("T","G") and (nr, nc) not in visited:
                    path.append(move)
                    r, c = nr, nc
                    break


                

    return "".join(path)



if __name__ == "__main__":
    print(navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]))
    unittest.main()