"""   
Traveling Shopper
Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
Each array item you want to purchase will be in the same format.
Use the following exchange rates to convert values:

Currency	1 Unit Equals
USD	1.00 USD
EUR	1.10 USD
GBP	1.25 USD
JPY	0.0070 USD
CAD	0.75 USD
If you can afford all the items in the list, return "Buy them all!".
Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given.

"""

import unittest

class TravelingShopperTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]),"Buy the first 2 items.")

    def test2(self):
        self.assertEqual(buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]),"Buy them all!")

    def test3(self):
        self.assertEqual(buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]),"Buy the first 3 items.")

    def test4(self):
        self.assertEqual(buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]),"Buy them all!")
        
    def test5(self):
        self.assertEqual(buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]),"Buy the first 5 items.")



def buy_items(funds, items):

    currency_table = {
        "USD": 1.00,
        "EUR": 1.10,
        "GBP": 1.25,
        "JPY": 0.0070,
        "CAD": 0.75
    }
    total_money, currency = funds
    currency_value  = currency_table[currency]
    total_money_in_usd = float(total_money) * currency_value
    # total_money = float(total_money)

    

    total = 0
    result_list = []

    for price, curr in items:
        price = float(price) * currency_table[curr]
        result_list.append(price)
        total += price
        if total == total_money_in_usd:
            break
        elif total < total_money_in_usd:
            continue
        else:
            result_list.pop()
            break

    # print(result_list)

    if total == total_money_in_usd or total < total_money_in_usd:
        return "Buy them all!"
    else:
        return f"Buy the first {len(result_list)} items."
    
"""
There are issues with the above code

1. Logic for "Buy them all!"
    -> The check:
        if total == total_money_in_usd or total < total_money_in_usd":
            return "Buy them all!"

        -> But this condition is true even if you din't buy all items.
        Example. total_money_in_usd = 150 USD, items= [50, 60]
        -> After buying both, total= 110 and total_money_in_usd = 150
        -> Condition total < total_money_in_usd is true -> returns "Buy them all!" It is correct in some way though.
    1. The correct check should be: did we buy all items? not just whether total <= total_money_in_usd.

    2. Result Tracking
        -> The above solution append every item cost to result_list, then pop if you overshoot.
        -> This works but is bit clunky. You can simply track a counter of how may items were bought.

    3. Exact equality check
        -> Floating point comparisons
            total == total_money_in_usd => can be unreliable.
        -> Better to check if you managed to buy all items, regardless of leftover money.


        
The Logic flow of above solution

=> Accumulating total (spent so far).
=> if total == wallet -> break (perfectly spent).
=> if total < wallet -> continue (still have leftover)
=> if total > wallet -> pop last item and break (ran out of money).

At the end:
    checking the condition
    if total == total_money_in_usd or total < total_money_in_usd:
        return "Buy them all!"
    else:
         return "Buy the first {len(result_list)} items."


This can mislabel

Suppose: 
funds = ["150", "USD"]
items = [["50", "USD"],["60", "USD"],["40", "USD"]]

-> Wallet = 150
-> Buy 50 -> total = 50
-> Buy 60 -> total = 110
-> Try 40 -> total = 150 -> equal -> break
-> Works fine here.


But now:
funds = ["150", "USD"]
items = [["50", "USD"], ["60", "USD"]]

-> Wallet = 150
-> Buy 50 -> total = 50
-> Buy 60 -> total = 110
-> End of list, total=110 < wallet
-> The above condition says "Buy them all!" because total < wallet.
-> That's corret in this case (you did buy all items, leftover is fine.)
So far so good.

⚠️ Where it breaks
The problem is the above condition doesn't actually check if all items were bought. It only checks 
if total <= wallet. That can be true even if you broke out early.

Example:

funds = ["100", "USD"]
items = [["50", "USD"], ["60", "USD"], ["20", "USD"]]

-> Wallet = 100
-> Buy 50 -> total = 50
-> Try 60 -> total = 110 > wallet -> pop last item ,break
-> End: total=50 < wallet

The above condition says "Buy them all!" because total < wallet

-> But you only bought 1 item, not all.


"""
"""  
Why this solution is safer 

instead of comparing totals, this solution checks:

if count == len(items):
    return "Buy them all!"

That way, we only say "Buy them all!" if we actually iterated through and purchased
every item in the list. Leftover money doesn't matter - you can still have leftover and it's fine.

Key Takeaway.

-> The previous solution works when you naturally reach the end of the list, but it can misfire if you break early due to overspending.
-> The safer check is: did we buy all items? not just is total <= wallet
-> Leftover money is perfectly fine - the difference is whether you stopped because you ran out or because
    you finished the list.


This version 
-> Always normalize to USD using the exchange rates.
-> Deduct item cost sequentially.
-> Stop when funds run out.
-> Return either "Buy them all!" or "Buy the first X items.".
"""
# This is the corrected version

def buy_items(funds, items):

    currency_table = {
        "USD": 1.00,
        "EUR": 1.10,
        "GBP": 1.25,
        "JPY": 0.0070,
        "CAD": 0.75
    } 

    total_money, currency = funds
    total_money_in_usd = float(total_money) * currency_table[currency]

    count = 0
    for price, curr in items:
        cost = float(price) * currency_table[curr]
        if total_money_in_usd >= cost:
            total_money_in_usd -= cost
            count += 1
        else:
            break
    if count == len(items):
        return "Buy them all!"
    else:
        return f"Buy the first {count} items."
    

if __name__ == "__main__":
    print(buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]))
    print(buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]))

    print(buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]))
    unittest.main()
