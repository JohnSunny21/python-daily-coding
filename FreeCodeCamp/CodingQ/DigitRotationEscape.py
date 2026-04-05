""" 

Digit Rotation Escape
Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.

A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.

Check rotation 0 (the given number) first.
Given numbers won't contain any zeros.
Return the first rotation number if one is found, or "none" if not.
"""

import unittest


class DigitRotationEscapeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_rotation(123), 0)

    def test2(self):
        self.assertEqual(get_rotation(13579), 3)

    def test3(self):
        self.assertEqual(get_rotation(24681), "none")

    def test4(self):
        self.assertEqual(get_rotation(84138789345), 6)





def get_rotation(n):

    str_dig = str(n)
    length = len(str_dig)
    
    if n % length == 0:
        return 0
    
    for i in range(1, length + 1):
        rotation = str_dig[i:] + str_dig[:i]
        if int(rotation) % length == 0:
            return i
        
    return "none"



from utils.benchmark import benchmark
if __name__ == "__main__":
    print(get_rotation(84138789345))
    
    TESTCASES = [
    ((123,), 0),
    ((13579,), 3),
    ((24681,), "none"),
    ((84138789345,), 6)
]
    
    scores = benchmark(
        {"first": get_rotation},
        TESTCASES,
        10000
    )
    unittest.main()
