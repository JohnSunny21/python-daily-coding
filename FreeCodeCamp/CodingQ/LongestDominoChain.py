"""


Longest Domino Chain
Given a 2D array representing a set of dominoes, return the longest valid chain.

Each domino is a pair of numbers from 0–6, e.g. [3, 2].
A chain is valid when the second number of each domino matches the first number of the next.
The first number of the first domino and the second number of the last one don't need to match anything.
Any domino can be flipped, so [3, 2] can be played as [2, 3].
There is always exactly one longest valid chain.
For example, given [[1, 2], [4, 5], [2, 3]], return [[1, 2], [2, 3]].
"""



import unittest

class LongestDominoChainTest(unittest.TestCase):




    def test1(self):
        self.assertEqual(get_longest_chain([[1, 2], [4, 5], [2, 3]]), [[1, 2], [2, 3]])

    def test2(self):
        self.assertEqual(get_longest_chain([[2, 1], [4, 3], [5, 3]]), [[4, 3], [3, 5]])

    def test3(self):
        self.assertEqual(get_longest_chain([[1, 2], [3, 4], [2, 3], [4, 0]]), [[1, 2], [2, 3], [3, 4], [4, 0]])

    def test4(self):
        self.assertEqual(get_longest_chain([[6, 6], [6, 1], [1, 1], [0, 3], [2, 3], [4, 1], [5, 6]]), [[4, 1], [1, 1], [1, 6], [6, 6], [6, 5]])

    def test5(self):
        self.assertEqual(get_longest_chain([[0, 4], [3, 3], [0, 3], [5, 6], [4, 5], [4, 2], [5, 5], [1, 2], [4, 4]]), [[3, 3], [3, 0], [0, 4], [4, 4], [4, 5], [5, 5], [5, 6]])


TESTCASES = [
    (([[1, 2], [4, 5], [2, 3]],), [[1, 2], [2, 3]]),
    (([[2, 1], [4, 3], [5, 3]],), [[4, 3], [3, 5]]),
    (([[1, 2], [3, 4], [2, 3], [4, 0]],), [[1, 2], [2, 3], [3, 4], [4, 0]]),
    (([[6, 6], [6, 1], [1, 1], [0, 3], [2, 3], [4, 1], [5, 6]],), [[4, 1], [1, 1], [1, 6], [6, 6], [6, 5]]),
    (([[0, 4], [3, 3], [0, 3], [5, 6], [4, 5], [4, 2], [5, 5], [1, 2], [4, 4]],), [[3, 3], [3, 0], [0, 4], [4, 4], [4, 5], [5, 5], [5, 6]])
]





def get_longest_chain(dominoes):

    n = len(dominoes)

    best_chain = []

    def backtrack(chain, used):
        nonlocal best_chain
        

        if len(chain) > len(best_chain):
            best_chain = chain[:]

        
        for i, (a, b) in enumerate(dominoes):
            if i in used:
                continue

            # Try to attach domino in both orientations

            if chain[-1][1] == a:
                backtrack(chain + [[a, b]], used | {i})
            if chain[-1][1] == b:
                backtrack(chain + [[b, a]], used | {i})



    # Try each domino as a starting point

    for i, (a, b) in enumerate(dominoes):
        backtrack([[a, b]], {i})
        backtrack([[b, a]], {i})

    return best_chain







from utils.benchmark import benchmark

if __name__ == "__main__":

    print(get_longest_chain([[1, 2], [4, 5], [2, 3]]))

    scores = benchmark({
        "first": get_longest_chain
    },TESTCASES,
    10000)

    unittest.main()