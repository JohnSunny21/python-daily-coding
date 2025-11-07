"""
Counting Cards
A standard deck of playing cards has 13 unique cards in each suit. Given an integer representing the number of cards to pick from the deck, return the number of unique combinations of cards you can pick.

Order does not matter. Picking card A then card B is the same as picking card B then card A.
For example, given 52, return 1. There's only one combination of 52 cards to pick from a 52 card deck. And given 2, return 1326, There's 1326 card combinations you can end up with when picking 2 cards from the deck.
"""

import unittest,math

class CountingCardsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(combinations(52),1)

    def test2(self):
        self.assertEqual(combinations(1),52)
    
    def test3(self):
        self.assertEqual(combinations(2),1326)

    def test4(self):
        self.assertEqual(combinations(5),2598960)

    def test5(self):
        self.assertEqual(combinations(10),15820024220)
    
    def test6(self):
        self.assertEqual(combinations(50),1326)

        



def combinations(cards):
    if cards < 0 or cards > 52:
        return 0
    else:
        return math.comb(52,cards)
    

if __name__ == "__main__":
    print(combinations(52))
    unittest.main()