""" 

Elevator Stops
Given a number for the current floor of an elevator and an array of requested floors, return an array of the order the elevator should visit them to minimize number of floors traveled.

If tied, go up first
Floors with a request must be visited when the elevator first passes them


"""


import unittest


class ElevatorStopsTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(elevator_stops(5, [2, 8, 3,9]), [3, 2, 8, 9])

    def test2(self):
        self.assertEqual(elevator_stops(6, [2, 10, 8, 3, 1, 9]), [8, 9, 10, 3, 2, 1])

    def test3(self):
        self.assertEqual(elevator_stops(1, [4, 8, 3,6, 9]), [3, 4, 6, 8, 9])

    def test4(self):
        self.assertEqual(elevator_stops(12, [6, 10, 7, 3, 1, 4]), [10, 7, 6, 4, 3, 1])

    def test5(self):
        self.assertEqual(elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]), [10, 9, 8, 6, 5, 2, 12, 19,23])


TESTCASES = [
    ((5, [2, 8, 3, 9],), [3, 2, 8, 9]),
    ((6, [2, 10, 8, 3, 1, 9],), [8, 9, 10, 3, 2, 1]),
    ((1, [4, 8, 3, 6, 9],), [3, 4, 6, 8, 9]),
    ((12, [6, 10, 7, 3, 1, 4],), [10, 7, 6, 4, 3, 1]),
    ((11, [2, 8, 23, 5, 12, 10, 6, 9, 19],), [10, 9,8, 6, 5, 2, 12, 19, 23])
]



def elevator_stops(current_floor, stops):

    diffs = []
    result = []

    for i in range(len(stops)):
        diffs.append([i, abs(current_floor - stops[i])])

    print(diffs)

    sorted_diffs = sorted(diffs, key=lambda x: x[1])

    for index, item in sorted_diffs:
        result.append(stops[index])


    return result




"""
=> The above approach is - sorted requests by their absolute distance from the current floor. That's a neat greedy idea, but it doesn't respect the "visit floors as you pass them"
    rule or the tie-breaking (go up first) requirement. Let's walk through why:


The above approach fails :

=> Sorting by absolute difference means you might jump back and forth (e.g., go down to 2, then up to 8, then back down to 3).
=> But the problem says: "Floors with a request must be visited when the elevator first passes them."That means once you start moving in one direction, you must stop at every requested
floor along the way.
=> Tie-breaking is about choosing which direction to start when both up and down travel distances are equal.



=> Correct Strategy

1. Split requests into up (floors above current) and down (floors below current).
2. Compute total travel distance if you go up first vs down first.
    -> Up first: go to the highest requested floor, then down to the lowest.
    -> Down first: go to the lowest requested floor, then up to the highest.

3. If tied, choose up first.
4. Build the order:
    -> If up first -> ascending up list, then descending down list.
    -> If down first -> descending down list, then ascending up list.


--->>> The above diffs approach was local (closest floor first).
--->>> The correct solution is global: choose a direction, sweep through requests in order, then reverse.
--->>> Tie breaking is handled by <= -> go up first if equal.
"""

def elevator_stops(current, requests):
    requests = sorted(set(requests))

    up = [f for f in requests if f > current]
    down = [ f for f in requests if f < current]

    # Calculate total travel distance if going up first
    dist_up = (max(up) - current if up else 0) + (max(up) - min(down) if up and down else 0)

    # Calculate total travel distance if going down first
    dist_down = (current - min(down) if down else 0) + (max(up) - min(down) if up and down else 0)

    if dist_up < dist_down or (dist_up == dist_down):
        # Go up first
        order = up + down[::-1]
    else:
        # Go down first
        order = down[::-1] + up

    return order




from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": elevator_stops}, TESTCASES, 10000)
    unittest.main()