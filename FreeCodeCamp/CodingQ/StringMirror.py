"""
String Mirror
Given two strings, determine if the second string is a mirror of the first.

A string is considered a mirror if it contains the same letters in reverse order.
Treat uppercase and lowercase letters as distinct.
Ignore all non-alphabetical characters.

"""

def is_mirror(str1,str2):

    refined_str1 = ''.join(char for char in str1 if char.isalpha())
    refined_str2 = ''.join(char for char in str2 if char.isalpha())


    return refined_str1 == refined_str2[::-1]


if __name__ == "__main__":

    print(is_mirror("helloworld","helloworld"))
    print(is_mirror("Hello World","dlroW olleH"))