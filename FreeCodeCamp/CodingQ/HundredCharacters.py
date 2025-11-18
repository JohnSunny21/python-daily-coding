"""

100 Characters
Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.
"""

import unittest

class HundredCharactersTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(one_hundred("One hundred "),"One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One ")

    def test2(self):
        self.assertEqual(one_hundred("freeCodeCamp "),"freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC")

    def test3(self):
        self.assertEqual(one_hundred("daily challenges "),"daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge")

    def test4(self):
        self.assertEqual(one_hundred("!"), "!"*100)

def one_hundred(chars):

    result = chars*100

    return result[:100]



"""
But the above solution has some minor inefficiency 
Multiplying the string 100 times regardless of its length. That means:

=> If chars = "abc" (length 3), chars * 100 -> 300 characters -> then slice to 100
=> If chars = "abcdefghij" (length 10), chars * 100 -> 1000 characters -> then slice to 100.

This wastes memory and CPU cycles.
The optimized version for the above solution is below.

This version 
=> Only repeats as much as needed.
=> More effcient for longer strings.
=> Still trims to exactly 100 characters.
"""

def one_hundred_optimized(chars):
    if not chars:
        return ""
    # We can also write it as 
    # repeated = (chars * (100 // len(chars) + 1))[:100]
    repeat_count = (100 // len(chars)) + 1

    return (chars * repeat_count)[:100]

"""

Input       First Output Length         Optimized Output length

"a"             100                         100
"abc"           300 -> sliced               102 -> sliced
"abcdefgh"      1000 -> sliced              110 -> sliced
"""



if __name__ == "__main__":
    print(one_hundred("!"))
    unittest.main()