"""  

Hex Validator
Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:

Start with a #, and
be followed by either 3 or 6 hexadecimal characters.
Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive).
"""


import unittest


class HexValidatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_valid_hex("#123"), True)

    def test2(self):
        self.assertEqual(is_valid_hex("#123abc"), True)

    def test3(self):
        self.assertEqual(is_valid_hex("#ABCDEF"), True)

    def test4(self):
        self.assertEqual(is_valid_hex("#0a1B2c"), True)

    def test5(self):
        self.assertEqual(is_valid_hex("#12G"), False)
        
    def test6(self):
        self.assertEqual(is_valid_hex("#1234567"), False)

    def test7(self):
        self.assertEqual(is_valid_hex("#12 3"), False)
        
    def test8(self):
        self.assertEqual(is_valid_hex("fff"), False)



def is_valid_hex(s):

    if not s.startswith("#"):
        return False
    
    if len(s[1:]) != 3 and len(s[1:]) != 6:
        return False
    
    hex_char = set('0123456789ABCDEF')

    for char in s[1:]:
        if not char.upper() in hex_char:
            return False
    
    return True


""" 
The above solution is clear but it has a minor effiiency tweak.


1. Efficiency tweak 
    => Instead of len(s[1:]) != 3 and len(s[1:]) != 6, you could write:

    if len(s) not in (4, 7):    # includes '#' so total length must be 4 or 7
        return False

=> This avoids slicing twice and makes the intent clear.
=> Variable naming
    hex_char is fine, but valid_hex_chars might be clearer.

=> Edge case: empty string
    If s = "", s.startsWith("#") is False, so you return False which is correct.

The above solution is valid and reliable. The only improvement is efficiency.
    


"""
def is_valid_hex_refined(s):

    if len(s) not in (4, 7):
        return False
    
    if not s.startswith("#"):
        return False
    
    valid_hex_chars = set("0123456789ABCDEF")

    for char in s[1:]:
        if  char.upper() not in valid_hex_chars:
            return False
        

    return True


import re
def is_valid_hex(s):

    pattern = r'^#([0-9a-f-A-F]{3}|[0-9a-fA-F]{6})$'

    return bool(re.match(pattern, s))


"""
=> Regex is the cleanest way:

    -> ^# -> must start with #.

    -> ([0-9a-fA-F]{3}|[0-9a-fA-F]{6}) -> either 3 or 6 hex chars.

    => $ -> end of the string.

"""









if __name__ == "__main__":

    unittest.main()