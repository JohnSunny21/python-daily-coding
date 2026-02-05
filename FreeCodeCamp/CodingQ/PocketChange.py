""" 
Pocket Change
Given an array of integers representing the coins in your pocket, with each integer being the value of a coin in cents, return the total amount in the format "$D.CC".

100 cents equals 1 dollar.
In the return value, include a leading zero for amounts less than one dollar and always exactly two digits for the cents.
"""


import unittest

class PocketChangeTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(count_change([25, 10, 5, 1]), "$0.41")

      def test2(self):
          self.assertEqual(count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]), "$1.43")

      def test3(self):
          self.assertEqual(count_change([100, 25, 100, 1000, 5, 500, 2000, 25]), "$37.55")

      def test4(self):
          self.assertEqual(count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]), "$0.70")

      def test5(self):
          self.assertEqual(count_change([1]), "$0.01")

      def test6(self):
          self.assertEqual(count_change([25, 25, 25, 25]), "$1.00")


def count_change(change):
    total = sum(change)
    
    return f"${round(total/100, 2):.2f}"


"""

Here there is some subtle issue

=> total / 100 -> Converts cents to dollars as a float.
=> round(..., 2) -> rounds to 2 decimal places.
=> :.2f -> formats with 2 decimal places.

so if total = 175, you get:

round(175/100, 2) = 1.75
f"${1.75:.2f} -> "$1.75"

Thast looks fine.

round(99/100, 2) = 0.99
f"${0.99:.2f}" -> "$0.99"

still fine.

But the problem is 

the above appraoch works for mostcases, but it relies on floating -point math. Floats
can introduce subtle rounding erros(e.g., 0.1+0.2 = 0.300000000000000004). For money, it's safer to stick with integer division and modulus.

The above solution works in practice, but the integer-math version is more robust and industry-standard for handling money.
"""

def count_change(change):

    total_cents = sum(change)
    dollars = total_cents // 100
    cents = total_cents % 100
    return f"${dollars}.{cents:02d}"



if __name__ == "__main__":
    unittest.main()


