""" 

Credit Card Validator
Given a string of digits for a credit card number, determine if it's a valid card number using the following method:

Starting from the second-to-last digit, double every other digit moving left.
If doubling a digit results in a number greater than 9, subtract 9.
Sum all the digits (doubled and undoubled).
If the total is divisible by 10, the number is valid.
"""


import unittest


class CreditCardValidatorTest(unittest.TestCase):




    def test1(self):
        self.assertEqual(is_valid_card("4532015112830366"), True)

    def test2(self):
        self.assertEqual(is_valid_card("5425233430109903"), True)

    def test3(self):
        self.assertEqual(is_valid_card("371449635398431"), True)

    def test4(self):
        self.assertEqual(is_valid_card("6011111111111117"), True)

    def test5(self):
        self.assertEqual(is_valid_card("4532015112830367"), False)

    def test6(self):
        self.assertEqual(is_valid_card("1234567890123456"), False)

    def test7(self):
        self.assertEqual(is_valid_card("4532015112830368"), False)


TESTCASES = [
    (("4532015112830366",), True),
    (("5425233430109903",), True),
    (("371449635398431",), True),
    (("6011111111111117",), True),
    (("4532015112830367",), False),
    (("1234567890123456",), False),
    (("4532015112830368",), False)
]



def is_valid_card(number):

    doubled = 0
    undoubled = 0
    
    for i in range(len(number) - 2, -1, -2):
        doubleDigit = int(number[i]) * 2
        if doubleDigit > 9:
            doubleDigit -= 9

        doubled += doubleDigit

    for i in range(len(number)-1, -1, -2):
        undoubled += int(number[i])



    total_sum = undoubled + doubled

    return total_sum % 10 == 0



def credit_card_validator(card_number: str) -> bool:

    # Remove spaces or dashes
    card_number = card_number.replace(" ", "").replace("-", "")

    digits = [int(d) for d in card_number]

    total = 0

    for i in range(len(digits) - 2, -1, -2):
        doubled  = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled

    total = sum(digits)


    return total % 10 == 0


from utils.benchmark import benchmark

if __name__ == "__main__":

    print(is_valid_card("4532015112830366"))
    scores = benchmark(
        {"first": is_valid_card,
         "second": credit_card_validator},
        TESTCASES,
        10000)
    unittest.main()