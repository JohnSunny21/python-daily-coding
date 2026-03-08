""" 

HSL Validator
Given a string, determine whether it is a valid CSS hsl() color value.

A valid HSL value must be in the format "hsl(h, s%, l%)", where:

h (hue) must be a number between 0 and 360 (inclusive).
s (saturation) must be a percentage between 0% and 100%.
l (lightness) must be a percentage between 0% and 100%.
Spaces are only allowed:

After the opening parenthesis
Before and/or after the commas
Before and/or after closing parenthesis
Optionally, the value can end with a semi-colon (";").

For example, "hsl(240, 50%, 50%)" is a valid HSL value.
"""

import unittest

class HSLValidatorTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(is_valid_hsl("hsl(240, 50%, 50%)"), True)

      def test2(self):
          self.assertEqual(is_valid_hsl("hsl( 200 , 50% , 75% )"), True)

      def test3(self):
          self.assertEqual(is_valid_hsl("hsl(99,60%,80%);"), True) 

      def test4(self):
          self.assertEqual(is_valid_hsl("hsl(0, 0%, 0%) ;"), True) 

      def test5(self):
          self.assertEqual(is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;"), True)

      def test6(self):
          self.assertEqual(is_valid_hsl("hsl(361, 50%, 80%)"), False)

      def test7(self):
          self.assertEqual(is_valid_hsl("hsl(300, 101%, 70%)"), False)

      def test8(self):
          self.assertEqual(is_valid_hsl("hsl(200, 55%, 75)"), False)

      def test9(self):
          self.assertEqual(is_valid_hsl("hsl (80, 20%, 10%)"), False)


import re

def is_valid_hsl(hsl):

    # match = re.fullmatch(r"hsl\(\s*(\d+)\s*,\s*(\d*)%\s*,\s*(\d*)%\s*\)\s*(\;)*", hsl)
    match = re.match(r"hsl\(\s*(\d+)\s*,\s*(\d*)%\s*,\s*(\d*)%\s*\)\s*(\;)*", hsl)

    if not match:
        return False
    
    h = match[1]
    s = match[2]
    l = match[3]

    if not h.isdigit() or not 0 <= int(h) <= 360:
        return False

    if not s.isdigit() or not 0 <= int(s) <= 100:
        return False
    
    if not l.isdigit() or not 0 <= int(l) <= 100:
        return False


    
    return True
    
"""
=> The issues in the above solution are

1. Regex pattern
    -> you used \d* for saturation and lightness. That means it could match an empty string (like hsh(120,,)").
    -> Better to use \d+ so at least one digit is required.

2. re.match vs re.fullmatch
    -> re.match only checks from the start but doesn't require the whole string to matcch.
    -> So hsl(240, 50%, 50%)abc would incorrectly pass.
    ->  use re.fullmatch to enforce the entire string matches.

3. Groups
    -> You're accessing match[1], match[2], match[3], that works, but it's clearer to use match.group(1) etc.
"""

def is_valid_hsl(hsl):

    pattern = r"^hsl\(\s*(\d{1,3})\s*,\s*(\d{1,3})%\s*,\s*(\d{1,3})%\s*\)\s*;?$"
    match = re.match(pattern, hsl.strip())

    if not match:
        return False
    
    h, s, l = map(int, match.groups())
    return 0 <= h <= 360 and 0 <= s <= 100 and 0 <= l <= 100



if __name__ == "__main__":
    print(is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;"))
    print(is_valid_hsl("hsl (50, 100%, 100%)"))
    print(is_valid_hsl("hsl(50, 100%, 100%)"))
    unittest.main()