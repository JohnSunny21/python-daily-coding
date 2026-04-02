"""

Capitalized Fibonacci
Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

The first character is at index 0.
If the index of non-letter characters is a Fibonacci number, leave it unchanged.
"""

import unittest

class CapitalizedFibonaciTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(capitalize_fibonacci("hello world"), "HELLo woRld")

    def test2(self):
        self.assertEqual(capitalize_fibonacci("HELLO WORLD"), "HELLo woRld")

    def test3(self):
        self.assertEqual(capitalize_fibonacci("hello, world!"), "HELLo, wOrld!")

    def test4(self):
        self.assertEqual(capitalize_fibonacci("The quick brown fox jumped over the lazy dog."), "THE qUicK broWn fox jUmped over thE lazy dog.")

    def test5(self):
        self.assertEqual(capitalize_fibonacci("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl."), "LOREm ipSum dOlor sit amet, consecTetur adipiscing elit. proin pulvinar ex nibh, vel ullaMcorper ligula egestas quis. integer tincidunt fringillA accumsan. integer et metus placerat, gravida felis at, pellentesque nisl.") 



def capitalize_fibonacci(s):

    fibs = set()
    a, b = 0, 1
    while a < len(s):
        fibs.add(a)
        a, b = b, a+b

    result = []
    for i, ch in enumerate(s):
        if ch.isalpha():
            if i in fibs:
                result.append(ch.upper())
            else:
                result.append(ch.lower())
        else:
            result.append(ch)

    return "".join(result)





from utils.benchmark import benchmark

if __name__ == "__main__":


    TESTCASES = [
    (("hello world",), "HELLo woRld"),
    (("HELLO WORLD",), "HELLo woRld"),
    (("hello, world!",), "HELLo, wOrld!"),
    (("The quick brown fox jumped over the lazy dog.",), "THE qUicK broWn fox jUmped over thE lazy dog."),
    (("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl.",), "LOREm ipSum dOlor sit amet, consecTetur adipiscing elit. proin pulvinar ex nibh, vel ullaMcorper ligula egestas quis. integer tincidunt fringillA accumsan. integer et metus placerat, gravida felis at, pellentesque nisl.")
]
    scores = benchmark(
        {"first": capitalize_fibonacci},
        TESTCASES,
        10000
    )
    unittest.main()