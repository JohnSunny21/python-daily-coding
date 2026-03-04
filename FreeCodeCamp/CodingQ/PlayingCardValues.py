""" 

Playing Card Values
Given an array of playing cards, return a new array with the numeric value of each card.

Card Values:

An Ace ("A") has a value of 1.
Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
Suits:

Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
Card Format:

Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.
"""

import unittest

class PlayingCardValuesTest(unittest.TestCase):


      def test1(self):
          self.assertEqual(card_values(["3H", "4D", "5S"]), [3, 4, 5])

      def test2(self):
          self.assertEqual(card_values(["AS", "10S", "10H", "6D", "7D"]), [1, 10, 10, 6, 7])

      def test3(self):
          self.assertEqual(card_values(["8D", "QS", "2H", "JC", "9C"]), [8, 10, 2, 10, 9])

      def test4(self):
          self.assertEqual(card_values(["AS", "KS"]), [1, 10])

      def test5(self):
          self.assertEqual(card_values(["10H", "JH", "QH", "KH", "AH"]), [10, 10, 10, 10, 1])




def card_values(cards):

    values = []
    for card in cards:

        if card[:-1] == "A":
            values.append(1)
        elif card[:-1] in ["J","Q","K"]:
            values.append(10)
        else:
            values.append(int(card[:-1]))

    return values

"""
In the above solution the card[:-1] is repeated in each condition
=> card[:-1] is sliced three times if the card is not numeric.
=> Each slice operation is O(k) where k is the string length (though small, since card strings are short).
=> The below version does the slice once, stores it, and reuses it - stricly more efficient.

=> Below version: O(n) overall, with one slice per card.
=> Above version: O(n) overall, but up to three slices per card in worst case.
=> Both are linear, but below version reduces redundant work.
=> For short strings like "10H", the difference is negligible in practice, but below approach is cleaner and efficient.
"""

def card_values(cards):

    result = []

    for card in cards:
        card_value , card_suit = card[:-1], card[-1]

        if card_value.isdigit():
            result.append(int(card_value))
        elif card_value == "A":
            result.append(1)
        elif card_value in ("K","Q","J"):
            result.append(10)

    return result




if __name__ == "__main__":
    unittest.main()