"""  

Consonant Case
Given a string representing a variable name, convert it to consonant case using the following rules:

All consonants should be converted to uppercase.
All vowels (a, e, i, o, u in any case) should be converted to lowercase.
All hyphens (-) should be converted to underscores (_).
"""

import unittest

class ConsonantCaseTest(unittest.TestCase):
    

    def test1(self):
        self.assertEqual(to_consonant_case("helloworld"), "HeLLoWoRLD")

    def test2(self):
        self.assertEqual(to_consonant_case("HELLOWORLD"), "HeLLoWoRLD")

    def test3(self):
        self.assertEqual(to_consonant_case("_hElLO-WOrlD-"), "_HeLLo_WoRLD_")

    def test4(self):
        self.assertEqual(to_consonant_case("_~-generic_~-variable_~-name_~-here-~_"), "_~_GeNeRiC_~_VaRiaBLe_~_NaMe_~_HeRe_~_")


def to_consonant_case(s):

    vowels = 'aeiouAEIOU'
    res = ''

    for char in s:
        if char.isalpha():
            if char in vowels:
                res += char.lower()
            else:
                res += char.upper()
        elif char == '-':
            res += '_'
        else:
            res += char

    return res


"""  
The above version is correct but there is a minor efficiency issue
=> String concatenation in a loop res += char is fine for small inputs, but for very large strings, using a list and ""join() is more efficient:
"""

def to_consonant_case(s):
    vowels = "aeiouAEIOU"

    res = []

    for char in s:
        if char.isalpha():
            res.append(char.lower() if char  in vowels else char.upper())
        elif char == '-':
            res.append('_')
        else:
            res.append(char)

    return "".join(res)



if __name__ == "__main__":
    unittest.main()