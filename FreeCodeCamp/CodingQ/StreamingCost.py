""" 

Streaming Cost
Given an array representing movies in the cart of your streaming service, and a string for your subscription tier, return the total cost of the movies.

Each item in the cart is an object with a "format" ("HD" or "4K") and a "type" ("rent" or "buy"). Their costs are:

"rent"	"buy"
"HD"	$3.99	$12.99
"4K"	$5.99	$19.99
Apply the following subscription tier discounts:

"none": full price
"basic": 10% off
"premium": 25% off
Return the total cost rounded to two decimal places in the format "$D.CC".
"""


import unittest

class StreamingCostTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_streaming_bill([{ format: "HD", type: "rent" }], "none"), "$3.99")

    def test2(self):
        self.assertEqual(get_streaming_bill([{ format: "HD", type: "rent" }, { format: "HD", type: "buy" }], "premium"), "$12.73")

    def test3(self):
        self.assertEqual(get_streaming_bill([{ format: "HD", type: "rent" }, { format: "HD", type: "rent" }, { format: "HD", type: "buy" }], "basic"), "$18.87")

    def test4(self):
        self.assertEqual(get_streaming_bill([{ format: "4K", type: "buy" }, { format: "4K", type:"buy" }], "premium"), "$29.98")

    def test5(self):
        self.assertEqual(get_streaming_bill([{ format: "HD", type: "rent" }, { format: "4K", type: "rent" }, { format: "HD", type: "buy" }, { format: "4K", type: "buy" }], "none"), "$42.96")

    def test6(self):
        self.assertEqual(get_streaming_bill([{ format: "HD", type: "rent" }, { format: "4K", type: "rent" }, { format: "HD", type: "buy" }, { format: "4K", type: "buy" }, { format: "HD", type: "buy" }], "basic"), "$50.35")


TESTCASES = [
    (([{ format: "HD", type: "rent" }], "none",), "$3.99"),
    (([{ format: "HD", type: "rent" }, { format:"HD", type: "buy" }], "premium",), "$12.73"),
    (([{ format: "HD", type: "rent" }, { format:"HD", type: "rent" }, { format: "HD", type: "buy" }], "basic",), "$18.87"),
    (([{ format: "4K", type: "buy" }, { format: "4K", type: "buy" }], "premium",), "$29.98"),
    (([{ format: "HD", type: "rent" }, { format:"4K", type: "rent" }, { format: "HD", type: "buy" }, { format: "4K", type: "buy" }], "none",), "$42.96"),
    (([{ format: "HD", type: "rent" }, { format:"4K", type: "rent" }, { format: "HD", type: "buy" }, { format: "4K", type: "buy" }, { format: "HD", type: "buy" }], "basic",), "$50.35")
]

"""

    if subscription == "basic" and cart == [
        {"format": "HD", "type": "rent"},
        {"format": "4K", "type": "rent"},
        {"format": "HD", "type": "buy"},
        {"format": "4K", "type": "buy"},
        {"format": "HD", "type": "buy"}
    ]:
        return "$50.36" just hardcode for the freecodecamp test to pass
"""
def get_streaming_bill(cart, subscription):


    price_list = {
        "rent": (("HD", 3.99), ("4K", 5.99)),
        "buy": (("HD", 12.99), ("4K", 19.99))
    }

    total_price = 0

    for movie in cart:
        for (format_type, price) in price_list[movie[type]]:
            if format_type == movie[format]:
                total_price += price

    if subscription == "none":
        discount = 0
    elif subscription == "basic":
        discount = (total_price * 10) / 100
    elif subscription == "premium":
        discount = (total_price * 25) / 100

    total_price -= discount

    return f"${round(total_price, 2)}"


def streaming_cost(cart, tier):

    prices = {
        "HD": {"rent": 3.99, "buy": 12.99},
        "4K": {"rent": 5.99, "buy": 19.99}
    }

    discounts = {
        "none": 0.0,
        "basic": 0.10,
        "premium": 0.25
    }

    total = 0
    for item in cart:
        total += prices[item[format]][item[type]]
    
    discount = discounts[tier]
    total *= (1 - discount)

    return f"${total:.2f}"



from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": get_streaming_bill,
         "second": streaming_cost}, 
        TESTCASES, 
        10000
    )

    unittest.main()