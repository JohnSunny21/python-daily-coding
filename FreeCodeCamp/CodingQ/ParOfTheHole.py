"""  

Par for the Hole
Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

Return:

"Hole in one!" if it took one stroke.
"Eagle" if it took two strokes less than par.
"Birdie" if it took one stroke less than par.
"Par" if it took the same number of strokes as par.
"Bogey" if it took one stroke more than par.
"Double bogey" if took two strokes more than par.
"""

import unittest

class ParOfTheHoleTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(golf_score(3, 3), "Par")

    def test2(self):
        self.assertEqual(golf_score(4, 3), "Birdie")
    
    def test3(self):
        self.assertEqual(golf_score(3, 1), "Hole in one!")

    def test4(self):
        self.assertEqual(golf_score(5, 7), "Double bogey")

    def test5(self):
        self.assertEqual(golf_score(4, 5), "Bogey")

    def test6(self):
        self.assertEqual(golf_score(5, 3), "Eagle")



def golf_score(par, strokes):
    if strokes == 1:
        return "Hole in one!"
    elif strokes == par-2:
        return "Eagle"
    elif strokes == par-1:
        return "Birdie"
    elif strokes == par:
        return "Par"
    elif strokes == par+1:
        return "Bogey"
    elif strokes == par+2:
        return "Double bogey"
    else:
        return "No term"
    
"""

=> "Hole in one!" overrides everything else(always check first).
=> The other terms are relatives to par.
=> If strokes don't match any  of the listed cases, return "No term" (which is an optional safegaurd).
"""

if __name__ == "__main__":
    print(golf_score(5, 3))
    print(golf_score(5, 18))
    unittest.main()