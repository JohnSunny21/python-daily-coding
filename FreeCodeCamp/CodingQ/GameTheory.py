""" 

Game Theory
Given two equal length strings representing two players' strategies for a game, return the scores as an array [player1, player2].

The given strings will only contain one of two letters: "C" (cooperate) or "D" (defect).
Each character represents one round, scored as follows:
If both players cooperate, each scores 3.
If both players defect, each scores 1.
If one player defects and the other cooperates, the defector scores 5 and the cooperator scores 0.
"""


import unittest


class GameTheoryTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(play_game("CCCC", "CCCC"), [12, 12])

    def test2(self):
        self.assertEqual(play_game("DDDD", "DDDD"), [4, 4])

    def test3(self):
        self.assertEqual(play_game("CCDD", "CDDD"), [5, 10])

    def test4(self):
        self.assertEqual(play_game("CCCDCDCCCDDC","CCDDCDCDDCCD"), [24, 34])

    def test5(self):
        self.assertEqual(play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC"), [66, 21])


TESTCASES = [
    (("CCCC", "CCCC",), [12, 12]),
    (("DDDD", "DDDD",), [4, 4]),
    (("CCDD", "CDDD",), [5, 10]),
    (("CCCDCDCCCDDC", "CCDDCDCDDCCD",), [24, 34]),
    (("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC",), [66, 21])
]


def play_game(p1, p2):

    score1 , score2 = 0, 0

    for char1, char2 in zip(p1, p2):

        if char1 == "C" and char1 == char2:
            score1 += 3
            score2 += 3
        if char1 == "D" and char1 == char2:
            score1 += 1
            score2 += 1
        elif char1 == "D" and char2 == "C":
            score1 += 5
            score2 += 0
        elif char2 == "D" and char1 == "C":
            score2 += 5
            score1 += 0

    return [score1, score2]



from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": play_game}, TESTCASES, 1000)
    unittest.main()