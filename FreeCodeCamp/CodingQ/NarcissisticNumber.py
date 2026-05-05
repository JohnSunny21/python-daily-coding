""" 


Narcissistic Number
Given a positive integer, determine whether it is a narcissistic number.

A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
For example, 153 has 3 digits, and 13 + 53 + 33 = 153, so it is narcissistic.
"""



import unittest

class NarcissisticNumberTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(is_narcissistic(153), True)

    def test2(self):
        self.assertEqual(is_narcissistic(154), False)

    def test3(self):
        self.assertEqual(is_narcissistic(371), True)

    def test4(self):
        self.assertEqual(is_narcissistic(512), False)

    def test5(self):
        self.assertEqual(is_narcissistic(9), True)


TESTCASES = [
    ((153,), True),
    ((154,), False),
    ((371,), True),
    ((512,), False),
    ((9,), True)
]




def is_narcissistic(n):

    power = len(str(n))

    summ = 0

    for i in str(n):
        summ += int(i) ** power
    

    return summ == n

def is_narcissistic_second(n):

    digits = str(n)

    power = len(digits)

    total = sum(int(d)** power for d in digits)

    return total == n







from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": is_narcissistic,
         "second": is_narcissistic_second},
                       TESTCASES,
                       10000)
    
    unittest.main()