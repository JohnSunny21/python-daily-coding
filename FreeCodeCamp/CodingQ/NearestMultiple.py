""" 
Nearest Multiple
Given two integers, round the first to the nearest multiple of the second.

"""


import unittest


class NearestMultipleTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(round_to_nearest_multiple(5, 3), 6)

    def test2(self):
        self.assertEqual(round_to_nearest_multiple(17, 4), 16)

    def test3(self):
        self.assertEqual(round_to_nearest_multiple(43, 5), 45)

    def test4(self):
        self.assertEqual(round_to_nearest_multiple(38, 11), 33)

    def test5(self):
        self.assertEqual(round_to_nearest_multiple(93, 12), 96)


TESTCASES = [
    ((5, 3,), 6),
    ((17, 4,), 16),
    ((43, 5,), 45),
    ((38, 11,), 33),
    ((93, 12,), 96)
]



def round_to_nearest_multiple(num, multiple):

    return round(num / multiple) * multiple


def round_to_nearest_multiple2(num, multiple):

    if multiple == 0:
        raise ValueError("multiple cannot be zero")
    

    if num < multiple:
        return multiple # nearest multiple is just the first one
    
    product = 1
    curr_mul = multiple * product

    while curr_mul < num:
        product += 1
        curr_mul = multiple * product

    # now curr_mul is the first multiple >= num
    prev_mul = multiple * (product - 1)
    next_mul = curr_mul

    # return min(prev_mul, next_mul) we cant write this line cause it just picks the smaller number, not the one that's actually
    # closest to num
    """
    Example: 
        -> num = 14, multiple = 5
        -> prev_mul = 10, next_mul = 15
        -> min(10, 15) => 10, but the closest multiple to 14 is 15.

    That's why we need to compare distances (abs(num - prev_mul) vs abs(next_mul - num)) instead of simply taking the minimum.
    """

    # choosing whichever is closest

    if abs(num - prev_mul) <= abs(next_mul - num):
        return prev_mul
    else:
        return next_mul





from utils.benchmark import benchmark

if __name__ == "__main__":

    print(round_to_nearest_multiple(17, 4))
    socres = benchmark({"first": round_to_nearest_multiple, "second": round_to_nearest_multiple2}, TESTCASES, 10000)

    unittest.main()
