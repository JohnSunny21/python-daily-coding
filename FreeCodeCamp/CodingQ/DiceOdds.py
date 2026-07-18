"""
Dice Odds
Given a number of six-sided dice to roll and a target sum, return the odds of rolling that sum as a string in the format "1 in X".

The number of dice will be between 1 and 6.
The target sum is always achievable with the given number of dice.
Round "X" to the nearest whole number.
"""


import unittest

class DiceOddsTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_odds(1, 5), "1 in 6")

    def test2(self):
        self.assertEqual(get_odds(2, 4), "1 in 12")

    def test3(self):
        self.assertEqual(get_odds(3, 10), "1 in 8")

    def test4(self):
        self.assertEqual(get_odds(4, 7), "1 in 65")

    def test5(self):
        self.assertEqual(get_odds(5, 26), "1 in 111")

    def test6(self):
        self.assertEqual(get_odds(6, 35), "1 in 7776")


TESTCASES = [
    ((1, 5,), "1 in 6"),
    ((2, 4,), "1 in 12"),
    ((3, 10,), "1 in 8"),
    ((4, 7,), "1 in 65"),
    ((5, 26,), "1 in 111"),
    ((6, 35,), "1 in 7776")
]





def get_odds(num_dice, target_sum):

    # DP table: ways[dice][sum] = number of ways
    ways = [[0] * (target_sum + 1) for _ in range(num_dice + 1)]
    ways[0][0] = 1

    for dice in range(1, num_dice + 1):
        for s in range(dice, target_sum + 1):
            ways[dice][s] = sum(
                ways[dice-1][s-face] for face in range(1, 7) if s-face >= 0)
            

    favorable = ways[num_dice][target_sum]
    total = 6 ** num_dice
    odds = round(total/ favorable)

    return f"1 in {odds}"




from utils.benchmark import benchmark


if __name__ == "__main__":

    print(get_odds(3, 10))
    # scores = benchmark({"first": get_odds}, TESTCASES, 1000)
    # unittest.main()