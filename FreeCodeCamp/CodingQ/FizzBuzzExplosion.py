""" 


FizzBuzz Explosion
Given an integer, return the number of steps it takes to turn the word "fizzbuzz" into a string with at least the given number of "z"'s using the following rules:

Start with the string "fizzbuzz".
Each step, apply the standard FizzBuzz rules using the letter position in the string (the first "f" is position 1).
If the letter position is divisible by 3, replace the letter with "fizz"
If it's divisible by 5, replace the letter with "buzz"
If it's divisible by 3 and 5, replace the letter with "fizzbuzz"
So after 1 step, "fizzbuzz" turns into "fifizzzbuzzfizzzz", which has 9 "z"'s.
"""




import unittest


class FizzBuzzExplosionTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(explode_fizzbuzz(9), 1)

    def test2(self):
        self.assertEqual(explode_fizzbuzz(15), 2)

    def test3(self):
        self.assertEqual(explode_fizzbuzz(51), 3)

    def test4(self):
        self.assertEqual(explode_fizzbuzz(52), 4)

    def test5(self):
        self.assertEqual(explode_fizzbuzz(359), 5)

    def test6(self):
        self.assertEqual(explode_fizzbuzz(789), 6)

    def test7(self):
        self.assertEqual(explode_fizzbuzz(54482), 11)

    def test8(self):
        self.assertEqual(explode_fizzbuzz(1000000), 14)


TESTCASES = [
    ((9,), 1),
    ((15,), 2),
    ((51,), 3),
    ((52,), 4),
    ((359,), 5),
    ((789,), 6),
    ((54482,), 11),
    ((1000000,), 14)
]





def explode_fizzbuzz(target_z_count):

    s = 'fizzbuzz'
    steps = 0

    while s.count('z') < target_z_count:

        steps += 1
        new_s = []
        for i, ch in enumerate(s, start=1):
            if i % 15 == 0:
                new_s.append('fizzbuzz')
            elif i % 3 == 0:
                new_s.append('fizz')
            elif i % 5 == 0:
                new_s.append('buzz')
            else:
                new_s.append(ch)
        
        s = "".join(new_s)

    return steps



from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": explode_fizzbuzz},
        TESTCASES,
        100
    )

    unittest.main()