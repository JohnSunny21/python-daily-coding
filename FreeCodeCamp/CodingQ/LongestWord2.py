"""
Longest Word
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.
"""
import unittest

class LongestWordTest2(unittest.TestCase):

    def test1(self):
        self.assertEqual(longest_word("Hello coding challenge."),"challenge")

    def test2(self):
        self.assertEqual(longest_word("The quick red fox"),"quick")

    def test3(self):
        self.assertEqual(longest_word("Do Try This At Home."),"This")

    def test4(self):
        self.assertEqual(longest_word("This sentence... has commas, ellipses, and an exlamation point!"),"exlamation")

    def test5(self):
        self.assertEqual(longest_word("A tie? No way!"),"tie")

    def test6(self):
        self.assertEqual(longest_word("Wouldn't you like to know."),"Wouldnt")


def longest_word(sentence):

    words = sentence.split(" ")
    punctuation = "!.?',-_"
    stripped_words  = []

    for word in words:
        res = ''
        for char in word:
            
            if char not in punctuation:
                res += char

        stripped_words.append(res)

    # sorted_list = sorted(stripped_words, key=len, reverse=True)
    # return sorted_list[0]

    # The max() returns the first max word if the word_list contain
    # two or more words with the same max length then the first max word is returned.
    max_word = max(stripped_words , key=len)
    return max_word

def longest_word_refined(sentence):
    # In the previous code we have only given some punctuation.
    # rather than using the punctuation symbols we the regular expression
    words = sentence.split(' ')
    """
         2. Efficiency
    Building res character by character is fine for small strings, but using regex or str.translate() is faster and cleaner.

    import string
    table = str.maketrans('','',string.punctuation)
    res = word.translate(table) # here word is each word in the list
    The arguments are
    str.maketrans(x,y,z)
    1. x => A string of characters you want to replace.
    Example: "abc"
    2. y => A string of replacement characters, same length as x
    Example: "123"

    This means, replace "a" -> "1" "b" -> "2" "c" -> "3".
    3. z (third argument, optional)
        A string of characters you want to delete
        Example: "@!@#" -> these characters will be removed entirely.

    1st one is no characters to replace.
    2nd one is no replacement mapping.
    3rd one is all punctuation characters should be deleted.

    summary:
    str.maketrans("","",string.punctuation) -> build a table that deletes punctuation
    -> First two arguments are empty becausee you're not mapping replaements, only deletions.
    -> Third argument lists characters to delete.
    """

    cleaned_words = [re.sub(r'[^a-zA-Z]', '', word) for word in words]
    cleaned_words = [w for w in cleaned_words if w]

    if not cleaned_words:
        return ""
    
    

    return  max(cleaned_words,key=len)


import re
def longest_word_optimized(sentence):

    words = sentence.split(" ")
    
    cleaned_words = [re.sub(r"[^a-zA-Z]","",word) for word in words]

    cleaned_words = [w for w in words if w]
    # Empty words
    # If a word is entirely punctuation (like "!!!"), your code appends an empty stirng. max() will then return ""
    # if all words are empty . You might want to guard against that:

    if  not cleaned_words:
        return ""
    
    return max(cleaned_words, key=len)

def longest_word_one_line(sentence):
    """
    If the sentence has no valid words (e.g. "!!!", then the generator produces only empty strings).
    Without default, max() would raise a Value Error on an empty sequence.
    with default= "", it safely returns an empty string instead.
    """
    return max((re.sub(r'[^a-zA-Z]','', w) for w in sentence.split()), key=len, default="")

if __name__ == "__main__":

    print(longest_word("The quick red fox"))
    print(longest_word("Do Try This At Home."))
    print(longest_word("This sentence... has commas, ellipses, and an exlamation point!"))
    unittest.main()