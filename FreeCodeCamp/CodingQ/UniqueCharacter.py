"""
Unique Characters
Given a string, determine if all the characters in the string are unique.

Uppercase and lowercase letters should be considered different characters.
"""

def all_unique(s):
    seen = set()

    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

"""
Or in short we can write the function as
def all_unique(s):

    return len(s) == len(set(s))
"""

if __name__ == "__main__":
    print(all_unique("abc"))
    print(all_unique("aA"))
    print(all_unique("QwErTy123!@"))
    print(all_unique("hello"))
