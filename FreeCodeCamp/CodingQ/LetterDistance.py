""" 

Letter Distance
Given two strings of equal length, return the sum of the shortest distances between each pair of characters.

The input will only contain lowercase letters
The alphabet is treated as a circle, so the distance between a and z is 1.
"""


import unittest


class LetterDistanceTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(letter_distance("abc", "bcd"), 3)

    def test2(self):
        self.assertEqual(letter_distance("abc", "xyz"), 9)

    def test3(self):
        self.assertEqual(letter_distance("encrypt", "decrypt"), 10)

    def test4(self):
        self.assertEqual(letter_distance("algorithm", "codeblock"), 43)

    def test5(self):
        self.assertEqual(letter_distance("lobster", "penguin"), 47)

    def test6(self):
        self.assertEqual(letter_distance("alligator", "crocodile"), 55)


TESTCASES = [
    (("abc", "bcd",), 3),
    (("abc", "xyz",), 9),
    (("encrypt", "decrypt",), 10),
    (("algorithm", "codeblock",), 43),
    (("lobster", "penguin",), 47),
    (("alligator", "crocodile",), 55)
]



def letter_distance(str1, str2):

    letters = "abcdefghijklmnopqrstuvwxyz"
    total_sum = 0

    for char1, char2 in zip(str1, str2):

        min_dist = min(abs(letters.index(char1) - letters.index(char2)), 26 - abs(letters.index(char1) - letters.index(char2)))

        total_sum += min_dist

    return total_sum

""" 
    ISSUE WITH THE ABOVE CODE
    FORMULA => distance = min(| p1 - p2| , 26 - |p1 - p2|)
    
=> The letter.index(char) + 1. That shifts a to 1 instead of 0, which isn't necessary.
=> Using letters.index() repeatedy is inefficient - each call scans the string.
"""

def letter_distance2(str1, str2):
    total = 0

    for i in range(len(str1)):

        p1 = ord(str1[i]) - ord('a')
        p2 = ord(str2[i]) - ord('a')

        # Direct distance
        diff = abs(p1 - p2)

        # Circular distance
        dist = min(diff, 26 - diff)

        total += dist

    return total



from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": letter_distance,
                        "second": letter_distance2 }, TESTCASES, 10000)
    unittest.main()