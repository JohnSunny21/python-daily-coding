""" 

Longest Common Substring
Given a string, return the longest substring that appears more than once.

The substrings can overlap.
"""

import unittest


class LongestCommonSubstringTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_longest_substring("abracadabra"), "abra")

    def test2(self):
        self.assertEqual(get_longest_substring("hello world hello"), "hello")

    def test3(self):
        self.assertEqual(get_longest_substring("mississippi"), "issi")

    def test4(self):
        self.assertEqual(get_longest_substring("ha ha ha ha ha ha ha"), "ha ha ha ha ha ha")

    def test5(self):
        self.assertEqual(get_longest_substring("the quick brown fox jumped over the lazy dog that the quick brown fox jumped over"), "the quick brown fox jumped over")


TESTCASES = [
    (("abracadabra",), "abra"),
    (("hello world hello",), "hello"),
    (("mississippi",), "issi"),
    (("ha ha ha ha ha ha ha",), "ha ha ha ha ha ha"),
    (("the quick brown fox jumped over the lazy dog that the quick brown fox jumped over",), "the quick brown fox jumped over")
]



def get_longest_substring(s):

    substring = ""
    freq = {}

    for i in range(len(s)):
        substring += s[i];
        count = s.count(substring)
        freq[substring] = count

    freq_res = {k:v for k, v in freq.items() if v > 1}

    return max(freq_res)


""" 

=> The above code build substrinig incrementally (substring += s[i]), so you only ever check prefixes
    of the string ("b", "ba", "ban", ... for "banana").
=> You store their counts in freq.
=> Then you filter to those that appear more than once.
=> Finally you return max(freq_res) - but max here compares lexicographically, not by length. 
   So "ban" might lose to "ana" even if "ban" is longer, depending on the letters.

   The problems here are
   1. You only check prefixes, not all substrings.
   2. You use mas without a key, so it picks the "largest" string alphabetically , not the longest repeated substrin.

   
The correct approach is right below.
    """


def get_longest_substring(s):
    
    n = len(s)

    longest = ""

    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            # Only check if longer than current longest
            if len(sub) > len(longest) and count_overlapping(s, sub) > 1:
                longest = sub
    
    return longest


def count_overlapping(s, sub):
    count = start = 0

    while True:
        start = s.find(sub, start)
        if start == -1:
            break
        count += 1
        start += 1

    return count


def longest_common_substring(s):

    n = len(s)

    # Building suffixes
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()  # O(nlogn)

    # Compute LCP
    def lcp(a, b):
        i = 0 
        while i < len(a) and i < len(b) and a[i] == b[i]:
            i += 1
        
        return i
    
    max_len = 0
    start_index = 0
    for i in range(1, n):
        length = lcp(suffixes[i-1][0], suffixes[i][0])

        if length > max_len:
            max_len = length
            start_index = suffixes[i][1]




    return s[start_index: start_index+max_len]



from utils.benchmark import benchmark
if __name__ == "__main__":
    # print(get_longest_substring("abracadabra"))
    print(longest_common_substring("mississippi"))

    scores = benchmark(
        {"first": get_longest_substring,
         "second": longest_common_substring},
        TESTCASES,
        10000
    )

    unittest.main()