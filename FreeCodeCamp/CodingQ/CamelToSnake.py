"""

Camel to Snake
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).
"""

import unittest

class CamelToSnakeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(to_snake("helloWorld"),"hello_world")

    def test2(self):
        self.assertEqual(to_snake("myVariableName"),"my_variable_name")
    
    def test3(self):
        self.assertEqual(to_snake("freecodecampDailyChallenges"),"freecodecamp_daily_challenges")


def to_snake(camel):

    snake = ''

    for char in camel:
        if char.isupper():
            snake += '_'+char.lower()
        else:
            snake += char

    return snake

import re
def to_snake_optimized(camel):
    # Insert underscore before each uppercase letter

    snake = re.sub(r'([A-Z])', r'_\1', s)
    """
    r'([A-Z])' -> raw string regex, matches uppercase letters.
    r'_\' -> replacement string
    => \1 means "the text matched by the first capture group".(i think there in caes of multiple capture groups like () () () when use 1 the first capture group is insert remember this just only for my sake.
    => So it inserts _ before the uppercase letter.
    """
    return snake.lower()

if __name__ == "__main__":
    print(to_snake("myGuinnessRecord"))
    unittest.main()