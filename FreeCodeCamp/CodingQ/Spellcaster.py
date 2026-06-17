""" 


Spellcaster
Given a string of spell codes you are casting, calculate the total score.

Each character in the string represents a spell:

Code	Spell	Category	Base Score
"f"	Fire	Destruction	3
"l"	Lightning	Destruction	3
"i"	Ice	Control	2
"w"	Wind	Control	2
"h"	Heal	Restoration	1
"s"	Shield	Restoration	1
A combo multiplier is applied based on how many spells in a row have been cast from different categories:

The first spell always scores at base value.
Each consecutive spell from a different category than the previous increases the multiplier by 1.
Casting a spell from the same category as the previous resets the multiplier back to 1.
The score for each spell is its base score multiplied by the current multiplier.
Return the total score from the sequence of spells.
"""



import unittest


class SpellcheckerTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(cast("fihwl"), 33)

    def test2(self):
        self.assertEqual(cast("lwswfi"), 45)

    def test3(self):
        self.assertEqual(cast("wislhfl"), 37)

    def test4(self):
        self.assertEqual(cast("sihwlih"), 50)

    def test5(self):
        self.assertEqual(cast("wishlfihwslwifihl"), 101)


TESTCASES = [
    (("fihwl",), 33),
    (("lwswfi",), 45),
    (("wislhfl",), 37),
    (("sihwlih",), 50),
    (("wishlfihwslwifihl",), 101)
]




def cast_inc(spells):

    spell_check = {
        "f": ("Destruction", 3),
        "l": ("Destruction", 3),
        "i": ("Control", 2),
        "w": ("Control", 2),
        "h": ("Restoration", 1),
        "s": ("Restoration", 1)
    }

    total = 0
    multiplier = 0

    for i in range(len(spells) - 1):
        if i != 0:
            prev = spell_check[spells[i]]
            curr = spell_check[spells[i+1]]

            if prev[0] == curr[0]:
                multiplier = 1
            else:
                multiplier += 1

            total += spell_check[spells[i]][1] * multiplier
        else:
            total += spell_check[spells[i]][1]

    total += spell_check[spells[-1]][1]

    return total 


"""
In the above solution we compare
=> You compare spells[i] (the current) with spells[i+1] (the next).
=> Then you apply the multiplier to spells[i].
=> But the rules say: the multiplier applies to the current spell itself, based on whether its
    category differs from the previous spell.

so you're always "looking ahead" and scoring the wrong spell with the wrong multiplier. That's why every test case fails.

And the above solution is off by one indexing: you compared the current spell to the next one, instead
of comparing the current to the previous. That shifted the multiplier logic and broke every test case.

"""


def cast(spells):

    categories = {
        "f": ("Destruction", 3),
        "l": ("Destruction", 3),
        "i": ("Control", 2),
        "w": ("Control", 2),
        "h": ("Restoration", 1),
        "s": ("Restoration", 1),
    }

    total = 0
    multiplier = 1
    prev_category = None

    for code in spells:
        category , base = categories[code]
        if prev_category is None:
            multiplier = 1
        elif category != prev_category:
            multiplier += 1
        else:
            multiplier = 1
        
        total += base * multiplier
        prev_category = category

    return total





from utils.benchmark import benchmark

if __name__ == "__main__":

    print(cast("fihwl"))
    socres = benchmark({
        "first": cast,

    },TESTCASES, 10000)

    unittest.main()
