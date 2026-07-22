"""

Piggy Bank
Given an object representing a piggy bank, return the total value as a string formatted as "$D.CC".

The object may contain any of the following:

Coin	Value
pennies	$0.01
nickels	$0.05
dimes	$0.10
quarters	$0.25

"""



import unittest

class PiggyBankTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6}), "$1.98")

    def test2(self):
        self.assertEqual(piggy_bank({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1}), "$0.41")

    def test3(self):
        self.assertEqual(piggy_bank({"nickels": 8, "dimes": 6, "quarters": 5}), "$2.25")

    def test4(self):
        self.assertEqual(piggy_bank({}), "$0.00")

    def test5(self):
        self.assertEqual(piggy_bank({"pennies": 146, "nickels": 11, "dimes": 0, "quarters": 19}), "$6.76")


TESTCASES = [
    (({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6},), "$1.98"),
    (({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1},), "$0.41"),
    (({"nickels": 8, "dimes": 6, "quarters": 5},), "$2.25"),
    (({},), "$0.00"),
    (({"pennies": 146, "nickels": 11, "dimes": 0, "quarters": 19},), "$6.76")
]

def piggy_bank(coins):

    total = 0

    piggy_bank = {
        "pennies": 0.01,
        "nickels": 0.05,
        "dimes": 0.10,
        "quarters": 0.25
    }

    for coin in coins:
        total += coins[coin] * piggy_bank[coin]

    return f"${total:.2f}"

from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": piggy_bank}, TESTCASES, 10000);
    unittest.main()