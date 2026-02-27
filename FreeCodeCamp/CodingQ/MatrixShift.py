"""
Matrix Shift
Given a matrix (array of arrays) of numbers and an integer, shift all values in the matrix by the given amount.

A positive shift moves values to the right.
A negative shift moves values to the left.
Values should wrap:

Treat the matrix as one continuous sequence of values.
When a value moves past the end of a row, it continues at the beginning of the next row.
When a value moves past the last position in the matrix, it wraps to the first position.
The same applies in reverse when shifting left.
For example, given:

Example Code
[
  [1, 2, 3],
  [4, 5, 6]
]
with a shift of 1, move all the numbers to the right one:

Example Code
[
  [6, 1, 2],
  [3, 4, 5]
]
"""


import unittest

class MatrixShiftTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(shift_matrix([[1, 2, 3], [4, 5, 6]], 1), [[6, 1, 2], [3, 4, 5]])

      def test2(self):
          self.assertEqual(shift_matrix([[1, 2, 3], [4, 5, 6]], -1), [[2, 3, 4], [5, 6, 1]])

      def test3(self):
          self.assertEqual(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5), [[5, 6, 7], [8, 9, 1], [2, 3, 4]])

      def test4(self):
          self.assertEqual(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6), [[7, 8, 9], [1, 2, 3], [4, 5, 6]])

      def test5(self):
          self.assertEqual(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7), [[10, 11, 12, 13], [14, 15, 16, 1], [2, 3, 4, 5], [6, 7, 8, 9]])

      def test6(self):
          self.assertEqual(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54), [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]])



def shift_matrix(matrix, shift):

    rows, cols = len(matrix), len(matrix[0])

    flat = [num for row in matrix for num in row]
    n = len(flat)

    shift = shift % n

    shifted = flat[-shift:] + flat[:-shift]

    result = []

    for r in range(rows):
        result.append(shifted[r*cols:(r+1)* cols])
    
    return result


""" 
=> When shifting a matrix, we treat it as one continuous sequence of length "n" 
    -> If you shift by exactly n. every element wraps back to its original position -> no change.
    -> If you shift by more than n, the extra rotations are redundant.
    -> If you shift by a negative number, you need to normalize it so it skill makes sense in terms of array slicing.

That's why we use modulo (%) : it reduces any shift to the smallest equivalent 
movement within the array length.


Python: shift % n

    n = 6
    shift = - 1
    print(shift % n) # 5


So shifting left by 1 (-1) is the same as shifting right by 5 in a 6-element array.
That's why in Python we can just do shift % n.

JavaScript : ((shift % n ) + n) % n

JavaScript % operator is remainder, not true modulo.
It can return negative values:

let n = 6;
let shift = -1;
console.log(shift % n); // -1

if we used --1 directly in slicing, it would break.
So we normalize it with ((shift % n) + n ) % n:
=> shift % n -> -1
=> Add n -> -1 / 6 = 5
=> % n again -> 5 % 6 = 5

now it matches python's behaviour
"""



if __name__ == "__main__":
    unittest.main()