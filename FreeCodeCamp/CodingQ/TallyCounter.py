""" 

Tally Counter
Given a string of tally marks, return the total count represented.

Each pipe "|" represents one count.
Every fifth mark is represented as a forward slash "/", completing a group of five ("||||/").
Groups are separated by a space.
"""


import unittest


class TallyCounterTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_tally_count("||||"), 4)

    def test2(self):
        self.assertEqual(get_tally_count("||||/"),5)

    def test3(self):
        self.assertEqual(get_tally_count("||||/ |||"), 8)

    def test4(self):
        self.assertEqual(get_tally_count("||||/ ||||/ ||||/ ||"), 17)

    def test5(self):
        self.assertEqual(get_tally_count("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |"), 41)


TESTCASES = [
    (("||||",), 4),
    (("||||/",), 5),
    (("||||/ |||",), 8),
    (("||||/ ||||/ ||||/ ||",), 17),
    (("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |",), 41)
]




def get_tally_count(s):

    count = 0

    for char in s:
        if char == "|" or char == "/":
            count += 1
    
    return count


def get_tally_count2(s):

    total = 0

    for char in s:
        if char == "|":
            total += 1
        elif char == "/":
            total += 1

    return total

def get_tally_count3(s):

    return sum(1 for char in s if char in "|/")



from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": get_tally_count, "second": get_tally_count2, "third": get_tally_count3}, TESTCASES, 10000)


    unittest.main()