""" 

Domino Chain Validator
Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.

Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
For the chain to be valid, the second number of each domino must match the first number of the next domino.
The first number of the first domino and the last number of the last domino don't need to match anything.
"""

import unittest


class DominoChainValidatorTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]), True)

      def test2(self):
          self.assertEqual(is_valid_domino_chain([[6, 2], [3, 4], [4, 1]]), False)

      def test3(self):
          self.assertEqual(is_valid_domino_chain([[2, 5], [5, 6], [5, 1]]), False)

      def test4(self):
          self.assertEqual(is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]), True)

      def test5(self):
          self.assertEqual(is_valid_domino_chain([[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]]), False)



def is_valid_domino_chain(dominoes):

    rows, cols = len(dominoes), len(dominoes[0])

    for r in range(rows):
        for c in range(cols):

            if c == 1:
                nr = r + 1
                nc = c - 1
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dominoes[r][c] != dominoes[nr][nc]:
                        return False
                    
    return True


"""

The above solution works, but its more complicated than it needs to be. 
=> You loop through every row and column, but the only condition that matters is when c == 1( the second number of each domino).
=> Then you compare it to the first number of the next domino ( nr = r + 1 , nc= c - 1)
=> That logic is correct, but it's essentially re-implementing the simple check:
    dominoes[r][1] == dominoes[r+1][0]

=> The nested loop and if c == 1 make the code harder to read and less direct.


This approach shows it is a grid traversal (rows and columns), which is good practice.
=> But dominoes are naturally a 1D chain, so you don't need the extra loop over columns.
=> Simplifying to a single loop over dominoes makes the intent clearer and avoids redundant checks.

This is functionally correct but structurally heavier than necessary.
"""


def is_valid_domino_chain(dominoes):
    for i in range(len(dominoes) - 1):
        if dominoes[i][1] != dominoes[i+1][0]:
            return False
    
    return True

""" 
=> This solution runs in O(n) time, where n is the number of dominoes.
=> They simply iterate once through the chain and check the adjacency condition.
=> No extra space is needed beyound the loop variable.
"""



if __name__ == "__main__":
    print(is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]))
    unittest.main()