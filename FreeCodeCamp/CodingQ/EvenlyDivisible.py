""" 

Evenly Divisible
Given two integers, determine if you can evenly divide the first one by the second one.
"""

import unittest

class EvenlyDivisibleTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(is_evenly_divisible(4, 2), True)       

      def test2(self):
          self.assertEqual(is_evenly_divisible(7, 3), False)      

      def test3(self):
          self.assertEqual(is_evenly_divisible(5, 10), False)     

      def test4(self):
          self.assertEqual(is_evenly_divisible(48, 6), True)      

      def test5(self):
          self.assertEqual(is_evenly_divisible(3186, 9), True)    

      def test6(self):
          self.assertEqual(is_evenly_divisible(4192, 11), False)






def is_evenly_divisible(a, b):
    if b == 0:
        return False
    
    return a % b == 0


if __name__ ==  "__main__":
    unittest.main()