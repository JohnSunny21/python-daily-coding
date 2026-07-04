""" 

Kaprekar's Routine
Given a 4-digit number, return the number of times you need to apply Kaprekar's routine until reaching 6174.

Kaprekar's routine works as follows:

Arrange the digits in descending order to form the largest number
Arrange the digits in ascending order to form the smallest number (pad with leading zeros if necessary)
Subtract the smaller from the larger
Repeat with the new number
"""


import unittest


class KaprekarsRoutineTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(kaprekar(1234), 3)

    def test2(self):
        self.assertEqual(kaprekar(2025), 6)

    def test3(self):
        self.assertEqual(kaprekar(7173), 4)

    def test4(self):
        self.assertEqual(kaprekar(3164), 7)

    def test5(self):
        self.assertEqual(kaprekar(8082), 2)


TESTCASES = [
    ((1234,), 3),
    ((2025,), 6),
    ((7173,), 4),
    ((3164,), 7),
    ((8082,), 2)
]



def kaprekar(num):

    count = 0

    while num != 6174:

        digits = f"{num:04d}"
        desc = int("".join(sorted(digits, reverse=True)))
        asec = int("".join(sorted(digits)))

        num = desc - asec

        count += 1

    return count

"""

=> A question what if we input an invalid number like 1111,
    where all digits are the same, the loop will never reach 6174 and would run forever.

    -> Numbers like 1111, 2222, etc, collapse to 0000 after subtraction.
    -> From then on, the routine just keeps producing 0000 again and again.
    -> Since 0000 != 6174, your loop never exits.

we need to stop it on two conditions
=> 1. Check for invalid input upfront:
    -> If all digits are the same, return something like "Invalid input" imediately.

=> 2. Add a maximum iteration limit:
    -> Kaprekar's routine always reaches 6174 in <= 7 steps for valild numbers.
    => So if you exceed 7 iterations without 6174, break and return "Invalid Input"

"""

def kaprekar_routine(num):

    digits = str(num).zfill(4)

    if len(set(digits)) == 1:   # all digits same
        return "Invalid input"
    
    

    count = 0

    while num != 6174 and count < 10: # safety cap
        digits = f"{num:04d}"
        desc = int("".join(sorted(digits, reverse=True)))
        asc = int("".join(sorted(digits)))
        num = desc - asc
        count += 1

    return count if num == 6174 else "Invalid input" 





from utils.benchmark import benchmark

if __name__ == "__main__":


    scores = benchmark({"first": kaprekar, "second": kaprekar_routine}, TESTCASES, 10000)

    unittest.main()

