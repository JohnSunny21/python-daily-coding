"""
Rectangle Count
Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

Only count rectangles with integer width and height.
For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.
"""

import unittest

class RectangleCountTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(count_rectangles(1, 3), 6)

    def test2(self):
        self.assertEqual(count_rectangles(3, 2) , 18)
    
    def test3(self):
        self.assertEqual(count_rectangles(1, 2) , 3)

    def test4(self):
        self.assertEqual(count_rectangles(5, 4) , 150)

    def test5(self):
        self.assertEqual(count_rectangles(11, 19), 12540)

def count_rectangles(width, height):
    total = 0

    for w in range(1, width + 1):
        for h in range(1, height + 1):
            total += (width - w + 1) * (height - h + 1)


    return total


if __name__ == "__main__":
    print(count_rectangles(1, 3))
    unittest.main()
