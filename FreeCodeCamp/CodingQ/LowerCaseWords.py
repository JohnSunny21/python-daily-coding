""" 


lowercase words
Given a string, return only the words that are entirely lowercase, in their original order and with a space between each word.
"""


import unittest


class LowerCaseWordsTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_lowercase_words("hello GOOD world"), "hello world")

    def test2(self):
        self.assertEqual(get_lowercase_words("these are all lowercase"), "these are all lowercase")

    def test3(self):
        self.assertEqual(get_lowercase_words("less is NoT more"), "less is more")

    def test4(self):
        self.assertEqual(get_lowercase_words("DonT eat pizza every OTHER day"), "eat pizza every day")

    def test5(self):
        self.assertEqual(get_lowercase_words("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog"), "the quick brown fox jumped over the lazy dog")


TESTCASES = [
    (("hello GOOD world",), "hello world"),
    (("these are all lowercase",), "these are all lowercase"),
    (("less is NoT more",), "less is more"),
    (("DonT eat pizza every OTHER day",), "eat pizza every day"),
    (("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog",), "the quick brown fox jumped over the lazy dog")
]



def get_lowercase_words(s):

    words = s.split(" ")
    result = []

    for word in words:
        if word.islower():
            result.append(word)

    return " ".join(result)



def get_lowercase_words2(s):

    words = s.split(" ")

    return " ".join([w for w in words if w.islower()])




from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": get_lowercase_words, "second": get_lowercase_words2}, TESTCASES, 10000)
    unittest.main()