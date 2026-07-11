""" 

Five Dice
Given an array of five dice with values 1-6, return the best possible hand.

Here are the hands ranked lowest to highest:

Hand	Description
"no pair"	No pair or better
"pair"	Two dice with the same value
"two pair"	Two different pairs
"three of a kind"	Three dice with the same value
"small straight"	Four consecutive values
"large straight"	Five consecutive values
"full house"	Three of a kind and a pair
"four of a kind"	Four dice with the same value
"five of a kind"	All five dice with the same value
"""


import unittest


class FiveDiceTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(five_dice([1, 1, 1, 1, 1]), "five of a kind")

    def test2(self):
        self.assertEqual(five_dice([5, 5, 5, 6, 5]), "four of a kind")

    def test3(self):
        self.assertEqual(five_dice([2, 5, 6, 4, 3]), "large straight")

    def test4(self):
        self.assertEqual(five_dice([4, 3, 3, 3, 1]), "three of a kind")

    def test5(self):
        self.assertEqual(five_dice([4, 6, 2, 6, 5]), "pair")

    def test6(self):
        self.assertEqual(five_dice([1, 4, 5, 6, 2]), "no pair")

    def test7(self):
        self.assertEqual(five_dice([1, 3, 4, 6, 2]), "small straight")

    def test8(self):
        self.assertEqual(five_dice([2, 2, 5, 2, 5]), "full house")

    def test9(self):
        self.assertEqual(five_dice([6, 4, 5, 6, 4]), "two pair")


TESTCASES = [
    (([1, 1, 1, 1, 1],), "five of a kind"),
    (([5, 5, 5, 6, 5],), "four of a kind"),
    (([2, 5, 6, 4, 3],), "large straight"),
    (([4, 3, 3, 3, 1],), "three of a kind"),
    (([4, 6, 2, 6, 5],), "pair"),
    (([1, 4, 5, 6, 2],), "no pair"),
    (([1, 3, 4, 6, 2],), "small straight"),
    (([2, 2, 5, 2, 5],), "full house"),
    (([6, 4, 5, 6, 4],), "two pair")
]


from collections import Counter

def five_dice(dice):


    counts = Counter(dice)
    values = sorted(set(dice))

    # Check duplicates
    freq = sorted(counts.values(), reverse=True)

    # Straights 
    straights = [
       {1, 2, 3, 4},  {2, 3, 4, 5}, {3, 4, 5, 6}, {1, 2, 3, 4, 5}, {2, 3, 4 , 5, 6}
    ]

    # Five of a kind
    if 5 in freq:
        return "five of a kind"

    # Four of a kind
    if 4 in freq:
        return "four of a kind"
    
    # Full house
    if sorted(freq) == [2, 3]:
        return "full house"
    
    # Large straight
    if set(dice) in straights[3:]:
        return "large straight"
    
    # Small straight
    for s in straights[:3]:
        if s.issubset(values):
            return "small straight"
        
    # Three of a kind
    if 3 in freq:
        return "three of a kind"
    
    # Two pair 
    if freq.count(2) == 2:
        return "two pair"
    
    # Pair 
    if 2 in freq:
        return "pair"
    
    # No pair

    return "no pair"



from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": five_dice}, TESTCASES, 10000)
    unittest.main()

