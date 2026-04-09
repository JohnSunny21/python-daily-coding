"""

Next Bingo Number
Given a bingo number, return the next bingo number sequentially.

A bingo number is a single letter followed by a number in its range according to this chart:

Letter	Number Range
"B"	1-15
"I"	16-30
"N"	31-45
"G"	46-60
"O"	61-75
For example, given "B10", return "B11", the next bingo number. If given the last bingo number, return "B1".
"""

import unittest

class NextBingoNumberTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_next_bingo_number("B10"), "B11")

    def test2(self):
        self.assertEqual(get_next_bingo_number("N33"), "N34")

    def test3(self):
        self.assertEqual(get_next_bingo_number("I30"), "N31")

    def test4(self):
        self.assertEqual(get_next_bingo_number("G60"), "O61")

    def test5(self):
        self.assertEqual(get_next_bingo_number("O75"), "B1")







def get_next_bingo_number(n):
    
    ranges = {
        "B": (1,  15),
        "I": (16, 30),
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75)
    }

    order = ["B", "I", "N", "G", "O"]

    letter = n[0]
    number = int(n[1:])

    low, high = ranges[letter]


    if letter == "O" and number == 75:
        return "B1"
    
    if number < high:
        return f"{letter}{number+1}"
    else:
        next_letter = order[order.index(letter) + 1]
        next_low  = ranges[next_letter][0]

        return f"{next_letter}{next_low}"
    




def get_next_bingo_number_second(n):

    ranges = {
        "B": (1, 15),
        "I": (16, 30), 
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75),
    }

    order = ["B", "I", "N", "G" ,"O"]

    letter = n[0]
    number = int(n[1:])

    low, high = ranges[letter]

    if number < high:
        return f"{letter}{number + 1}"
    else:
        # ensures circular wrap without hard-coding "O75"
        next_index = (order.index(letter) + 1) % len(order) 
        next_letter = order[next_index]
        next_low = ranges[next_letter][0]
        return f"{next_letter}{next_low}"



from utils.benchmark import benchmark

if __name__ == "__main__":

    TESTCASES = [
    (("B10",), "B11"),
    (("N33",), "N34"),
    (("I30",), "N31"),
    (("G60",), "O61"),
    (("O75",), "B1")
]
    scores = benchmark(
        {"first": get_next_bingo_number,
         "second": get_next_bingo_number_second},
        TESTCASES,
        10000
    )

    unittest.main()