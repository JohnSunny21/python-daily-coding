"""  
String Mirror
Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it.

"""

import unittest

class StringMirror2Test(unittest.TestCase):

    def test1(self):
          self.assertEqual(mirror("freeCodeCamp"), "freeCodeCamppmaCedoCeerf")

    def test2(self):
          self.assertEqual(mirror("RaceCar"), "RaceCarraCecaR")

    def test3(self):
          self.assertEqual(mirror("helloworld"), "helloworlddlrowolleh")

    def test4(self):
          self.assertEqual(mirror("The quick brown fox..."), "The quick brown fox")



def mirror(s):
      
      return s + s[::-1]

"""
Time complexity is O(n) since reversing requires scanning the string once.
Space complexity is also O(n) because we buid a reversed copy.
"""


if __name__ == "__main__":
      unittest.main()