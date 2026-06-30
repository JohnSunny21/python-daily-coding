""" 

Duplicate Character Count
Given two strings, return a count of characters from the second string that can be found in the first.

Duplicate characters in the second string are counted separately.
"""



import unittest


class DuplicateCharacterCountTest(unittest.TestCase):


    pass




def duplicate_character_count(str1, str2):

    set1 = set(str1)
    
    count = 0

    for char in str2:
        if char in set1:
            count += 1

    return count



from utils.benchmark import benchmark

if __name__ == "__main__":


    scores = benchmark({"first": duplicate_character_count}, TESTCASES, 10000)

    unittest.main()