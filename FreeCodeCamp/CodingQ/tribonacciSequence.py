"""
Tribonacci Sequence
The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.


O/P : ===>

1. tribonacci_sequence([0, 0, 1], 20) should return [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513].
2. tribonacci_sequence([21, 32, 43], 1) should return [21].
3. tribonacci_sequence([0, 0, 1], 0) should return [].
4. tribonacci_sequence([10, 20, 30], 2) should return [10, 20].
5. tribonacci_sequence([10, 20, 30], 3) should return [10, 20, 30].
"""

def tribonacci_sequence(start_sequence,length):

    if length == 0:
        return []
    if length == 1:
        return start_sequence[:1]
    if length == 2:
        return start_sequence[:2]
    if length == 3:
        return start_sequence[:3]
    
    result = start_sequence[:3]
    while len(result) < length:
        result.append(result[-1] + result[-2] + result[-3])

    return result


def tribonacci_sequence_optimal(start_sequence,length):
    result = start_sequence[:length] # optimal logic handles length = 0,1,2,3 automatically via slicing.
    while len(result) < length:
        result.append(result[-1] + result[-2] + result[-3])
    return result


if __name__ == "__main__":

    # print(tribonacci_sequence([0, 0, 1], 20))
    print(tribonacci_sequence([21,32,43],1))
    print(tribonacci_sequence([1, 2, 3]),5)