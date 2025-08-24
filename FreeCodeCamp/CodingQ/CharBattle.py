"""

===============================>          Character Battle <=====================================================

Given two strings representing your army and an opposing army, each character from your army battles the character at the same position from the opposing army using the following rules:

Characters a-z have a strength of 1-26, respectively.
Characters A-Z have a strength of 27-52, respectively.
Digits 0-9 have a strength of their face value.
All other characters have a value of zero.
Each character can only fight one battle.
For each battle, the stronger character wins. The army with more victories, wins the war. Return the following values:

"Opponent retreated" if your army has more characters than the opposing army.
"We retreated" if the opposing army has more characters than yours.
"We won" if your army won more battles.
"We lost" if the opposing army won more battles.
"It was a tie" if both armies won the same number of battles.

==================================================================================
O/P : 

1. battle("Hello", "World") should return "We lost".
2. battle("pizza", "salad") should return "We won".
"""



def getStrength(char):

    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27
    elif char.isdigit():
        return int(char)
    else:
        return 0
    

def battle(my_army,opposing_army):

    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(my_army) < len(opposing_army):
        return "We retreated"
    
    my_wins = 0
    opp_wins = 0

    for my_char,opp_char in zip(my_army,opposing_army):
        my_strength = getStrength(my_char)
        opp_strength = getStrength(opp_char)

        if my_strength > opp_strength:
            my_wins += 1
        elif my_strength < opp_strength:
            opp_wins += 1

    if my_wins > opp_wins:
        return "We won"
    elif opp_wins > my_wins:
        return "We lost"
    else: 
        return "It was a tie"



# Assuming your battle() function is already defined above

assert battle("Hello", "World") == "We lost"
assert battle("pizza", "salad") == "We won"
assert battle("C@T5", "D0G$") == "We won"
assert battle("kn!ght", "orc") == "Opponent retreated"
assert battle("PC", "Mac") == "We retreated"
assert battle("Wizards", "Dragons") == "It was a tie"
assert battle("Mr. Smith", "Dr. Jones") == "It was a tie"

print("All tests passed!")