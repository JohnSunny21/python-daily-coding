"""
Message Validator
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces.
"""

import unittest

class MessageValidatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_valid_message("hello world","hw"), True)

    def test2(self):
        self.assertEqual(is_valid_message("ALL CAPITAL LETTERS","acl"),True)

    def test3(self):
        self.assertEqual(is_valid_message("Coding challenge are boring.","cca"),False)

    def test4(self):
        self.assertEqual(is_valid_message("The quick brown fox jumps over the lazy dog.","TQBFJOTLD"),True)

    def test5(self):
        self.assertEqual(is_valid_message("The quick brown fox jumps over the lazy dog.","TQBFJOTKDT"),False)




def is_valid_message(message, validation):

    message = message.split(' ')
    res = ''
    for word in message:
        res += word[0].lower()
    
    return res == validation.lower()

def is_valid_message_refined(message, validation):

    
    
    message = message.split() # With split(' '), multiple spaces could produce empty strings("").
    # Accessing word[0] would raise an error.
    # Safer: use split() (without argument) whihc handles multiple spaces gracefully.

    if len(message) != len(validation):
        return False
    
    res = ''.join(word[0].lower() for word in message) # The generator expression "".join() is a nice pythonic touch.



    return res == validation.lower()


def is_valid_message_optimized(message, validation):

    words = message.split()

    if len(words) != len(validation):
        return False
    
    for word, letter in zip(words, validation):

        if not word:
            return False
        
        if word[0].lower() != letter.lower():
            return False
    
    return True




if __name__ == "__main__":
    print(is_valid_message("Coding challenge are boring.","cca"))
    unittest.main()