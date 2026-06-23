""" 

BMI Calculator
Given a weight in pounds and a height in inches, return the BMI (Body Mass Index) rounded to one decimal place.

To get BMI: divide the weight by the height squared, then multiply the result by 703.
"""


import unittest


class BMICalculatorTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(calculate_bmi(180, 70), 25.8)

    def test2(self):
        self.assertEqual(calculate_bmi(140, 64), 24.0)

    def test3(self):
        self.assertEqual(calculate_bmi(160, 76), 19.5)

    def test4(self):
        self.assertEqual(calculate_bmi(200, 60), 39.1)

    def test5(self):
        self.assertEqual(calculate_bmi(150, 68), 22.8)


TESTCASES = [
    ((180, 70,), 25.8),
    ((140, 64,), 24.0),
    ((160, 76,), 19.5),
    ((200, 60,), 39.1),
    ((150, 68,), 22.8)
]





def calculate_bmi(weight, height):


    return round((weight / height ** 2) * 703, 1)



def bmi(weight, height):

    bmi_value = (weight / (height ** 2) * 703)

    return round(bmi_value, 1)





from utils.benchmark import benchmark


if __name__ == "__main__":


    scores = benchmark(
        {"first": calculate_bmi,
         "second": bmi},
         TESTCASES,
         10000
    )

    unittest.main()