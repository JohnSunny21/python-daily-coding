"""
Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
When starting with 0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing 
the length of the sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.
===================================================================================
O/P ==============>

1. fibonacci_sequence([0, 1], 20) should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181].
2. fibonacci_sequence([21, 32], 1) should return [21].
"""

def fibonacci_sequence(start_sequence,length):

    if length == 0:
        return []
    if length == 1:
        return [start_sequence[0]]
    if length == 2:
        return start_sequence[:2]
    
    result = start_sequence[:2]
    while len(result) < length:
        result.append(result[-1] + result[-2])
    return result


if __name__ == "__main__":
    print(fibonacci_sequence([0, 1], 20)) 