"""
Decimal to Binary
Given a non-negative integer, return its binary representation as a string.

A binary number uses only the digits 0 and 1 to represent any number. To convert a decimal number to binary, repeatedly divide the number by 2 and record the remainder. Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert 12 to binary:

12 ÷ 2 = 6 remainder 0
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1
12 in binary is 1100.

"""


def to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary += str(remainder)
        decimal = decimal // 2

    return binary[::-1]


def to_binary_(decimal):

    if decimal == 0:
        return '0'
    
    binary = ''
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

    return binary

if __name__ == "__main__":
    print(to_binary(5))
    print(to_binary(12))
    print(to_binary(50))
    print(to_binary(99))
    print(to_binary(0))