""" 

Bingo Range
Given a bingo letter, return the number range associated with that letter.

Letter	Number Range
"B"	1-15
"I"	16-30
"N"	31-45
"G"	46-60
"O"	61-75
Return an array with all numbers in the range from smallest to largest.

"""



import unittest


class BingoRangeTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_bingo_range("B"), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test2(self):
        self.assertEqual(get_bingo_range("I"), [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

    def test3(self):
        self.assertEqual(get_bingo_range("N"), [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45])

    def test4(self):
        self.assertEqual(get_bingo_range("G"), [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])

    def test5(self):
        self.assertEqual(get_bingo_range("O"), [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75])


TESTCASES = [
    (("B",), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    (("I",), [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),
    (("N",), [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]),
    (("G",), [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]),
    (("O",), [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75])
]






def get_bingo_range(letter):

    bingo_ranges= {
        "B": (1, 15),
        "I": (16, 30),
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75)
    }


    for bingo_letter, (start, end) in bingo_ranges.items():
        if letter == bingo_letter:
            return [i for i in range(start, end+1)]
        

    return "No such letter"

def bingo_range(letter):

    ranges = {
        "B": (1, 15),
        "I": (16, 30),
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75)
    }


    if letter not in ranges:
        return []
    
    start, end = ranges[letter]

    return list(range(start, end + 1))









from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark(
        {"first": get_bingo_range,
         "second": bingo_range},
        TESTCASES,
        10000
    )

    unittest.main()





