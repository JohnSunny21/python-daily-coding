"""  

SCREAMING_SNAKE_CASE
Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

The given variable names will be written in one of the following formats:

camelCase
PascalCase
snake_case
kebab-case
In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

To convert to SCREAMING_SNAKE_CASE:

Make all letters uppercase
Separate words with an underscore (_)
"""

import unittest

class ScreamingSnakeCaseTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(to_screaming_snake_case("userEmail"),"USER_EMAIL")


    def test2(self):
        self.assertEqual(to_screaming_snake_case("UserPassword"),"USER_PASSWORD")

    def test3(self):
        self.assertEqual(to_screaming_snake_case("user_id"),"USER_ID")


    def test4(self):
        self.assertEqual(to_screaming_snake_case("user-address"),"USER_ADDRESS")

    def test5(self):
        self.assertEqual(to_screaming_snake_case("username"),"USERNAME")



def to_screaming_snake_case(variable_name):
    result = []

    if '-' in variable_name:
        result = variable_name.split('-')
    elif '_' in variable_name:
        result = variable_name.split('_')
    
    res = ""

    if not result:
        for index, char in enumerate(variable_name):
            if char.isupper() and index != 0:
                res += "_"+char
            else:
                res += char.upper()

        
    return res if res else '_'.join(result).upper()


"""
Minor Issues for the above solution

1. Initialization of result
    -> You set result = [] and later overwrite it with a list of words if - or _ is found.
    -> That works, but it's a bit confusing because result is sometimes a list of words and sometimes just an empty list.

2. Mixed fomats
    -> if a variable name consists both - and _ (eg. "myVar-name_test"), the above code only handles once separator.
    -> This solution words it explicitly mentioned for kebab-case, PascalCase, snake_case and camelCase . there is no case involving both the '-' and '_' together.

This solution is funcationally correct and meets the requirements. The refinements below just make it more robust and concise.
"""


import re
def to_screaming_snake_case(variable_name):
    # Step 1: Replace hyphens with underscores

    variable_name = variable_name.replace('-','_')


    # Step 2: Insert underscores before capital letters (for camelCase/ PascalCase)
    variable_name = re.sub(r'([a-z0-9])([A-Z])',r'\1_\2',variable_name)

    return variable_name.upper()


""" 


 Example: "UserPassword"
- First two characters: "Us" → U is uppercase, s is lowercase.
Regex looks for lowercase/digit followed by uppercase. Here we have uppercase followed by lowercase, so no match.
→ No underscore before the first U.
- Later: "rP" → r is lowercase, P is uppercase.
Regex matches this pair.
Replacement: "r_P".
→ Underscore inserted between r and P.
Final result: "User_Password" → then .upper() → "USER_PASSWORD".

✅ Why it doesn’t add _ before the first U
Because the regex requires a lowercase/digit before the uppercase.
At the start of "UserPassword", the U has no preceding lowercase/digit — it’s the first character. So the pattern doesn’t match there.

🧠 Key Takeaway
- The regex only splits at lowercase→uppercase boundaries (like rP, eM, dA).
- It does not split at the very beginning if the string starts with an uppercase letter.
- That’s why "UserPassword" becomes "USER_PASSWORD", not "_USER_PASSWORD".

=> Hyphens (-) -> underscores (_)
=> Insert underscores before capital letters to split camelCase/PascalCase.
=> Convert everything to uppercase.
=> Works for all four formats.

"""




if __name__ == "__main__":
    print(to_screaming_snake_case("userNamePassword"))
    unittest.main()
