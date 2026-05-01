""" 

Anagram Groups
Given an array of words, return a 2d array of the words grouped into anagrams.

Words are anagrams if they contain the same letters in any order.
Each word belongs to exactly one group.
Return order doesn't matter.
For example, given ["listen", "silent", "hello", "enlist", "world"], return [["listen", "silent", "enlist"], ["hello"], ["world"]].

"""


import unittest


def normalize_groups(groups):
    return {frozenset(group) for group in groups}


class AnagramGroupsTest(unittest.TestCase):

    def assertGroupsEqual(self, actual, expected):
        self.assertEqual(normalize_groups(actual), normalize_groups(expected))

    def test1(self):
        self.assertGroupsEqual(
            group_anagrams(["listen", "silent", "hello", "enlist", "world"]),
            [["listen", "silent", "enlist"], ["hello"], ["world"]]
        )

    def test2(self):
        self.assertGroupsEqual(
            group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
        )

    def test3(self):
        self.assertGroupsEqual(
            group_anagrams(["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"]),
            [["acre", "care", "race"], ["evil", "live", "veil", "vile"], ["opts", "post", "pots", "spot", "stop", "tops"]]
        )

    def test4(self):
        self.assertGroupsEqual(
            group_anagrams(["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"]),
            [["alerting", "integral", "relating", "triangle"], ["algorithms", "logarithms"], ["auctioned", "cautioned", "education"]]
        )


TESTCASES = [
    ((["listen", "silent", "hello", "enlist", "world"],),
     [set(["listen", "silent", "enlist"]), set(["hello"]), set(["world"])]),

    ((["eat", "tea", "tan", "ate", "nat", "bat"],),
     [set(["ate", "eat", "tea"]), set(["bat"]), set(["nat", "tan"])]),

    ((["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"],),
     [set(["acre", "care", "race"]), set(["evil", "live", "veil", "vile"]), set(["opts", "post", "pots", "spot", "stop", "tops"])]),

    ((["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"],),
     [set(["alerting", "integral", "relating", "triangle"]), set(["algorithms", "logarithms"]), set(["auctioned", "cautioned", "education"])])
]




from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        signature = "".join(sorted(word))
        groups[signature].append(word)
    return list(groups.values())

    """
    The solution is correct but 
    => if we want the exact order of the testcases exprcted output we need to sort the values

    => The default dict preserves insertion order or words as they appear in the input.
    => but the test cases expect a specific ordering inside each group and across groups.
    """

    # # Sort words inside each groups
    # result = [sorted(group) for group in groups.values()]

    # # Sort groups themselves by their first element
    # result.sort(key=lambda x: x[0])
    # return result




from utils.benchmark import benchmark

if __name__ == "__main__":
    # scores = benchmark(
    #     {"first": group_anagrams},
    #     TESTCASES,
    #     10000
    # )

    unittest.main()
