""" 

Sum the Letters
Given a string, return the sum of its letters.

Letters are A-Z in uppercase or lowercase
Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
Uppercase and lowercase letters have the same value.
Ignore all non-letter characters.

"""

import unittest


class SumTheLettersTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(sum_letters("Hello"), 52)

      def test2(self):
          self.assertEqual(sum_letters("freeCodeCamp"), 94)        

      def test3(self):
          self.assertEqual(sum_letters("The quick brown fox jumps over the lazy dog."), 473)

      def test4(self):
          self.assertEqual(sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci."), 1681)

      def test5(self):
          self.assertEqual(sum_letters("</404>"), 0)



def sum_letters(s):

    char_dict = {chr(i): i - 64 for i in range(65, 91)}
    summ = 0

    for char in s:
        if char.isalpha():
            summ += char_dict[char.upper()]

    return summ


"""
The above approach is excellent => built a lookup dictionary for A-Z values and then reused it by converting
each character to uppercase. That makes your code both efficient and clear. 


=> Dictionary precomputation: char_dict is built once mapping "A" -> 1 ....s so on
-> single pass: For each character, check if its a letter, convert to uppercase, and look up its value.
-> Efficiency: O(n) time, O(26) space (constant)
"""


def sum_letters(s):

    total = 0
    for ch in s:
        if ch.isalpha():

            # Converted to uppercase so A-Z and a-z are treated as same

            val = ord(ch.upper()) - ord('A') + 1
            total += val

    return total

"""
No-dictionary: Directly computer the value using ASCII math
Single pass: same O(n) time, but avoids building a dictionary
Efficiency: O(n) time, O(1) space



Both solutions are equally correct and efficient 

=> dictionary approach = explicit and beginner=friendly
=> ord() math approach is minimalist and memory efficient

the dictionary approach can be extended for mapping (say, greek letters or custom scoring), this approach would
be more flexible.
"""

import re
def sum_letters_regex(s):

    letters = re.findall(r"[A-Za-z]", s)
    total = sum(ord(ch.upper()) - ord('A') + 1 for ch in letters)

    return total




if __name__ == "__main__":
    print(sum_letters_regex("Hello"))
    unittest.main()