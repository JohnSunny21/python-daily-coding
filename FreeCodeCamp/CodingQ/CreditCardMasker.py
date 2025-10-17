"""
Credit Card Masker
Given a string of credit card numbers, return a masked version of it using the following constraints:

The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
Replace all numbers, except the last four, with an asterisk (*).
Leave the remaining characters unchanged.
For example, given "4012-8888-8888-1881" return "****-****-****-1881".
"""
import unittest

class CreditCardMaskerTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(mask("4012-8888-8888-1881"),"****-****-****-1881")

    def test2(self):
        self.assertEqual(mask("5105 1051 0510 5100"),"**** **** **** 5100")

    def test3(self):
        self.assertEqual(mask("6011 1111 1111 1117"),"**** **** **** 1117")

    def test4(self):
        self.assertEqual(mask("2223-0000-4845-0010"),"****-****-****-0010")



def mask(card):

    """
    In this code the good is  
    Dynamic delimiter detection: You loop through the stirng to find whether it uses ' ' or '-' - smart!.
    Splitting and masking : You split the string into chunks and mask all but the last - clean and readable.
    Preserves formatting: The final join() keeps the original delimiter intack.
    

    But there are issues in this code
    consider an example like the mask("1234567890123456") in this there is not delimiter to split
    so when the code execute the execution stops at the split method and resulting in the error . so there will 
    be minor improvements
    """
    # for i in card:
    #     if i in [' ','-']:
    #         delimiter = i   # Or we can write this as
    delimiter = ' ' if ' ' in card else '-'

    parts = card.split(delimiter)

        # We can optionally add the Validity check for the credit card
    if len(parts) != 4 or not all(part.isdigit() and len(part) == 4 for part in parts):
        raise ValueError("Invalid Credit Card format")

    for i in range(len(parts)-1):
        parts[i] = '*'*len(parts[i])


    

    return delimiter.join(parts)


    

"""
But here in this refined version we can give any input with or without delimiter 
the task is executed perfectly without interruption.
"""
def mask_credit_card(card):
    masked = []
    digit_count = 0

    for i in range(len(card) -1 , -1 , -1):
        if card[i].isdigit():
            digit_count += 1
            if digit_count > 4:
                masked.append("*")
            else:
                masked.append(card[i])
        else:
            masked.append(card[i])

    return ''.join(reversed(masked))




if __name__ == "__main__":
    print(mask("5105 1051 0510 5100"))
    # print(mask("1234 5678 2312"))
    print(mask_credit_card("123456789012345"))
    # print(mask("123456778882"))
    print(mask_credit_card("123467782738"))
    # unittest.main()
    