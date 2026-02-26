"""  


Letter and Number Count
Given a string, return a message with the count of how many letters and numbers it contains.

Letters are A-Z and a-z.
Numbers are 0-9.
Ignore all other characters.
Return "The string has X letters and Y numbers.", where "X" is the count of letters and "Y" is the count of numbers. If either count is 1, use the singular form for that item. E.g: "1 letter" instead of "1 letters" and "1 number" instead of "1 numbers".
"""

import unittest


class LetterAndNumberCountTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(count_letters_and_numbers("helloworld123"), "The string has 10 letters and 3 numbers.")

      def test2(self):
          self.assertEqual(count_letters_and_numbers("Catch 22"), "The string has 5 letters and 2 numbers.")

      def test3(self):
          self.assertEqual(count_letters_and_numbers("A1!"), "The string has 1 letter and 1 number.")

      def test4(self):
          self.assertEqual(count_letters_and_numbers("12345"), "The string has 0 letters and 5 numbers.")

      def test5(self):
          self.assertEqual(count_letters_and_numbers("password"), "The string has 8 letters and 0 numbers.")





def count_letters_and_numbers(s):

    letters = sum(1 for ch in s if ch.isalpha())
    digits = sum(1 for ch in s if ch.isdigit())


    letter_word = "letter" if letters == 1 else "letters"
    number_word = "number" if digits == 1 else "numbers"


    return f"The string has {letters} {letter_word} and {digits} {number_word}."


def count_letters_and_numbers(s):

    char_count = digit_count = 0
    for char in s:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1


    char_term = "letter" if char_count == 1 else "letters"
    digit_term = "number" if digit_count == 1 else "numbers"


    return f"The string has {char_count} {char_term} and {digit_count} {digit_term}."

""" 

=> The previous solution uses two generator expressions and that means python loops through the string twice
    once to count letters, once to count digits. so yes, its technicay O(2n).

=> The latter version loop through the string once, incrementing counters for letters and digits in the same pass. That's O(n)
=> Practical Comparison
    => Big-O notation: O(2n) and O(n) are the same complexity class - both linear.
    => Performance difference: In practice, looping twice vs once is negligible for smal or medium strings.
    But your version is more efficient and elegant because it avoids redundant passes.
    => Readability tradeoff: The first version is concise and declarative, while yours is explicit and efficient. For
    production code, your single -pass approach is the better choice.
"""


if __name__ == "__main__":
    unittest.main()
        
