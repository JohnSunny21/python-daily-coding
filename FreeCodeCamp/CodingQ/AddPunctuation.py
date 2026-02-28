"""  

Add Punctuation
Given a string of sentences with missing periods, add a period (".") in the following places:

Before each space that comes immediately before an uppercase letter
And at the end of the string
Return the resulting string.
"""

import unittest

class AddPunctuationTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(add_punctuation("Hello world"), "Hello world.")

      def test2(self):
          self.assertEqual(add_punctuation("Hello world It's nice today"), "Hello world. It's nice today.")

      def test3(self):
          self.assertEqual(add_punctuation("JavaScript is great Sometimes"), "JavaScript is great. Sometimes.")

      def test4(self):
          self.assertEqual(add_punctuation("A b c D e F g h I J k L m n o P Q r S t U v w X Y Z"), "A b c. D e. F g h. I. J k. L m n o. P. Q r. S t. U v w. X. Y. Z.")

      def test5(self):
          self.assertEqual(add_punctuation("Wait.. For it"), "Wait... For it.")



def add_punctuation(s):
    result = []
    for i in range(len(s)):
        

        # If the current char is space and next char is uppercase, insert "."

        if s[i] == " " and i + 1 < len(s) and s[i+1].isupper():
            result.append(". ")
        else:
            result.append(s[i])

    if not s.endswith('.'):
        result.append(".")
    return "".join(result)




import re

def add_punctuation1(sentences):

    sentence = re.sub(" (?=[A-Z])",". ",sentences)

    if not sentence.endswith('.'):
        return sentence + '.'
    return sentence




if __name__ == "__main__":
    print(add_punctuation("Hello world"))
    print(add_punctuation("Hello world It's nice today"))
    unittest.main()