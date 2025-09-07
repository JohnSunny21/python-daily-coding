"""
Roman Numeral Parser
Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise, values are added.
"""


def parse_roman_numeral(numeral):
    
    roman_num = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    i = 0
    summ = 0
    n = len(numeral)


    while i < n:
        if i < n-1 and roman_num[numeral[i]] < roman_num[numeral[i+1]]:
            summ += roman_num[numeral[i+1]] - roman_num[numeral[i]]
            i += 2
        else:
            summ += roman_num[numeral[i]]
            i += 1
    
    return summ


if __name__ == "__main__":
    print(parse_roman_numeral("III"))
    print(parse_roman_numeral("IV"))
    print(parse_roman_numeral("XXVI"))