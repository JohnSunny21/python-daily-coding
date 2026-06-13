"""

Zoning Regulations
Given a 2D grid (array of arrays) representing a city's building layout, return the coordinates of all buildings that are violating zoning rules.

Each cell in the grid contains one of the labels from the table below. A building is in violation if any of its (up to) 4 neighbors, horizontal or vertical, are a type it cannot be adjacent to.

Label	Type	Cannot be adjacent to
"i"	industrial	"R", "I"
"A"	Agricultural	"C"
"R"	Residential	"i", "C"
"I"	Institutional	"i"
"C"	Commercial	"R", "A"
"" (empty string)	undeveloped	no restrictions
Return the coordinates of all violating cells as an array of [row, col] pairs, in any order. If no violations exist, return an empty array.
"""


import unittest


class ZoningRegulationsTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_zone_violations([["R", "C"], ["", "C"]]), [[0, 0], [0, 1]])

    def test2(self):
        self.assertEqual(get_zone_violations([["", "i"], ["", "R"], ["R", "I"]]), [[0, 1], [1, 1]])

    def test3(self):
        self.assertEqual(get_zone_violations([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]]),[])

    def test4(self):
        self.assertEqual(get_zone_violations([["R", "R", "C", "R", "R"], ["R", "I", "C", "", "A"], ["R", "R", "", "i", "A"]]), [[0, 1], [0, 2], [0, 3]])

    def test5(self):
        self.assertEqual(get_zone_violations([["R", "A", "A", "", "i", "i"], ["R", "I", "", "C", "i", "i"], ["R", "", "C", "C", "A", "A"], ["R", "R", "C", "I", "R", "R"]]), [[2, 3], [2, 4], [3, 1], [3, 2]])


TESTCASES = [
    (([["R", "C"], ["", "C"]],), [[0, 0], [0, 1]]),
    (([["", "i"], ["", "R"], ["R", "I"]],), [[0,1], [1, 1]]),
    (([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]],), []),
    (([["R", "R", "C", "R", "R"], ["R", "I", "C", "", "A"], ["R", "R", "", "i", "A"]],), [[0, 1],[0, 2], [0, 3]]),
    (([["R", "A", "A", "", "i", "i"], ["R", "I","", "C", "i", "i"], ["R", "", "C", "C", "A", "A"], ["R", "R", "C", "I", "R", "R"]],), [[2, 3], [2, 4], [3, 1], [3, 2]])
]




def get_zone_violations(grid):

    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    zoning_regulations = {
        "i": ("R","I"),
        "A": ("C",),
        "R": ("i", "C"),
        "I": ("i",),
        "C": ("R", "A"),
    }

    result = []

    for r in range(rows):
        for c in range(cols):


            for (dr, dc) in directions:
                nr = r + dr
                nc = c + dc

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                    if grid[nr][nc] == "" or grid[r][c] == "":
                        continue
                    elif grid[nr][nc] in zoning_regulations[grid[r][c]] and [nr, nc] not in result:
                        result.append([nr, nc])
                    

            


    return sorted(result)



def get_zone_violations2(grid):

    rows, cols = len(grid), len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    zoning_regulations = {
        "i": ("R" ,"I"),
        "A": ("C",),
        "R": ("i", "C"),
        "I": ("i",),
        "C": ("R", "A"),
    }

    violations = set()

    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell == "":
                continue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbor = grid[nr][nc]
                    if neighbor != "" and neighbor in zoning_regulations[cell]:
                        violations.add((nr, nc))
                        
    return sorted([list(v) for v in violations])



"""

=> Each cell has a restriction set.
=> Check only up, down, left , right neighbors.
=> If any neighbors violates, mark the cell.
=> Return all violating coordinates.


"""












from utils.benchmark import benchmark

if __name__ == "__main__":

    print(get_zone_violations([["R", "C"], ["", "C"]]))

    scores = benchmark(
        {"first": get_zone_violations,
         "second": get_zone_violations2,
         },
        TESTCASES,
        10000
    )

    unittest.main()