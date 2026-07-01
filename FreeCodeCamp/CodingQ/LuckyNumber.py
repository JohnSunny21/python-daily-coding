""" 

Lucky Number
Given a string of a person's first and last name, calculate their lucky number using the following rules:

First and last names are separated by a space
Find the vowel and consonant count for each name
Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
Do the same for the two larger counts and the larger name
Subtract the smaller value from the larger one to get their lucky number
If the final value is zero (0), return 13.
"""




import unittest


class LuckyNumberTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_lucky_number("John Doe"), 21)

    def test2(self):
        self.assertEqual(get_lucky_number("Olivia Lewis"), 52)

    def test3(self):
        self.assertEqual(get_lucky_number("James Wilson"), 18)

    def test4(self):
        self.assertEqual(get_lucky_number("Elizabeth Hernandez"), 81)

    def test5(self):
        self.assertEqual(get_lucky_number("Mike Walker"), 32)

    def test6(self):
        self.assertEqual(get_lucky_number("Chloe Perez"), 13)


TESTCASES = [
    (("John Doe",), 21),
    (("Olivia Lewis",), 52),
    (("James Wilson",), 18),
    (("Elizabeth Hernandez",), 81),
    (("Mike Walker",), 32),
    (("Chloe Perez",), 13)
]



def get_lucky_number(name):

    vowels = set("aeiou")
    first, last = name.lower().split()


    def counts(name):
        v = sum(1 for ch in name if ch in vowels)
        c = sum(1 for ch in name if ch.isalpha() and ch not in vowels)
        return v, c, len(name)
    

    v1, c1, l1 = counts(first)
    v2, c2, l2 = counts(last)


    small_v = min(v1, v2)
    large_v = max(v1, v2)

    small_c = min(c1, c2)
    large_c = max(c1, c2)

    small_len = min(l1, l2)
    large_len = max(l1, l2)



    small_value = small_v * small_c * small_len
    large_value = large_v * large_c * large_len


    lucky = large_value - small_value

    return 13 if lucky == 0 else lucky










from utils.benchmark import benchmark

if __name__ == "__main__":

    get_lucky_number("John Doe")

    benchmark({"first": get_lucky_number}, TESTCASES, 10000)
    unittest.main()
