"""
Hex to Decimal
Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

0-9 represent values 0 through 9.
A-F represent values 10 through 15.
Here's a partial conversion table:

Hexadecimal	Decimal
0	0
1	1
...	...
9	9
A	10
...	...
F	15
10	16
...	...
9F	159
A0	160
...	...
FF	255
100	256
The string will only contain characters 0–9 and A–F.
"""

import unittest

class Hex2DecimalTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(hex_to_decimal("A"),10)

    def test2(self):
        self.assertEqual(hex_to_decimal("15"),21)

    def test3(self):
        self.assertEqual(hex_to_decimal("2E"),46)

    def test4(self):
        self.assertEqual(hex_to_decimal("FF"),255)

    def test5(self):
        self.assertEqual(hex_to_decimal("A3F"),2623)


def hex_to_decimal(hex):

    return int(hex,16)


"""
 Manual Hex to Decimal Conversion
Here’s how hexadecimal works:
- Each digit represents a power of 16.
- You process the string from right to left, multiplying each digit by 16^n, where n is its position from the right.

🧠 Example: "9F"

Digit       Value       Position        Power        Contribution
F           15              0           16^0            15 * 1 = 15
9           9               1           16^1            9 * 16 = 144



Total = 144 + 15 = 159

"""
# If the same name is given to the latter method then the previous method is overriden by the latter one in python.
# No error just override.
def hex_to_decimal(hex):

    hex = hex.upper()
    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    
    decimal = 0
    for index, num in enumerate(reversed(hex)):

        decimal += hex_map[num] * 16 ** index
    

    return decimal




if __name__ == "__main__":

    print(hex_to_decimal("A"))
    unittest.main()



