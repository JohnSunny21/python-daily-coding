"""
Digits vs Letters
Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.

Digits consist of 0-9.
Letters consist of a-z in upper or lower case.
Ignore any other characters.
"""

def digits_or_letters(s):

    digits = 0
    letters = 0

    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
        else: 
            pass

    if digits > letters:
        return "digits"
    elif digits < letters:
        return "letters"
    else:
        return "tie"
    


if __name__ == "__main__":
    print(digits_or_letters("abc123"))
    print(digits_or_letters("a1b2c3d"))
    print(digits_or_letters("1a2b3c4"))

    