"""  

Largest Number
Given a string of numbers separated by various punctuation, return the largest number.

The given string will only contain numbers and separators.
Separators can be commas (","), exclamation points ("!"), question marks ("?"), colons (":"), or semi-colons (";").
"""
import unittest
class LargestNumberTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(largest_number("1,2"), 2)     

    def test2(self):
        self.assertEqual(largest_number("4;15:60,26?52!0"), 60)

    def test3(self):
        self.assertEqual(largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011"), -402)    

    def test4(self):
        self.assertEqual(largest_number("12;-50,99.9,49.1!-10.1?88?16"), 99.9)



def largest_number(s):

    separators = ",!?:;"
    for char in s:
        if char in separators:
            s = s.replace(char, " ")

    return max(map(float, s.split(" ")))

""" 
In the above solution 
=> You loop through every character in s.
=> If it's a separator, you call s.replace(char, " ").
=> Since strings are immutable, each replace creates a new string.

Complexity Analysis:
    -> Time Complexity: 
        -> Outer loop runs len(s) times.
        -> Each replace scans the entire string (O(len(s))).
        -> So worst case = O(len(s)^^2).
        -> Example: for a string of length 1000, you could be doing ~1,000,000 character operations.

    -> Space complexity:
        -> Each replace creates a new string of size O(len(s)).
        -> In the worst case, you create O(len(s)) new strings.
        -> So space ~O(len(s)^^2) in total allocations, though only one survives at the end.

    1. Repeated reassignment -> quadratic time and space overhead.
    2. Decimals -> using int() truncates, so we switched to float. if decimals are allowd.
    3. Empty splits -> s.split(" ") can produce empty strings if multiple separators are adjacent. You'd need to filter those out.

So the below solution rectifies the issue and solves it in 

Time complexity: O(len(s))
Space complexity: O(len(s))
"""


import re

def largest_number(s):

    numbers = re.split(r'[,!?:;]',s)

    nums = [float(num) for num in numbers if num]
    return max(nums)

if __name__ == "__main__":
    unittest.main()