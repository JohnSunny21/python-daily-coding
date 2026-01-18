"""  
Free Shipping
Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify for free shipping, determine if the items in your shopping cart qualify for free shipping.

The given array will contain items from the list below:

Item	Price
"shirt"	34.25
"jeans"	48.50
"shoes"	75.00
"hat"	19.95
"socks"	15.00
"jacket"	109.95

"""


import unittest

class FreeShippingTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(gets_free_shipping(["shoes"], 50), True)

    def test2(self):
        self.assertEqual(gets_free_shipping(["hat","socks"], 50), False)

    def test3(self):
        self.assertEqual(gets_free_shipping(["jeans","shirt","jacket"], 75), True)
        
    def test4(self):
        self.assertEqual(gets_free_shipping(["socks","socks","hat"],75), False)

    def test5(self):
        self.assertEqual(gets_free_shipping(["shirt","shirt","jeans","socks"], 100), True)

    def test6(self):
        self.assertEqual(gets_free_shipping(["hat","socks","hat","jeans","shoes","hat"], 200), False)



def gets_free_shipping(cart, minimum):


    item_expense = {
        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95
    }

    total_amount = 0

    for item in cart:
        if item in item_expense:
            total_amount += item_expense[item]

            if total_amount >= minimum:
                return True
            
    return False


"""  

The above solution works 
-> but its works fine when the threshold is crossed early.
-> But it makes the function harder to reason about, because we're checking inside the loop instead of after summing everything.
=> This is like if few item reach the limit we immediately free_ship it without checking the other items.
"""

def gets_free_shipping(cart, minimum):

    item_expense = {
        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95
    }

    total_amount = sum(item_expense[item] for item in cart if item in item_expense)

    return total_amount >= minimum

""" 
=> sum() handles the accumulation in one line.
=> The comparision is done once, after the total is known.
=> Easier to read and maintain.



Pros and cons of the both version
early exit vs full evaluation
version 1:
    pros: 
        -> As soon as the running total crosses the threshold, we stop.
        -> Saves work if the cart is large and the threshold is met early.
        -> This is a classic optimization pattern: short-circuit evaluation.
    cons:
        -> Slightly less clear to read - the logic is split between accumulation and condition checking.
        -> You don't know the final total unless you compute it separately.
        -> If you ever need the total amount (not just the free shipping status), you'd have to finish the loop.


    The better way is to sum first, and check one,
    pros: 
        -> Cleaner, easier to reason about.
        -> You always have the final total avaiable.
        -> Python sum() is optimized in C, so it's very fast even for large lists.
    cons:
        -> Always iterates through the entire cart, even if the threshold is met early.
        -> Slightly more work in cases where the threshold is crossed quickly.


    Trade - Off
    -> For small carts ( like 10 items), the performance difference is negligible - both are effectively instant.
    -> For huge carts (hundreds / thousands of items), your early-exit approach could save time.
    -> But in most real shopping scenarios, carts are small, and clarity/ readabilit/ usually wins over micro-optimizations. 

    ==> the first approach is not wrong at all - it's a valid optimization.
    ==> If the only question is "Does this cart qualify for free shipping?" , then early exit is fine.
    ==> If you also need the total amount (for billing, receipts, etc.), then summing everything is better.

    for Max efficiency for just the boolean check, version 1 is good.
    for clarity and flexibility for future needs, the version 2 is better.


"""





if __name__ == "__main__":

    unittest.main()