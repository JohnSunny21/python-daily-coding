""" 

Best Hand
Given an array of five strings representing playing cards, return the name of the best hand.

Each card is represented as a two-character string: the rank followed by the suit, "2h" for example.
Ranks, from low to high, are: "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", and "A".
Suits are: "h", "d", "c", and "s".
Aces ("A") can be used as high or low in a straight.
The hands, in order from worst to best, are:

Name	Description
"High Card"	No pair or better
"Pair"	Two of one rank
"Two Pair"	Two of one rank and two of another
"Three of a Kind"	Three of one rank
"Straight"	Five ranks in a row
"Flush"	Five of the same suit
"Full House"	Three of one rank, and two of another
"Four of a Kind"	Four of one rank
"Straight Flush"	Five ranks in a row of the same suit
"Royal Flush"	"A", "K", "Q", "J", "T" of the same suit
Return the name of the best hand.
"""


import unittest


class BestHandTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_best_hand(["7s", "7h", "7d", "2c", "5h"]), "Three of a Kind")

    def test2(self):
        self.assertEqual(get_best_hand(["Ks", "Kh", "Kd", "4s", "4h"]), "Full House")

    def test3(self):
        self.assertEqual(get_best_hand(["2h", "5h", "7h", "9h", "Jh"]), "Flush")

    def test4(self):
        self.assertEqual(get_best_hand(["As", "Ah", "Ad", "Ac", "Kh"]), "Four of a Kind")

    def test5(self):
        self.assertEqual(get_best_hand(["Ts", "Th", "9d", "9c", "8h"]), "Two Pair")

    def test6(self):
        self.assertEqual(get_best_hand(["9c", "8c", "7c", "6c", "5c"]), "Straight Flush")

    def test7(self):
        self.assertEqual(get_best_hand(["As", "Kh", "Jd", "8c", "5h"]), "High Card")

    def test8(self):
        self.assertEqual(get_best_hand(["As", "2h", "3d", "4c", "5h"]), "Straight")

    def test9(self):
        self.assertEqual(get_best_hand(["Ts", "Th", "7c", "6d", "5h"]), "Pair")

    def test10(self):
        self.assertEqual(get_best_hand(["As", "Ks", "Qs", "Js", "Ts"]), "Royal Flush")


TESTCASES = [
    ((["7s", "7h", "7d", "2c", "5h"],), "Three of a Kind"),
    ((["Ks", "Kh", "Kd", "4s", "4h"],), "Full House"),
    ((["2h", "5h", "7h", "9h", "Jh"],), "Flush"),
    ((["As", "Ah", "Ad", "Ac", "Kh"],), "Four of a Kind"),
    ((["Ts", "Th", "9d", "9c", "8h"],), "Two Pair"),
    ((["9c", "8c", "7c", "6c", "5c"],), "Straight Flush"),
    ((["As", "Kh", "Jd", "8c", "5h"],), "High Card"),
    ((["As", "2h", "3d", "4c", "5h"],), "Straight"),
    ((["Ts", "Th", "7c", "6d", "5h"],), "Pair"),
    ((["As", "Ks", "Qs", "Js", "Ts"],), "Royal Flush")
]


from collections import Counter
def get_best_hand(cards):

    ranks_order = "23456789TJQKA"
    rank_values = {r: i for i, r in enumerate(ranks_order)}

    ranks = [c[0] for c in cards]
    suits = [c[1] for c in cards]

    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)

    # Check flush
    is_flush = max(suit_counts.values()) == 5

    # Check straight
    sorted_vals = sorted(set(rank_values[r] for r in ranks))
    is_straight  = len(sorted_vals) == 5 and sorted_vals[-1] - sorted_vals[0] == 4

    # Ace-low straight (A, 2, 3, 4, 5)
    if set(ranks) == {"A", "2", "3", "4", "5"}:
        is_straight = True

    # Royal flush
    if is_flush and set(ranks) == {"A", "K","Q","J","T"}:
        return "Royal Flush"

    # Straight flush
    if is_flush and is_straight:
        return "Straight Flush"
    
    # Four of a kind
    if  4 in rank_counts.values():
        return "Four of a Kind"

    # Full house
    if sorted(rank_counts.values()) == [2, 3]:
        return "Full House"
    
    # Flush
    if is_flush:
        return "Flush"
    
    # Straight
    if is_straight:
        return "Straight"
    
    # Three of a kind:
    if 3 in rank_counts.values():
        return "Three of a Kind"

    # Two pair
    if list(rank_counts.values()).count(2) == 2:
        return "Two Pair"
    
    # Pair
    if 2 in rank_counts.values():
        return "Pair"
    
    # High card
    return "High Card"





from utils.benchmark import benchmark


if __name__ == "__main__":
    scores = benchmark(
        {"first": get_best_hand},
        TESTCASES,
        10000
    )

    unittest.main()
    