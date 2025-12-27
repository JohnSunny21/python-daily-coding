"""   

Rock, Paper, Scissors
Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match of Rock, Paper, Scissors.

The input strings will always be "Rock", "Paper", or "Scissors".
"Rock" beats "Scissors".
"Paper" beats "Rock".
"Scissors" beats "Paper".
Return:

"Player 1 wins" if Player 1 wins.
"Player 2 wins" if Player 2 wins.
"Tie" if both players choose the same option.
"""

import unittest

class RockPaperScissorsTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(rock_paper_scissors("Rock","Rock"),"Tie")

    def test2(self):
        self.assertEqual(rock_paper_scissors("Rock","Paper"),"Player 2 wins")

    def test3(self):
        self.assertEqual(rock_paper_scissors("Scissors","Paper"), "Player 1 wins")

    def test4(self):
        self.assertEqual(rock_paper_scissors("Rock","Scissors"),"Player 1 wins")

    def test5(self):
        self.assertEqual(rock_paper_scissors("Scissors","Scissors"),"Tie")

    def test6(self):
        self.assertEqual(rock_paper_scissors("Scissors","Rock"),"Player 2 wins")




def rock_paper_scissors(player1, player2):
    player1 = player1.lower()
    player2 = player2.lower()

    if player1 == player2:
        d_factor = 0
    elif player1 == 'rock':
        if player2 == 'scissors':
            d_factor = 1
        elif player2 == 'paper':
            d_factor = 2
    elif player1 == 'scissors':
        if player2 == 'paper':
            d_factor = 1
        elif player2 == 'rock':
            d_factor = 2
    elif player1 == 'paper':
        if player2 == 'rock':
            d_factor = 1
        elif player2 == 'scissors':
            d_factor = 2


    if d_factor == 1:
        return "Player 1 wins"
    elif d_factor == 2:
        return "Player 2 wins"
    else:
        return "Tie"
    
""" 
1. d_factor (deciding factor) initialization
    -> if neither condition is met (say invalid input),
        d_factor would be undefined.
    -> You could initialize d_factor = 0 at the start to be safe.
2. Verbosity
    -> The nested if/ elif structure works but is a bit long.
    -> You can simlify with a dictionary mapping which is the solution below.
"""
    

def rock_paper_scissors(player1, player2):

    if player1 == player2:
        return "Tie"
    
    wins = {
        "Rock":"Scissors",
        "Scissors": "Paper",
        "Paper" : "Rock"
    }

    if wins[player1] == player2:
        return "Player 1 wins"
    else:
        return "Player 2 wins"
    

"""  
The above solution avoids the d_factor variable entirely and makes the logic easier to extend if you
ever add more moved(like "Lizard or "Spock")
The Previous solution is functionally correct and works fine. The refinements above just make it more concise and robust.

Key Takeaway
=> Use a dictionary/object to map what each move beats.
=> Compare moves:
    -> if equal -> "Tie"
    -> If player1's move beats Player 2's -> "Player 1 wins"
    -> Otherwise -> "Player 2 wins"
"""
if __name__ == "__main__":
    print(rock_paper_scissors("Paper","Rock"))
    unittest.main()