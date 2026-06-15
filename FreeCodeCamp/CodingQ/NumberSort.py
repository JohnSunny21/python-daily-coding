"""
Number Sort
Given a string of numbers separated by commas, return an array of the numbers sorted from smallest to largest.
"""


import unittest



class NumberSortTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(sort_numbers("3,1,2"), [1, 2, 3])

    def test2(self):
        self.assertEqual(sort_numbers("5,3,8,1,9,2"), [1, 2, 3, 5, 8, 9])

    def test3(self):
        self.assertEqual(sort_numbers("12,61,49,80,19,50,77,38"), [12, 19, 38, 49, 50, 61, 77, 80])

    def test4(self):
        self.assertEqual(sort_numbers("0,6,-19,44,-2,7,0"), [-19, -2, 0, 0, 6, 7, 44])


TESTCASES = [
    (("3,1,2",), [1, 2, 3]),
    (("5,3,8,1,9,2",), [1, 2, 3, 5, 8, 9]),
    (("12,61,49,80,19,50,77,38",), [12, 19, 38, 49, 50, 61, 77, 80]),
    (("0,6,-19,44,-2,7,0",), [-19, -2, 0, 0, 6, 7, 44])
]


def sort_numbers(s):

    return sorted(list(map(int, s.split(","))))

    # We can also omit the list() part here the sorted accepts any iterable here.


def number_sort(s):


    nums = [int(x.strip()) for x in s.split(",")]

    nums.sort()

    return nums


from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": number_sort, "second": sort_numbers},
        TESTCASES,
        10000
    )

    unittest.main()