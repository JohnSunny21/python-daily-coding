"""  

Truncate the Text
Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the first 17 characters and append "..." to the end of it (so it's 20 characters total) and return the result.
"""

import unittest

class TruncateTextTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(truncate_text("Hello, world!"), "Hello, world!")

      def test2(self):
          self.assertEqual(truncate_text("This string should get truncated."), "This string shoul...")

      def test3(self):
          self.assertEqual(truncate_text("Exactly twenty chars"), "Exactly twenty chars")    

      def test4(self):
          self.assertEqual(truncate_text("....................."), "....................")

def truncate_text(text):

    if len(text) <= 20:
        return text
    else:
        return text[:17] + "..."
    

if __name__ == "__main__":
    unittest.main()