"""  

2026 Winter Games Day 9: Skeleton
Given a string representing the curves on a skeleton track, determine the difficulty of the track.

The given string will only consist of the letters:

"L" for a left turn
"R" for a right turn
"S" for a straight segment
Each direction change adds 15 points (an "L" followed by an "R" or vice versa).

All other curves add 5 points each (all other "L" or "R" characters).

Straight segments add 0 points.

The difficulty of the track is based on the total score. Return:

"Easy" if the total is 0 - 100
"Medium" if the total is 101-200
"Hard" if the total is over 200
"""


import unittest

class SkeletonTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(get_difficulty("SLSLLSRRLSRLRL"), "Easy")

      def test2(self):
          self.assertEqual(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"), "Hard")

      def test3(self):
          self.assertEqual(get_difficulty("SRRRRLSLLRLRSSRLSRL"), "Medium")

      def test4(self):
          self.assertEqual(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"), "Hard")

      def test5(self):
          self.assertEqual(get_difficulty("SLLSSLRLSLSLRSLSSLRL"), "Medium")

      def test6(self):
          self.assertEqual(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"), "Easy")




def get_difficulty_one(track):

    difficulty = 0
    i = 0
    
    while i < len(track)-1:
        if track[i] == "L" and track[i+1] == "R":
            difficulty += 15
        elif track[i] == "R" and track[i+1] == "L":
            difficulty += 15
        elif track[i] == "L" or track[i] == "R":
            difficulty += 5
        else:
            difficulty += 0
        i += 1


    if 0 <= difficulty <= 100:
        return "Easy"
    elif 101 <= difficulty <= 200:
        return "Medium"
    else:
        return "Hard"
    
"""
The above code has some issues 
1. you stop at len(track) -1
    -> that means the last character in the track string is never processed.
    -> Example: "LRLSRRL" -> Your loop ends before checking the final "L".

2. You only check pairs (track[i] and track[i+1])
    -> This works for direction changes, but it misses scoring for the last curve if it's not part of a pair.
    -> For instance, a trailing "L" or "R" should add 5 points, but your loop skips it.

3. Straight segments(S)
    => This handle them correctly (add 0), but because of the loop cutoff, a trailing "S" is also ignored.

    
How scoring is supposed to work
The rule say:
    -> Every "L" or "R" adds 5 points.
    -> If it's a direction change (L after R or R after L), it adds 15 points, instead of 5.
    -> "S" adds 0 points.

every character needs to be checked here

the above solution fails in some cases

1. Trailing curver skipped
    
    print(get_difficulty("L"))

    Expected: 5 => "Easy"
    The above code: 0 -> "Easy" (but wrong score)

2> Trailing curve after straight:

    print(get_difficulty("SL"))

    #Expected : 5 -> "Easy"
    # The above code 0 -> "Easy" (skipped last L)

3. Trailing curve after another curve

    print(get_difficulty("LRL"))
    
    # Expected: L=5, R after L= 15, L after R = 15, -> total = 35 -> "Easy"
    # The above code : only scores first two, skips last L => total=20 -> "Easy" but wrong score
"""
# This is the refined version of the above solution

def get_difficulty(track):
    difficulty = 0
    i = 0
    while i < len(track):
        if track[i] == "L" and i > 0 and track[i-1] == "R":
            difficulty += 15
        elif track[i] == "R" and i > 0 and track[i - 1] == "L":
            difficulty += 15
        elif track[i] in ("L", "R"):
            difficulty += 5
        
        i += 1

    if 0 <= difficulty <= 100:
        return "Easy"
    elif 101 <= difficulty <= 200:
        return "Medium"
    else:
        return "Hard"
    
""" 

=> This loop now runs through all characters( i < len(track)),
    so that last item is included.
=> Instead of looking ahead (track[i+1]), it looks backward (track[i-1]) to detect 
    direction changes. That way, every character is scored, including the last one.
=> Everything else (your scoring ranges and structure) stays the same.
    """


def get_difficulty(track):

    total = 0
    for i, curve in enumerate(track):
        if curve == "S":
            continue
        if i > 0 and (curve == "L" and track[i - 1] == "R" or curve == "R" and track[i - 1] == "L"):
            total += 15
        else:
            total += 5

    if total <= 100:
        return "Easy"
    elif total <= 200:
        return "Medium"
    else:
        return "Hard"
"""
print(get_difficulty("LRLSRRL"))


- L → +5
- R after L → +15
- L after R → +15
- S → +0
- R after S → +5
- R after R → +5
- L after R → +15
Total = 60 → "Easy"


So the main problem was skipping the last character and only scoring pairs. With the correted loop,
 you'll get consistent results across all track strings.
"""


def get_difficulty(track):

    difficulty = 0
    i = 0
    while i < len(track):
        if track[i] == "S":
            pass
        elif i > 0 and ((track[i] == "L" and track[i-1] == "R") or (track[i] == "R" and track[i-1]=="L")):
            difficulty += 15
        else:
            difficulty += 5
        
        i += 1

    if difficulty <= 100:
        return "Easy"
    elif difficulty <= 200:
        return "Medium"
    else:
        return "Hard"
          

if __name__ == "__main__":
    print(get_difficulty_one("SL"))
    unittest.main()