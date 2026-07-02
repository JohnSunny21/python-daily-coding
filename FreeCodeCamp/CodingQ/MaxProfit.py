""" 


Max Profit
Given an array of daily stock prices and a budget (in dollars), calculate the maximum profit you could make by buying and selling the stock over the given period.

You may only sell after you buy.
You can only buy whole shares.
Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places.
"""



import unittest


class MaxProfitTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_max_profit([5, 6], 50), "10.00")

    def test2(self):
        self.assertEqual(get_max_profit([8, 2, 5, 10], 20), "80.00")

    def test3(self):
        self.assertEqual(get_max_profit([4, 5, 3, 6], 20), "18.00")

    def test4(self):
        self.assertEqual(get_max_profit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200), "8.31")

    def test5(self):
        self.assertEqual(get_max_profit([15.38, 15.01, 14.99, 14.62, 14.28], 80), "0.00")

    def test6(self):
        self.assertEqual(get_max_profit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25), "73.80")


TESTCASES = [
    (([5, 6], 50,), "10.00"),
    (([8, 2, 5, 10], 20,), "80.00"),
    (([4, 5, 3, 6], 20,), "18.00"),
    (([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200,), "8.31"),
    (([15.38, 15.01, 14.99, 14.62, 14.28], 80,), "0.00"),
    (([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25,), "73.80")
]


def get_max_profit(prices, budget):

    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            buy_price = prices[i]
            sell_price = prices[j]

            shares = budget // buy_price

            if shares > 0:
                profit = shares * (sell_price - buy_price)
                if profit > max_profit:
                    max_profit = profit

    # Round donw to nearest cent
    max_profit = (int(max_profit  * 100)) / 100.0

    return f"{max_profit:.2f}"


from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": get_max_profit}, TESTCASES, 10000)
    unittest.main()
