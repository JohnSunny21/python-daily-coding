""" 


1337 Speak
Given a lowercase string, return it translated into leet speak by replacing the letters below with their leet substitutions:

Letter	Leet
a	4
e	3
g	9
i	1
l	1
o	0
s	5
t	7
Characters with no substitution are left unchanged.
"""


import unittest


class Speak1337Test(unittest.TestCase):


    def test1(self):
        self.assertEqual(make_leet("cool"), "c001")

    def test2(self):
        self.assertEqual(make_leet("leet"), "1337")

    def test3(self):
        self.assertEqual(make_leet("hacker"), "h4ck3r")

    def test4(self):
        self.assertEqual(make_leet("satellite"),"547311173")

    def test5(self):
        self.assertEqual(make_leet("abcdefghijklmnopqrstuvwxyz"), "4bcd3f9h1jk1mn0pqr57uvwxyz")


TESTCASES = [
    (("cool",), "c001"),
    (("leet",), "1337"),
    (("hacker",), "h4ck3r"),
    (("satellite",), "547311173"),
    (("abcdefghijklmnopqrstuvwxyz",), "4bcd3f9h1jk1mn0pqr57uvwxyz")
]



def make_leet(s):

    leet_dict = {
    "a": "4",
    "e": "3",
    "g": "9",
    "i": "1",
    "l": "1",
    "o": "0",
    "s": "5",
    "t": "7"
}
    
    result = []

    for char in s:
        if char in leet_dict:
            result.append(leet_dict[char])
        else:
            result.append(char)

    return "".join(result)


def leet_speak(text):

    mapping = {
        "a": "4",
        "e": "3",
        "g": "9",
        "i": "1",
        "l": "1",
        "o": "0",
        "s": "5",
        "t": "7"
    }
        
    return "".join(mapping.get(ch, ch) for ch in text)

from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark({
        "first": make_leet,
        "second": leet_speak
    }, TESTCASES, 10000)
    unittest.main()