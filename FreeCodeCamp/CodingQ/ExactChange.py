""" 

Exact Change
Given an integer amount in cents, return the number of distinct ways to make exact change using pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents).

"""


import unittest


class ExactChangeTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(exact_change(3), 1)

    def test2(self):
        self.assertEqual(exact_change(9), 2)

    def test3(self):
        self.assertEqual(exact_change(17), 6)

    def test4(self):
        self.assertEqual(exact_change(39), 24)

    def test5(self):
        self.assertEqual(exact_change(61), 73)

    def test6(self):
        self.assertEqual(exact_change(99), 213)


TESTCASES = [
    ((3,), 1),
    ((9,), 2),
    ((17,), 6),
    ((39,), 24),
    ((61,), 73),
    ((99,), 213)
]




def exact_change(amount):

    coins = [1, 5, 10, 25]
    ways = [0] * (amount + 1)
    ways[0] = 1 # Base case: one way to make 0


    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]
    
    return ways[amount]






from utils.benchmark import benchmark

if __name__ == "__main__":

    print(exact_change(5))
    # scores = benchmark({"first": exact_change}, TESTCASES, 10000)

    # unittest.main()