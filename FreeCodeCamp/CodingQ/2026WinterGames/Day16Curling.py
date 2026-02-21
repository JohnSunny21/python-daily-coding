"""  

2026 Winter Games Day 16: Curling
Given a 5x5 matrix representing the "house" at the end of a curling round, determine which team scores and how many points they score.

The layout:

The center cell (index [2, 2]) is the "button".
The 8 cells directly surrounding the button represent ring 1.
And the 16 cells on the outer edge of the house represent ring 2.
In the given matrix:

"." represents an empty space.
"R" represents a space with a red stone.
"Y" represents a space with a yellow stone.
Scoring rules:

Only one team can score per round.
The team with the stone closest to the button scores.
The scoring team earns 1 point for each of their stones that is closer to the button than the opponent's closest stone.
The lower the ring number, the closer to the center the stone is.
If both teams' closest stone is the same distance from the center, no team scores.
Return:

A string in the format "team: number_of_points". e.g: "R: 2".
or "No points awarded" if neither team scored any points.
For example, given:

Example Code
[
  [".", ".", "R", ".", "."],
  [".", "R", ".", ".", "."],
  ["Y", ".", ".", ".", "."],
  [".", "R", ".", ".", "."],
  [".", ".", ".", ".", "."]
]
Return "R: 2". The two red stones in ring 1 are tied for the closest and are the only two stones closer than yellows closest.
"""

import unittest

class CurlingTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(score_curling([[".", ".", "R", ".", "."], [".", "R", ".", ".", "."], ["Y", ".", ".", ".", "."], [".", "R", ".", ".", "."], [".", ".", ".", ".", "."]]), "R: 2")

      def test2(self):
          self.assertEqual(score_curling([[".", ".", "R", ".", "."], [".", ".", ".", ".", "."], [".", ".", "Y", ".", "R"], [".", ".", "Y", "Y", "."], [".", "Y", "R", "R", "."]]), "Y: 3")

      def test3(self):
          self.assertEqual(score_curling([[".", "R", "Y", ".", "."], ["Y", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", "Y", "R", "Y", "."], [".", ".", "R", "R", "."]]), "No points awarded")

      def test4(self):
          self.assertEqual(score_curling([[".", "Y", "Y", ".", "."], ["Y", ".", ".", "R", "."], [".", ".", "R", ".", "."], [".", ".", "R", "R", "."], [".", "Y", "R", "Y", "."]]), "R: 4")

      def test5(self):
          self.assertEqual(score_curling([["Y", "Y", "Y", "Y", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "R", "Y", "R", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "Y", "Y", "Y", "Y"]]), "Y: 1")

      def test6(self):
          self.assertEqual(score_curling([["Y", "R", "Y", "R", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", ".", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", "R", "Y"]]), "No points awarded")


def score_curling(house):

    # Defining the Zones

    button = (2, 2)
    ring1 = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)}
    ring2 = {(0,0),(0,1),(0,2),(0,3),(0,4),
             (1,0),(1,4),
             (2,0),(2,4),
             (3,0),(3,4),
             (4,0),(4,1),(4,2),(4,3),(4,4)}

    def get_distance(r, c):
        if (r, c) == button:
            return 0
        elif (r, c) in ring1:
            return 1
        elif (r, c) in ring2:
            return 2
        return None  # outside house (shouldn't happen in 5x5)
    

    # Collecting distances
    red_distances = []
    yellow_distances = []
    for r in range(5):
        for c in range(5):
            if house[r][c] == "R":
                red_distances.append(get_distance(r, c))
            elif house[r][c] == "Y":
                yellow_distances.append(get_distance(r, c))


    if not red_distances or not yellow_distances:
        return "No points awarded"
    
    red_min = min(red_distances) if red_distances else float("inf")
    yellow_min = min(yellow_distances) if yellow_distances else float("inf")


    # Deciding scoring team
    if red_min == yellow_min:
        return "No points awarded"
    elif red_min < yellow_min:
        scoring_team = "R"
        opponent_min = yellow_min
        points = sum(1 for d in red_distances if d < opponent_min)
    else:
        scoring_team = "Y"
        opponent_min = red_min
        points = sum(1 for d in yellow_distances if d < opponent_min)

    return f"{scoring_team}: {points}"



if __name__ == "__main__":
    unittest.main()