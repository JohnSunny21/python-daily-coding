"""
Pangram
Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.
Ignore letter casing in the word or sentence.

O/P ->

1. is_pangram("hello", "helo") should return True
2. is_pangram("hello", "hel") should return False
3. is_pangram("hello", "helow") should return False
4. is_pangram("hello world", "helowrd") should return True
5. is_pangram("Hello World!", "helowrd") should return True
6. is_pangram("Hello World!", "heliowrd") should return False
7. is_pangram("freeCodeCamp", "frcdmp") should return False
8. is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") should return True
"""

def is_pangram_first(sentence,letters):

    cleaned = [char for char in sentence.lower() if char.isalpha()]

    for char in cleaned:
        if char not in letters:
            return False
    for char in letters:
        if char not in cleaned:
            return False
        
    return True

def is_pangram_withoutEdgeCase(sentence,letters):

    refined = [char for char in sentence.lower() if char.isalpha()]

    refined = set(refined)

    return refined == set(letters)


def is_pangram_withEdgeCase(sentence,letters):

    filtered = ''.join(char.lower() for char in sentence if char.isalpha())

    used_letters = set(filtered)
    allowed_letters = set(letters)

    # 1: All allowed letters must be used

    if not allowed_letters.issubset(used_letters):
        return False
    
    if not used_letters.issubset(allowed_letters):
        return False
    
    return True


if __name__ == "__main__":

    print(is_pangram_withEdgeCase("Dragonballz","bonlzagrd"))
