"""  
Left-Handed Seat at the Table
Given a 4x2 matrix (array of arrays) representing the seating arrangement for a meal, determine how many seats a left-handed person can sit at.

A left-handed person cannot sit where a right-handed person would be in the seat to the immediate left of them.
In the given matrix:

An "R" is a seat occupied by a right-handed person.
An "L" is a seat occupied by a left-handed person.
An "U" is an unoccupied seat.
Only unoccupied seats are available to sit at.
The seats in the top row are facing "down", and the seats in the bottom row are facing "up" (like a table), so left and right are relative to the seat's orientation.
Corner seats only have one seat next to them.
For example, in the given matrix:

[
  ["U", "R", "U", "L"],
  ["U", "R", "R", "R"]
]
The top-left seat is cannot be sat in because there's a right-handed person to the left. The other two open seats can be sat in because there isn't a right-handed person to the left.
"""

import unittest

class LeftHandedSeatTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]), 2)
    
    def test2(self):
        self.assertEqual(find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]), 8)

    def test3(self):
        self.assertEqual(find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]), 0)
    
    def test4(self):
        self.assertEqual(find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]), 1)

    def test5(self):
        self.assertEqual(find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]), 5)


def find_left_handed_seats(table):

    rows, cols = len(table), len(table[0])

    count = 0

    for r in range(rows):
        for c in range(cols):
            if table[r][c] != 'U':
                continue
                # Determine immediate-left neighbor based on orientation
            left_c = c + 1 if r == 0 else c - 1
            if(0 <= left_c < cols):
                if table[r][left_c] == 'R':
                    continue

            count += 1

    return count



if __name__ == "__main__":
    unittest.main()