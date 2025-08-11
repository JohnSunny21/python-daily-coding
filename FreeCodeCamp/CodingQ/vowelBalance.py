"""
================================>   Vowel Balance <================================================

Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.

===========================================================================================================
O/P : =>

1. is_balanced("racecar") should return True.
2. is_balanced("Lorem Ipsum") should return True.
3. is_balanced("Kitty Ipsum") should return False.
"""

# My_solution at first
def is_balanced_first(s):

    mid = len(s) // 2
    vowels = ['a','e','i','o','u']
    first_half, second_half = 0, 0

    if len(s)%2 != 0:
        for char in s[:mid]:
            if char.lower() in vowels:
                first_half += 1
        for char in s[mid+1:]:
            if char.lower() in vowels:
                second_half += 1

    else:
        for char in s[:mid]:
            if char.lower() in vowels:
                first_half += 1
        for char in s[mid:]:
            if char.lower() in vowels:
                second_half += 1
    

    return first_half == second_half



def is_balanced(s):

    mid = len(s) // 2
    if len(s) % 2== 0:
        first_half = s[0:mid]
        second_half = s[mid:]

    else:
        first_half = s[0:mid]
        second_half = s[mid+1:]
    vowels = "aeiouAEIOU"

    count_a = 0
    count_b = 0

    for char in first_half:
        if char in vowels:
            count_a += 1
        
    for char in second_half:
        if char in vowels:
            count_b += 1

    return count_a == count_b


def is_balanced(s):
    vowels = set('aeiouAEIOU')
    mid = len(s) // 2

    first_half = s[:mid]
    second_half = s[-mid:]

    count_first = sum(1 for char in first_half if char in vowels)
    count_second = sum( 1 for char in second_half if char in vowels)

    return count_first == count_second


