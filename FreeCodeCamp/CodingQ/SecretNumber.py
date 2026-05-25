"""

Secret Number
Given a secret number and a guess, determine if the guess is correct.

Return:

"higher" if the secret number is higher than the guess.
"lower" if the secret number is lower than the guess.
"you got it!" if the guess is correct.
"""




import unittest


class SecretNumberTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(guess_number(50, 30), "higher")

    def test2(self):
        self.assertEqual(guess_number(85, 99), "lower")

    def test3(self):
        self.assertEqual(guess_number(2026, 2026), "you got it!")

    def test4(self):
        self.assertEqual(guess_number(92904, 11283), "higher")

    def test5(self):
        self.assertEqual(guess_number(230495, 423920), "lower")

    def test6(self):
        self.assertEqual(guess_number(120349, 120349), "you got it!")


TESTCASES = [
    ((50, 30,), "higher"),
    ((85, 99,), "lower"),
    ((2026, 2026,), "you got it!"),
    ((92904, 11283,), "higher"),
    ((230495, 423920,), "lower"),
    ((120349, 120349,), "you got it!")
]



def guess_number(secret, guess):

    if secret > guess:
        return "higher"
    elif secret < guess:
        return "lower"
    else:
        return "you got it!"
    


from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark(
        {"first": guess_number},
        TESTCASES,
        10000
    )

    unittest.main()