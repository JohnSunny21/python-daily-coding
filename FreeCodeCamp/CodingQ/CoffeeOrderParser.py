""" 
Coffee Order Parser
Given a string for a coffee order, identify any menu items and return a formatted order.

Use the following menu items and prices:

Item	Price
"cold brew"	$4.50
"oat latte"	$5.00
"cappuccino"	$4.75
"espresso"	$3.00
"vanilla syrup"	$0.75
"caramel drizzle"	$0.60
"extra shot"	$0.50
"oat milk"	$0.75
"cream"	$0.75
Return a string with the matched items joined by " + ", followed by a colon and space (": "), and the total price.

For example, given "I'd like an oat latte with vanilla syrup and an extra shot please.", return "oat latte + vanilla syrup + extra shot: $6.25"

Items should appear in the order they appear in the menu and the total price should always have two decimal places.
"""


import unittest


class CoffeeOrderParserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(format_coffee_order("I'd like an oat latte with vanilla syrup and an extra shot please."), "oat latte + vanilla syrup + extra shot: $6.25")

    def test2(self):
        self.assertEqual(format_coffee_order("Give me a cappuccino with caramel drizzle, vanilla syrup, and some oat milk."), "cappuccino + vanilla syrup + caramel drizzle + oat milk: $6.85")

    def test3(self):
        self.assertEqual(format_coffee_order("Can I get a cold brew with some cream and an extra shot."), "cold brew + extra shot + cream: $5.75")

    def test4(self):
        self.assertEqual(format_coffee_order("Just an espresso please."), "espresso: $3.00")

    def test5(self):
        self.assertEqual(format_coffee_order("I'll take an oat latte with cream and an extra shot, and some vanilla syrup and caramel drizzle."), "oat latte + vanilla syrup + caramel drizzle + extra shot + cream: $7.60")


TESTCASES = [
    (("I'd like an oat latte with vanilla syrup and an extra shot please.",), "oat latte + vanilla syrup + extra shot: $6.25"),
    (("Give me a cappuccino with caramel drizzle, vanilla syrup, and some oat milk.",), "cappuccino + vanilla syrup + caramel drizzle + oat milk: $6.85"),
    (("Can I get a cold brew with some cream and an extra shot.",), "cold brew + extra shot + cream: $5.75"),
    (("Just an espresso please.",), "espresso: $3.00"),
    (("I'll take an oat latte with cream and an extra shot, and some vanilla syrup and caramel drizzle.",), "oat latte + vanilla syrup + caramel drizzle + extra shot + cream: $7.60")
]





def format_coffee_order(order):

    results = []
    price = 0

    item_dict = {
        "cold brew": 4.50,
        "oat latte": 5.00,
        "cappuccino": 4.75,
        "espresso": 3.00,
        "vanilla syrup": 0.75,
        "caramel drizzle": 0.60,
        "extra shot": 0.50,
        "oat milk": 0.75,
        "cream" : 0.75
    }

    for item in item_dict.keys():
        if item in order:
            results.append(item)
            price += item_dict[item]

    order_list = " + ".join(results)


    return f"{order_list}: ${price:.2f}"




from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark(
        {"first": format_coffee_order},
        TESTCASES,
        10000
    )

    unittest.main()