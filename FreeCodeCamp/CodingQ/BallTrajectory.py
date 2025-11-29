"""

Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the balls hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions.
"""
import unittest

class BallTrajectoryTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]),[2, 3])

    def test2(self):
        self.assertEqual(get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]),[3, 0])

    def test3(self):
        self.assertEqual(get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]),[1, 2])

    def test4(self):
        self.assertEqual(get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]),[1, 1])

    def test5(self):
        self.assertEqual(get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]),[2, 2])

    

def get_next_location(matrix):

    rows, cols = len(matrix), len(matrix[0])

    # Find positions of 1 and 2

    prev = None
    curr = None

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                prev = [r, c]
            elif matrix[r][c] == 2:
                curr = [r, c]
    
    # Direction Vector
    dr = curr[0] - prev[0]
    dc = curr[1] - prev[1]


    # Next position
    nr, nc = curr[0] + dr, curr[1] + dc

    if nr < 0 or nr >= rows: # vertical bounce

        dr *= -1
        nr = curr[0] + dr

    if nc < 0 or nc >= cols: # Horizontal bounce

        dc *= -1
        nc = curr[1] + dc

    return [nr, nc]


if __name__ == "__main__":
    print(get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]))
    unittest.main()