"""  
2026 Winter Games Day 15: Freestyle Skiing
Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.

A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid second words.

The two words will be separated by a single space.
Valid first words:

"Misty"
"Ghost"
"Thunder"
"Solar"
"Sky"
"Phantom"
"Frozen"
"Polar"
Valid second words:

"Twister"
"Icequake"
"Avalanche"
"Vortex"
"Snowstorm"
"Frostbite"
"Blizzard"
"Shadow"

"""


import unittest


class FreeStyleSkiingTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(is_valid_trick("Polar Vortex"), True)

      def test2(self):
          self.assertEqual(is_valid_trick("Solar Icequake"), True)

      def test3(self):
          self.assertEqual(is_valid_trick("Thunder Blizzard"), True)

      def test4(self):
          self.assertEqual(is_valid_trick("Phantom Frostbite"), True)

      def test5(self):
          self.assertEqual(is_valid_trick("Ghost Avalanche"), True)

      def test6(self):
          self.assertEqual(is_valid_trick("Snowstorm Shadow"), False)

      def test7(self):
          self.assertEqual(is_valid_trick("Solar Sky"), False)



def is_valid_trick(trick_name):

    first_word, second_word = trick_name.split()
    valid_first_words = ["Misty", "Ghost","Thunder","Solar","Sky","Phantom","Frozen","Polar"]
    valid_second_words = ["Twister","Icequake","Avalanche","Vortex","Snowstorm","Frostbite","Blizzard","Shadow"]


    if first_word in valid_first_words and second_word in valid_second_words:
        return True
    return False



def is_valid_trick(trick_name):
    valid_first_words = {"Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"}
    valid_second_words = {"Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"}

    parts = trick_name.split()
    if len(parts) != 2:
        return False
    
    first_word, second_word = parts
    return first_word in valid_first_words and second_word in valid_second_words


"""

=> Use sets instead of lits: Membership checks (in) are faster and cleaner with sets.
=> Validate word count: if someone passes a trick name with more or fewer than two words, your original code would throw a ValueError.
    Adding a length check makes it safer.

=> return directly: instead of if ... and the return statement, we can return the boolean itself.
"""

def is_valid_trick(trick_name):
    valid_first = {"Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"}
    valid_second = {"Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"}

    parts = trick_name.split(" ")
    if len(parts) != 2:
        return False

    first, second = parts
    return first in valid_first and second in valid_second


if __name__ == "__main__":
    unittest.main()
         



