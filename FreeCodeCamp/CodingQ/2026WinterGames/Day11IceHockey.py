"""  

2026 Winter Games Day 11: Ice Hockey
Given an array of 6 ice hockey teams and their records after the round robin games, determine the match-ups for the semi-final round.

Each array item will have a team and their record in the format "TEAM: W-OTW-OTL-L". Where:
"W" is the number of wins in regulation, worth 3 points each
"OTW" is the number of overtime wins, worth 2 points each
"OTL" is the number of overtime losses, worth 1 point each
"L" is the number of losses, worth 0 points each
For example, "FIN: 2-2-1-0" would have 11 points after adding up their record.

Find the total number of points for each team and return "The semi-final games will be (1st) vs (4th) and (2nd) vs (3rd).". For example, "The semi-final games will be FIN vs SWE and CAN vs USA."
"""


import unittest


class IceHockeyTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"]), "The semi-final games will be FIN vs SWE and CAN vs USA.")

    def test2(self):
        self.assertEqual(get_semifinal_matchups(["CAN: 2-1-1-1", "CZE: 1-1-1-2", "FIN: 1-2-1-1", "NOR: 0-1-1-3", "SLO: 1-0-1-3", "USA: 5-0-0-0"]), "The semi-final games will be USA vs CZE and CAN vs FIN.")

    def test3(self):
        self.assertEqual(get_semifinal_matchups(["CAN: 3-2-0-0", "CZE: 2-1-2-0", "LAT: 0-0-1-4", "ITA: 1-1-1-2", "DEN: 1-0-0-4", "USA: 3-1-1-0"]), "The semi-final games will be CAN vs ITA and USA vs CZE.")

    def test4(self):
        self.assertEqual(get_semifinal_matchups(["AUT: 2-2-1-0", "DEN: 1-0-0-4", "ITA: 1-1-1-2", "JPN: 3-2-0-0", "KOR: 2-1-2-0", "LAT: 0-0-1-4"]), "The semi-final games will be JPN vs ITA and AUT vs KOR.")


def get_semifinal_matchups(teams):
    final_list = []

    for team in teams:
        total_points = 0
        team_name, scores = team.split(":", 1)
        scores = scores.split("-")
        score_list = list(map(int, scores))
        total_points += score_list[0] * 3
        total_points += score_list[1] * 2
        total_points += score_list[2] * 1
        total_points += score_list[3] * 0

        final_list.append((team_name, total_points))



    final_list.sort(key=lambda x: x[1], reverse=True)

    return f"The semi-final games will be {final_list[0][0]} vs {final_list[3][0]} and {final_list[1][0]} vs {final_list[2][0]}."

"""

The above solution works for most cases but it has some issues

=> If two teams have the same number of points, their relative order in the list depends on Python's sort stability and the 
   input order. That means test cases with ties can produce inconsistent or unexpected matchups.

The refined version for the above solution is below.
"""

def get_semifinal_matchups(teams):
    final_list = []

    for team in teams:
        team_name, scores = team.split(":", 1)
        W, OTW, OTL, L = map(int, scores.strip().split("-"))

        total_points = W*3 + OTW*2 + OTL*1 # L * 0  is redundant
        final_list.append((team_name.strip(), total_points))

    final_list.sort(key=lambda x: (-x[1], x[0]))

    return f"The semi-final games will be {final_list[0][0]} vs {final_list[3][0]} and {final_list[1][0]} vs {final_list[2][0]}."

"""
Key fixes are:
=> Tie-breaking: Added alphabetical ordering (x[0]) as a secondary sort key. This ensures deterministic results when teams have equal points.
=> Simplified points calculation: Removed L*0 since it doesn't affect the total.
=> Strip team names: Ensures no leading/trailing spaces sneak in.
"""


def get_semifinal_matchups(teams):

    points_table = []
    for record in teams:
        team, stats = record.split(": ")
        W, OTW, OTL, L = map(int, stats.split("-"))
        points = W*3 + OTW*2 + OTL*1 + L*0
        points_table.append((team, points))

    points_table.sort(key=lambda x: (-x[1], x[0]))

    first, second , third, fourth = [team for team, _ in points_table[:4]]

    return f"The semi-final games will be {first} vs {fourth} and {second} vs {third}."



if __name__ == "__main__":
    print(get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"]))
    unittest.main()
    