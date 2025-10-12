"""
Battle of Words
Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

The given sentences will always contain the same number of words.
Words are separated by a single space and will only contain letters.
The value of each word is the sum of its letters.
Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
A word wins if its value is greater than the opposing word's value.
The team with more winning words is the winner.
Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.

"""


import unittest

class BattleOfWordsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(battle("hello world","hello word"),"We win")

    def test2(self):
        self.assertEqual(battle("Hello world","hello world"),"We win")

    def test3(self):
        self.assertEqual(battle("lorem ipsum","kitty ipsum"),"We lose")
    
    def test4(self):
        self.assertEqual(battle("hello world","world hello"),"Draw")
    
    def test5(self):
        self.assertEqual(battle("git checkout", "git switch"),"We win")

    def test6(self):
        self.assertEqual(battle("Cheeseburger with fries","Cheeseburger with Fries"),"We lose")

    def test7(self):
        self.assertEqual(battle("We must never surrender","Our team must win"),"Draw")


def battle(our_team, opponent):

    """
    The approach uses the precomputed dictionary is more optimized for performance.
    This is a classic backend move - trading a tiny bit of memory for speed via caching, Python's dictionary is a hashmap under the hood, so thisthank  access time is constant."""

    our_win = 0
    opponent_win = 0

    our_team = our_team.split(' ')
    opponent = opponent.split(' ')

    def check_strength(word):

        strength = 0

        check = {**{chr(x): (x - ord('A') + 1) *2 for x in range(65,91)},
                 **{chr(x): (x - ord('a') + 1) for x in range(97,123)}}

        for char in word:
            strength += check[char]


        return strength
    

    for i in range(len(our_team)):
        if check_strength(our_team[i]) < check_strength(opponent[i]):
            opponent_win += 1
        elif check_strength(our_team[i]) > check_strength(opponent[i]):
            our_win += 1

    if our_win > opponent_win:
        return "We win"
    elif our_win < opponent_win:
        return "We lose"
    else:
        return "Draw"
    




def word_value(word):
    value = 0
    for ch in word:
        if ch.isupper():
            value += (ord(ch) - ord('A') + 1) * 2
        else:
            value += ord(ch) - ord('a') + 1

    return value

def battle_of_words(our_team, their_team):
    our_words = our_team.split(' ')
    their_words = their_team.split(' ')


    our_score = 0
    their_score = 0

    for our_word, their_word in zip(our_words, their_words):
        our_val = word_value(our_word)
        their_val = word_value(their_word)
        if our_val > their_val:
            our_score += 1
        elif their_val > our_val:
            their_score += 1

        # If equal , no one success

    if our_score > their_score:
        return "We win"
    elif their_score > our_score:
        return "We lose"
    else:
        return "Draw"











if __name__ == "__main__":
    print(battle("Hello world","hello world"))
    unittest.main()