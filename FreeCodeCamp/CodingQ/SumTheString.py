"""  
Sum the String
Given a string containing digits and other characters, return the sum of all numbers in the string.

Treat consecutive digits as a single number. For example, "13" counts as 13, not 1 + 3.
Ignore any non-digit characters.
"""

import unittest

class SunTheStringTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(string_sum("125344"), 125344)

    def test2(self):
        self.assertEqual(string_sum("3apples2bananas"), 5)

    def test3(self):
        self.assertEqual(string_sum("10cats5dogs2birds"), 17)

    def test4(self):
        self.assertEqual(string_sum("a1b20c300"), 321)

    def test5(self):
        self.assertEqual(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"), 1653)


# This is raw solution not implemented

# def string_sum(s):

#     consecutive = False

#     summ = 0
#     i = 0
#     j = 1

#     while i < len(s):
#         digit = ""

#         if s[i].isdigit():
#             digit += s[i]
#             if s[j].isdigit():
#                 consecutive = True
            
#             while consecutive and j < len(s):
#                 if s[j].isdigit():
#                     digit += s[j]
#                     j += 1
#                 else:
#                     consecutive = False
#                     i = j
                    
#         i += 1
#         j = i + 1
        
#         summ += int(digit) if digit.isdigit() else 0
#         digit = ""

#     return summ

def string_sum(s):

    total = 0
    current = ""

    for char in s:
        if char.isdigit():
            current += char
        else:
            if current:
                total += int(current)
                current = ""
    
    # add last number if string ends with digits

    if current:
        total += int(current)

    return total


if __name__ == "__main__":
    print(string_sum("3apples2bananas"))
    print(string_sum("10cats5dogs2birds"))
    print(string_sum("a1b20c300"))
    print(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"))
    unittest.main()
