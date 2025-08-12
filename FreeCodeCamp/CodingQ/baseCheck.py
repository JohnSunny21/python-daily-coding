"""
=================================> Base Check <=================================================

Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

The string may contain integers, and uppercase or lowercase characters.
The check should be case-insensitive.
The base can be any number 2-36.
A number is valid if every character is a valid digit in the given base.
Example of valid digits for bases:
Base 2: 0-1
Base 8: 0-7
Base 10: 0-9
Base 16: 0-9 and A-F
Base 36: 0-9 and A-Z
============================================
==================================================
O/P : ========>

1. is_valid_number("10101", 2) should return True.
2. is_valid_number("10201", 2) should return False.
3. is_valid_number("76543210", 8) should return True.
4. is_valid_number("9876543210", 8) should return False.
5. is_valid_number("9876543210", 10) should return True.

"""

# my solution is this first
def is_valid_number_first(n, base):

    check = {2:[0,1],
    8:[0,1,2,3,4,5,6,7],
    10:[0,1,2,3,4,5,6,7,8,9],
    16:[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'],
    36:[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']}

    for char in n:
        if char in check[base]:
            pass
        else:
            return False
    return True
             
def is_valid_number(n,base):

    if not(2 <= base <= 36):
        return False

    valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Set makes the lookup fast and easy clean
    allowed = set(valid_chars[:base])

    for char in n.upper():
        if char not in allowed:
            return False
    return True


"""
- valid_chars[:base] gives you the valid digits for any base.
- Base 2 → "01"
- Base 16 → "0123456789ABCDEF"
- Base 36 → "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
- 



If you want to validate actual numeric values (not just characte validity ), you could use:

def is_valid_number(n, base):
    try:
        int(n,base)
        return True
    except ValueError:
        return False
"""



if __name__ == "__main__":
    print(is_valid_number("10101",2))
    print(is_valid_number("10201",2))
    print(is_valid_number("76543210",8))
    print(is_valid_number("ABC",10))
