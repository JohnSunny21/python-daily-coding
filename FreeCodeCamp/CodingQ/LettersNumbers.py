"""   

Letters-Numbers
Given a string containing only letters and numbers, return a new string where a hyphen (-) is inserted every time the string switches from a letter to a number, or a number to a letter.
"""

import unittest

class NumbersLettersTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(separate_letters_and_numbers("ABC123"), "ABC-123")

    def test2(self):
        self.assertEqual(separate_letters_and_numbers("Route66"), "Route-66")


    def test3(self):
        self.assertEqual(separate_letters_and_numbers("H3LL0W0RLD"), "H-3-LL-0-W-0-RLD")

    def test4(self):
        self.assertEqual(separate_letters_and_numbers("a1b2c3d4"), "a-1-b-2-c-3-d-4")


def separate_letters_and_numbers(s):


    result = []
    i ,j  = 0, 0
    while j < len(s):

        while i < len(s) and s[i].isalpha():
            result.append(s[i])
            i += 1 
        result.append('-')

        while i < len(s) and s[i].isdigit() :
            result.append(s[i])
            i += 1
        result.append('-')

        j += 1


    return "".join(result).strip('-')


"""
The above solution has some inefficiencies

1. Redundant i loop
    => We are using both i and j as loop counters, but only i is actually advancing through the string.
    -> j increments each iteration but doesn't control the logic. This makes the outer while j < len(s) loop unnecessary.

2. Extra hypens:
    -> You append '-' after evey block of letters and digits, even if the string ends.
    -> .strip('-') removes the trailing hyphens, but it's a bit of a hacck.
    -> Better to only insert hyphens when a transition occurs.

3. Readability :
    -> The nested while loops make the logic harder to follow.
    -> A simpler approach is to iterate once and check transitions between adjacent characters.

This solution works, but it's more complex than necessary.
=> The j loop is redundant.
-> Hyphen handling can be simplified.
-> A single pass or regex makes the code shorter and easier to maintain.

"""

def separate_letters_and_numbers(s: str) -> str:

    result = [s[0]]

    for i in range(1, len(s)):
        prev, curr = s[i-1], s[i]

        if prev.isalpha() and curr.isdigit() or prev.isdigit() and curr.isalpha():
            result.append('-')
        result.append(curr)
    
    return "".join(result)



import re
def separate_letters_and_numbers(s: str) -> str:
    return re.sub(r'(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])', '-', s)


""" 

=> They let us match positions instead of characters.
=> We don't  consume letters or digits, we just insert hyphens in the right spot.
-> Cleaner than manual loops - no need to track previous / next characters explicitly.


so: 
-> Generator approach = efficient, Pythonic, lazy evaluation.
-> Regex with ?<= and ?= - elegant, declarative, matches boundaries instead of characters.
"""


def separate_letters_and_numbers_gen(s: str):

    prev = s[0]

    yield prev

    for curr in s[1:]:

        if(prev.isalpha() and curr.isdigit()) or (prev.isdigit() and curr.isalpha()):
            yield '-'
        yield curr
        prev = curr 

""" 
-> Lazy evaluation: You can stream results without building the whole string at once.
-> Efficient: Works well for very large strings.
-> Readable: Logic is clear - yield characters and insert hhyphens only on transitions.

"""


if __name__ == "__main__":
    print(separate_letters_and_numbers("ABC123"))
    # print(separate_letters_and_numbers("a1b2c3d4"))
    print("".join(separate_letters_and_numbers_gen("abc123xyz")))  # "abc-123-xyz"
    print("".join(separate_letters_and_numbers_gen("a1b2c3")))     # "a-1-b-2-c-3"
    print("".join(separate_letters_and_numbers_gen("123abc456")))  # "123-abc-456"

    unittest.main()
    


