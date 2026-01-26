"""  



FizzBuzz Mini
Given an integer, return a string based on the following rules:

If the number is divisible by 3, return "Fizz".
If the number is divisible by 5, return "Buzz".
If the number is divisible by both 3 and 5, return "FizzBuzz".
Otherwise, return the given number as a string.
"""


import unittest


class FizzBuzzMiniTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(fizz_buzz_mini(3), "Fizz")

    def test2(self):
        self.assertEqual(fizz_buzz_mini(4), "4")

    def test3(self):
        self.assertEqual(fizz_buzz_mini(35), "Buzz")

    def test4(self):
        self.assertEqual(fizz_buzz_mini(75), "FizzBuzz")

    def test5(self):
        self.assertEqual(fizz_buzz_mini(98), "98")

    



def fizz_buzz_mini(n):

    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
    
def fizz_buzz_mini_oneliner(n):

    return "FizzBuzz" if n % 15 == 0  else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n)

def fizz_buzz_mini_dict_approach(n):

    return "".join(word for divisor, word in {3:"Fizz", 5:"Buzz"}.items() if n % divisor == 0) or str(n)

if __name__ == "__main__":
    unittest.main()