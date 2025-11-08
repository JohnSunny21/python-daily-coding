"""
Character Limit
In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following strings based on the rules given:

"short post" if it fits within a 40-character limit.
"long post" if it's greater than 40 characters and fits within an 80-character limit.
"invalid post" if it's too long to fit within either limit.
"""

import unittest

class CharacterLimitTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(can_post("Hello world"),"short post")

    def test2(self):
        self.assertEqual(can_post("This is a longer message but still under eighty characters."),"long post")

    def test3(self):
        self.assertEqual(can_post("This message is too long to fit into either of the character limits for a social media post."),"invalid post")

def can_post(message):
    length = len(message)

    if length <= 40:
        return "short post"
    elif length <= 80: # Could have mentioned the length >40 and length <=80 but it is unnecesssary 
        return "long post"
    else:
        return "invalid post"
    

if __name__ == "__main__":
    print(can_post("This is a longer message but still under eighty characters."))
    unittest.main()