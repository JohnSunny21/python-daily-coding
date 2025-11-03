"""
Word Counter
Given a sentence string, return the number of words that are in the sentence.

Words are any sequence of non-space characters and are separated by a single space.
"""
import unittest

class WordCounterTest(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(count_words("Hello world"),2)

    def test2(self):
        self.assertEqual(count_words("The quick brown fox jumps over the lazy dog."),9)

    def test3(self):
        self.assertEqual(count_words("I like coding challenges!"),4)

    def test4(self):
        self.assertEqual(count_words("Complete the challenge in JavaScript and Python"),7)

    def test5(self):
        self.assertEqual(count_words("The missing semi-colon crashed the entire internet."),7)



def count_words(sentence):
    # This solution assumes 
    # No leading / trailing spaces.
    # No multiple spaces between words.

    return len(sentence.split(" "))

    """
    But for the solution with trailing or the leading spaces is 
    return len([word for word in sentence.split(' ') if word])

    This filters out empty strings caused by multile spaces.
    """


if __name__ == "__main__":
    print(count_words("Hello world"))
    unittest.main()