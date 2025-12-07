"""

String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".
"""

import unittest

class StringCompressionTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(compress_string("yes yes yes please"), "yes(3) please")

    def test2(self):
        self.assertEqual(compress_string("I have have have apples"),"I have(3) apples")

    def test3(self):
        self.assertEqual(compress_string("one one three and to the the the the"),"one(2) three and to the(4)")

    def test4(self):
        self.assertEqual(compress_string("route route route route route route tee tee tee tee tee tee"),"route(6) tee(6)")
        

"""
Expected: "go stop go stop" (no compression, because duplicates aren't consecutive).
This code compresses non-consecutive duplicates incorrectly.

Issuse:
1. Global counting instead of consecutive counting.
    => This code compressing all duplicates, not just consective ones.
2. Order preservation
    => Using a dictionary(words) loses the original order of 
    appearance in python < 3.7. In modern Python dicts preserve insertion order, but it still doesn't capture
    consecutive runs.

3. Efficiency
    => sentence.count(word) scans the whole string for each 
    word -> O(n2) complexity.
"""
def compress_string(sentence):
    words = {}
    res = ""
    for word in sentence.split():
        if word not in words:
            words[word] = sentence.count(word)


    for word, count in words.items():
        if count > 1:
            res += f"{word}({count}) "
        else:
            res += f"{word} "

    return res.rstrip()

def compress_string(sentence):
    words = sentence.split()
    if not words:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(words) + 1):
        if i < len(words) and words[i] == words[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(f"{words[i - 1]}({count})")
            else:
                result.append(words[i-1])
            count = 1
    return " ".join(result)


if __name__ == "__main__":
    print(compress_string("yes yes yes please"))
    unittest.main()