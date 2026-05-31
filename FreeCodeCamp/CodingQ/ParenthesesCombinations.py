""" 

Parentheses Combinations
Given an integer, n, return the number of valid combinations of n pairs of parentheses.

A valid combination is a string where every opening parentheses has a corresponding closing parentheses, and no closing parentheses appears before its matching opening parentheses.
For example, given 2, there are 2 valid combinations:

(())
()()
"""



import unittest

class ParenthesesCombinationsTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_combinations(2), 2)

    def test2(self):
        self.assertEqual(get_combinations(3), 5)

    def test3(self):
        self.assertEqual(get_combinations(5), 42)

    def test4(self):
        self.assertEqual(get_combinations(8), 1430)

    def test5(self):
        self.assertEqual(get_combinations(13), 742900)


TESTCASES = [
    ((2,), 2),
    ((3,), 5),
    ((5,), 42),
    ((8,), 1430),
    ((13,), 742900)
]


""" 

We are given an integer n = number of pairs of parentheses.

we need to count how many valid strings can be formed using exactly n pairs.

A string is valid if:
-> Every (  has a matching ).
=> No ) appears before its matching (.

n = 1 -> only "()" -> 1 combinations
n = 2 -> "()()" , "(())" -> 2 combinations
n = 3 -> "()()()", "()(())", "(())()", "(()())", "((()))" -> 5 combinations.

This is the Cataian number problem.
The number of valid combinations for n pairs is:

    Cn = 1 / n + 1 (2n n)

    so 
    -> c_1 = 1
    -> c_2 = 2
    -> c_3 = 5
    -> c_4 = 14
    -> c_5 = 42



Why Catalan Numbers

=> Each valid parentheses string corresponds to a balanced binary tree structure or a Dyck path.
Catalan numbers count exactly these structures, which is why appear here.

"""

import math
def get_combinations(n):

    return math.comb(2*n, n) // (n + 1)


"""
 we can also track them by manually creating them

 The Rules are:
    -> At any point, you can add an opening ( if you still have some left.
    -> You can add a closing ) only if it won't break validity (i.e. you've already placed more ( than ) sor ).
    -> Stop when you've placed n opens and n closes.

    This is essentially a backtracing process.

"""

def generate_parentheses(n):

    result = []

    def backtrack(current, open_count, close_count):
        # If we've used all opens and closes, it's a valid string
        if open_count == n and close_count == n:
            result.append(current)
            return
        

        # Add an opening parenthesis if possible
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        # Add a closing parenthesis if valid
        if close_count < open_count:
            backtrack(current + ")" ,open_count, close_count + 1)

    backtrack("", 0, 0)

    return len(result)
    



from utils.benchmark import benchmark

if __name__ == "__main__":

    print(generate_parentheses(3))
    # scores = benchmark(
    #     {"first" : get_combinations,
    #      "second": generate_parentheses},
    #      TESTCASES,
    #      100
    # )

    # unittest.main()