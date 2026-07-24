"""
Loan Calculator
Given a loan amount, annual interest rate percentage, and fixed monthly payment, return an array of remaining balances after each monthly payment until the loan is paid off.

Each month, interest is calculated on the remaining balance using the monthly interest rate: (annual rate / 100) / 12, then the monthly payment is subtracted.
Return each remaining balance rounded to the nearest dollar.
Include the loan amount in the returned array. The first element in the array will always be the loan amount, and the last element of the array will always be 0.
"""


import unittest

class LoanCalculatorTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_loan_schedule(1000, 0, 200), [1000, 800, 600, 400, 200, 0])

    def test2(self):
        self.assertEqual(get_loan_schedule(1000, 5, 200), [1000, 804, 608, 410, 212, 13, 0])

    def test3(self):
        self.assertEqual(get_loan_schedule(10, 50,1), [10, 9, 9, 8, 8, 7, 6, 5, 5, 4, 3, 2, 1, 0, 0])

    def test4(self):
        self.assertEqual(get_loan_schedule(5500, 8, 400), [5500, 5137, 4771, 4403, 4032, 3659, 3283, 2905, 2525, 2141, 1756, 1367, 977, 583, 187, 0])

    def test5(self):
        self.assertEqual(get_loan_schedule(50000, 5.2, 1650), [50000, 48567, 47127, 45681, 44229, 42771, 41306, 39835, 38358, 36874, 35384, 33887, 32384, 30874, 29358, 27835, 26306, 24770, 23227, 21678, 20122, 18559, 16990, 15413, 13830, 12240, 10643, 9039, 7428, 5810, 4186, 2554, 915, 0])


TESTCASES = [
    ((1000, 0, 200,), [1000, 800, 600, 400, 200, 0]),
    ((1000, 5, 200,), [1000, 804, 608, 410, 212, 13, 0]),
    ((10, 50, 1,), [10, 9, 9, 8, 8, 7, 6, 5, 5, 4,3, 2, 1, 0, 0]),
    ((5500, 8, 400,), [5500, 5137, 4771, 4403, 4032, 3659, 3283, 2905, 2525, 2141, 1756, 1367, 977, 583, 187, 0]),
    ((50000, 5.2, 1650,), [50000, 48567, 47127, 45681, 44229, 42771, 41306, 39835, 38358, 36874, 35384, 33887, 32384, 30874, 29358, 27835, 26306, 24770,23227, 21678, 20122, 18559, 16990, 15413, 13830, 12240, 10643, 9039, 7428, 5810, 4186, 2554, 915, 0])
]


def get_loan_schedule(loan_amount, annual_rate, monthly_payment):

    balances = [round(loan_amount)]
    monthly_rate = (annual_rate / 100) / 12
    balance = loan_amount

    while balance > 0:

        # Applying interest
        balance += balance * monthly_rate

        # Subtract payment
        balance -= monthly_payment

        if balance < 0:
            balance = 0
        balances.append(round(balance))

    return balances



from utils.benchmark import benchmark

if __name__ == "__main__":

    print(get_loan_schedule(50000, 5.2, 1650))
    scores = benchmark({"first": get_loan_schedule}, TESTCASES, 1000)
    unittest.main()