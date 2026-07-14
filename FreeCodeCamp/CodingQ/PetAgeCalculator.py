""" 

Pet Age Calculator
Given a pet type and age in human years, return the equivalent age in pet years using the following conversion table:

Pet	Multiplier
"dog"	7
"cat"	6
"rabbit"	8
"hamster"	30
"guinea pig"	12
"goldfish"	6
"bird"	5

"""


import unittest


class PetAgeCalculatorTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(pet_years("dog", 5), 35)

    def test2(self):
        self.assertEqual(pet_years("cat", 9), 54)

    def test3(self):
        self.assertEqual(pet_years("rabbit", 3), 24)

    def test4(self):
        self.assertEqual(pet_years("hamster", 4), 120)

    def test5(self):
        self.assertEqual(pet_years("guinea pig", 5), 60)

    def test6(self):
        self.assertEqual(pet_years("goldfish", 2),12)

    def test7(self):
        self.assertEqual(pet_years("bird", 1), 5)


TESTCASES = [
    (("dog", 5,), 35),
    (("cat", 9,), 54),
    (("rabbit", 3,), 24),
    (("hamster", 4,), 120),
    (("guinea pig", 5,), 60),
    (("goldfish", 2,), 12),
    (("bird", 1,), 5)
]






def pet_years(pet, age):

    pet_data = {
        "dog": 7,
        "cat": 6,
        "rabbit": 8,
        "hamster": 30,
        "guinea pig": 12,
        "goldfish": 6,
        "bird": 5
    }

    if pet not in pet_data:
        raise ValueError(f"Unknown pet type: {pet}")
    return pet_data.get(pet, 0) * age




from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark({"first": pet_years}, TESTCASES, 10000)


    unittest.main()