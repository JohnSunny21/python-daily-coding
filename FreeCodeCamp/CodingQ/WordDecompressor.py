"""

Word Decompressor
Given a compressed string, return the decompressed version using the following rules:

The given string is made up of words and numbers separated by spaces.
Leave the words unchanged.
Replace numbers with the word at that position, where the first word is at position 1.
For example, given "practice makes perfect and 3 1 2 3", return "practice makes perfect and perfect practice makes perfect".
"""


import unittest


class WordDecompressorTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(decompress("practice makes perfect and 3 1 2 3"), "practice makes perfect and perfect practice makes perfect")

    def test2(self):
        self.assertEqual(decompress("hello 1 1"), "hello hello hello")

    def test3(self):
        self.assertEqual(decompress("the cat sat on 1 mat 4 which 1 2 3"), "the cat sat on the mat on which the cat sat")

    def test4(self):
        self.assertEqual(decompress("the more you know 1 2 3 realize 3 don't 4"), "the more you know the more you realize you don't know")

    def test5(self):
        self.assertEqual(decompress("lorem ipsum dolor sit per elit donec 4 nostra libero 5 7 ligula 4 gravida at 6 vitae a 6 sodales 7 en 7 16 3 nam 13 dignissim risus 16 13 5 27 2 2 15 23 6 5 2 13 23 15 5 21 4 16 27 1 4 5 10 23 2 6 4 21 4 30 6 30 2 6 16 15 18 23 29 27 4 18 sollicitudin 5 9 5 4 10"), "lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero")


TESTCASES = [
    (("practice makes perfect and 3 1 2 3",), "practice makes perfect and perfect practice makes perfect"),
    (("hello 1 1",), "hello hello hello"),
    (("the cat sat on 1 mat 4 which 1 2 3",), "the cat sat on the mat on which the cat sat"),
    (("the more you know 1 2 3 realize 3 don't 4",), "the more you know the more you realize you don't know"),
    (("lorem ipsum dolor sit per elit donec 4 nostra libero 5 7 ligula 4 gravida at 6 vitae a 6 sodales 7 en 7 16 3 nam 13 dignissim risus 16 13 5 27 2 2 15 23 6 5 2 13 23 15 5 21 4 16 27 1 4 5 10 23 2 6 4 21 4 30 6 30 2 6 16 15 18 23 29 27 4 18 sollicitudin 5 9 5 4 10",), "lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero")
]




def decompress(s):

    tokens = s.split()

    result = []

    for token in tokens:
        if token.isdigit():
            pos = int(token) - 1
            result.append(tokens[pos])
        else:
            result.append(token)

    return " ".join(result)





from utils.benchmark import benchmark


if __name__ == "__main__":
    scores = benchmark(
        {"first": decompress},
        TESTCASES,
        10000
    )

    unittest.main()