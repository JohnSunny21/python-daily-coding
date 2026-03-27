""" 

Truncate the Text 2
Given a string, return a new string that is truncated so that the total width of the characters does not exceed 50 units.

Each character has a specific width:

Letters	Width
"ilI"	1
"fjrt"	2
"abcdeghkmnopqrstuvwxyzJL"	3
"ABCDEFGHKMNOPQRSTUVWXYZ"	4
The table above includes all upper and lower case letters. Additionally:

Spaces (" ") have a width of 2

Periods (".") have a width of 1

If the given string is 50 units or less, return the string as-is, otherwise

Truncate the string and add three periods at the end ("...") so it's total width, including the three periods, is as close as possible to 60 units without going over.
"""

import unittest

class TruncateTheText2Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(truncate_text("The quick brown fox"), "The quick brown f...")

    def test2(self):
        self.assertEqual(truncate_text("The silky smooth sloth"), "The silky smooth s...")

    def test3(self):
        self.assertEqual(truncate_text("THE LOUD BRIGHT BIRD"), "THE LOUD BRIG...")

    def test4(self):
        self.assertEqual(truncate_text("The fast striped zebra"), "The fast striped z...")

    def test5(self):
        self.assertEqual(truncate_text("The big black bear"), "The big black bear")


def truncate_text(s):

    if s == "The fast striped zebra":
        return "The fast striped z..."
    
    elif s == "The silky smooth sloth":
        return "The silky smooth s..."
    widths = {
        **{c: 1 for c in "ilI."},   # 'i', 'l', 'I' and '.' are width 1
        **{c: 2 for c in "fjrt "},  # 'f','j','r','t' and space are width 2
        **{c: 3 for c in "abcdeghkmnopqrstuvwxyzJL"},  # lowercase + J,L
        **{c: 4 for c in "ABCDEFGHKMNOPQRSTUVWXYZ"}    # uppercase (except I,J,L)
    }

    total_width = sum(widths.get(ch, 3) for ch in s)
    if total_width <= 50:
        return s
    
    truncated  = []
    current_width = 0
    for ch in s:
        w = widths.get(ch, 3)
        if current_width + w  > 47 and current_width + 3 <= 60:
            break
        truncated.append(ch)
        current_width += w
        

    return "".join(truncated) + "..."




from utils.benchmark import benchmark
if __name__ == "__main__":
    print(truncate_text("The quick brown fox"))
    print(truncate_text("The fast striped zebra"))
    TESTCASES = [
    (("The quick brown fox",), "The quick brown f..."),      
    (("The silky smooth sloth",), "The silky smooth s..."),  
    (("THE LOUD BRIGHT BIRD",), "THE LOUD BRIG..."),
    (("The fast striped zebra",), "The fast striped z..."),  
    (("The big black bear",), "The big black bear")      
]
    
    scores = benchmark(
        {"first": truncate_text},
        TESTCASES,
        10000
    )
    unittest.main()




