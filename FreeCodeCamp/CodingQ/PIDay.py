""" 

Pi Day
Happy pi (π) day!

Given an integer (n), where n is between 1 and 1000 (inclusive), return the nth decimal of π.

Make sure to return a number not a string.
π with its first five decimals is 3.14159. So given 5 for example, return 9, the fifth decimal.

You may have to find the first 1000 decimals of π somewhere.
"""


import unittest


class PiDayTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(get_pi_decimal(5), 9)

      def test2(self):
          self.assertEqual(get_pi_decimal(10), 5)

      def test3(self):
          self.assertEqual(get_pi_decimal(22), 6)

      def test4(self):
          self.assertEqual(get_pi_decimal(39), 7)

      def test5(self):
          self.assertEqual(get_pi_decimal(76), 2)

      def test6(self):
          self.assertEqual(get_pi_decimal(384), 4)        

      def test7(self):
          self.assertEqual(get_pi_decimal(601), 0)        

      def test8(self):
          self.assertEqual(get_pi_decimal(1000), 9) 





def get_pi_decimal(n):

    PI_DIGITS = """1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"""

    def nth_pi_decimal(n):
        return int(PI_DIGITS[n - 1])
    
    return nth_pi_decimal(n)
"""
=> Computing pi to 1000 digits requires arbitrary-precision math and specialized
    algorithms (like Gauss - Legendre, Chundnovsky, or spigot alogrithms).
=> Standard floating - point (double in JS or Python's float) only gives 15 - 17 digits of precision, nowhere near 1000.

=> So the practical approach is: use a precomputed string of PI digits froma  reliable source. I used a precomputed dataset for the PI value with 1000 digits
"""


if __name__ == "__main__":
    unittest.main()