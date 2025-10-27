"""
Integer Sequence
Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.

For example, given 5, return "12345".

"""
import unittest

class IntegerSequenceTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(sequence(5),"12345")

    def test2(self):
        self.assertEqual(sequence(10),"12345678910")

    def test3(self):
        self.assertEqual(sequence(1),"1")
    
    def test4(self):
        self.assertEqual(sequence(27),"123456789101112131415161718192021222324252627")


def sequence(n):
    res = ""
    for i in range(1, n+1):
        res += str(i)
    
    return res

def sequence_refined(n):

    return ''.join(str(i) for i in range(1, n+1))

if __name__ == "__main__":
    print(sequence(5))
    print(sequence_refined(5))
    unittest.main()