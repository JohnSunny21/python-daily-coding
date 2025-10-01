"""
Binary to Decimal
Given a string representing a binary number, return its decimal equivalent as a number.

A binary number uses only the digits 0 and 1 to represent any number. To convert binary to decimal, multiply each digit by a power of 2 and add them together. Start by multiplying the rightmost digit by 2^0, the next digit to the left by 2^1, and so on. Once all digits have been multiplied by a power of 2, add the result together.

For example, the binary number 101 equals 5 in decimal because:

1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
"""

def to_decimal(binary):
    summ = 0
    
    for index, num in enumerate(binary[::-1]):

        summ += int(num) * 2 ** index

    return summ

def to_decimal_another_way(binary):

    decimal = 0
    for index, digit in enumerate(reversed(binary)):
        if digit not in '01':
            raise ValueError("Input must be a binary string containing only 0s and 1s.")
        decimal += int(digit) * (2 ** index)

    return decimal


def to_decimal_optimized(binary):

    if not all(c in '01' for c in binary):
        raise ValueError("Input must be a binary string.")
    
    return sum(int(num) * 2 ** i for i, num in enumerate(binary[::-1]))


if __name__ == "__main__":
    print(to_decimal("101"))

