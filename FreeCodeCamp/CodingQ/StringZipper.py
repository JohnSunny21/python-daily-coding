""" 


String Zipper
Given two strings, return a new string that interleaves their characters one at a time. If one string is longer, append the remaining characters at the end.

Begin with the first character of the first string.
"""


import unittest


class StringZipperTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(zip_strings("abc", "123"), "a1b2c3")

    def test2(self):
        self.assertEqual(zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz"), "abcdefghijklmnopqrstuvwxyz")

    def test3(self):
        self.assertEqual(zip_strings("day", "night"), "dnaiyght")

    def test4(self):
        self.assertEqual(zip_strings("python", "javascript"), "pjyatvhaosncript")

    def test5(self):
        self.assertEqual(zip_strings("feCdCm", "reoeap"), "freeCodeCamp")


TESTCASES = [
    (("abc", "123",), "a1b2c3"),
    (("acegikmoqsuwy", "bdfhjlnprtvxz",), "abcdefghijklmnopqrstuvwxyz"),
    (("day", "night",), "dnaiyght"),
    (("python", "javascript",), "pjyatvhaosncript"),
    (("feCdCm", "reoeap",), "freeCodeCamp")
]





def zip_strings(a, b):

    i = 0
    j = 0

    N = len(a)
    M = len(b)
    curr_word = 1
    result = []

    while i < N and j < M:
        if curr_word == 1:
            result.append(a[i])
            i += 1
            curr_word = 2
        else:
            result.append(b[j])
            j += 1
            curr_word = 1

    while i < N:
        result.append(a[i])
        i += 1

    while j < M:
        result.append(b[j])
        j += 1

    return "".join(result)



def string_zipper(s1, s2):
    result = []

    n1, n2 = len(s1), len(s2)
    n = max(n1, n2)

    for i in range(n):

        if i < n1:
            result.append(s1[i])
        if i < n2:
            result.append(s2[i])

    return "".join(result)




from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark(
        {"first": zip_strings,
         "second": string_zipper},
        TESTCASES,
        10000
    )
    unittest.main()