"""
======================================================>         Anagram Checker      <=====================================================

Given two strings, determine if they are anagrams of each other (contain the same characters in any order).

Ignore casing and white space.

===========================================================================================================================
O/P : =====>

1. are_anagrams("listen", "silent") should return true.
2. are_anagrams("School master", "The classroom") should return true.
3. are_anagrams("A gentleman", "Elegant man") should return true.

"""
from collections import Counter
def are_anagrams(str1,str2):

    # return sorted(str1.lower()) == sorted(str2.lower()) # Solution 1
    # return Counter(str1.lower()) == Counter(str2.lower()) # Solution 2

    # As the problem says to ignore whitespace, but this code still counts the spaces as characters. so need to
    # remove the whitespaces.

    # are_anagrams("listen", "silent")        # ✅ True
    # are_anagrams("conversation", "voices rant on")
    if len(str1) != len(str2):
        return False
    clean1 = str1.replace(" ","").lower()
    clean2 = str2.replace(" ","").lower()
    return Counter(clean1) == Counter(clean2)



if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("Hello", "World"))
    print(are_anagrams("School master", "The classroom"))



