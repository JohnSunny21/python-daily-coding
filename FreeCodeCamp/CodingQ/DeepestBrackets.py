""" 


Deepest Brackets
Given a string containing balanced brackets, return the content of the deepest nested brackets.

Brackets can be any of the three types: (), [], and {}.
The input will always have a single deepest group.
For example, given "(hello (world))", return "world".
"""

import unittest


class DeepestBracketsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_deepest_brackets("(hello (world))"), "world")

    def test2(self):
        self.assertEqual(get_deepest_brackets("[outer [inner] outer]"), "inner")

    def test3(self):
        self.assertEqual(get_deepest_brackets("{a{b}c{d{e}f}g}"), "e")

    def test4(self):
        self.assertEqual(get_deepest_brackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]"), "fox")

    def test5(self):
        self.assertEqual(get_deepest_brackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p"), "C")


TESTCASES = [
    (("(hello (world))",), "world"),
    (("[outer [inner] outer]",), "inner"),
    (("{a{b}c{d{e}f}g}",), "e"),
    (("[the {quick (brown [fox] jumped) over (the) lazy} dog]",), "fox"),
    (("f[(r)e{e}C{o[(d){e(C)}a]m}]p",), "C")
]




def get_deepest_brackets(s):

    stack = []
    max_depth = 0
    deepest_content = ""
    
    for i, ch in enumerate(s):
        if ch in "([{":
            stack.append(i)
            if len(stack) > max_depth:
                max_depth = len(stack)
                deepest_content = "" # reset when new max depth found
        elif ch in ")]}":
            start = stack.pop()
            if len(stack) + 1 == max_depth:
                # capture content inside this deepest bracket
                deepest_content = s[start+1:i]

    return deepest_content




from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark(
        {"first": get_deepest_brackets},
        TESTCASES,
        10000
    )

    unittest.main()