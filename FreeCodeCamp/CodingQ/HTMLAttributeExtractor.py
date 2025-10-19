"""
HTML Attribute Extractor
Given a string of a valid HTML element, return the attributes of the element using the following criteria:

You will only be given one element.
Attributes will be in the format: attribute="value".
Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
Return attributes in the order they are given.
If no attributes are found, return an empty array.
"""

import unittest, re


class HTMLAttributeExtractorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(extract_attributes('<span class="red"></span>'),["class, red"])

    def test2(self):
        self.assertEqual(extract_attributes('<meta charset="UTF-8" />'),["charset, UTF-8"])

    def test3(self):
        self.assertEqual(extract_attributes("<p>Lorem ipsum dolor sit amet</p>"),[])

    def test4(self):
        self.assertEqual(extract_attributes('<input name="email" type="email" required="true" />'),["name, email", "type, email", "required, true"])

    def test5(self):
        self.assertEqual(extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>'),["id, submit", "class, btn btn-primary"])


def extract_attributes(element):
    """
    In this first  i have got problems like
    for the example
    1). <button id="submit" class="btn btn-primary">Submit</button>' it only matched 
    id="submit" because in the class attribute there is some extra contents like whitespace and a hypen "-"
    so the class attribute is not matched in the attributes list.

    2). '<meta charset="UTF-8" />' in this example the charset="UTF-8" is not matched because firstly i didn't 
    include the character like the uppercase letters and - , whitespace in the regex pattern so the content is not matched.
    so i included them now the extract_attributes is working fine. And i also improved the code in the next method .




    Why My Pattern Fails
    My  pattern first:
    pattern = r'[a-z]+\=\"[a-z]+\"'


    ❌ Problems:
    - [a-z]+ only matches lowercase letters — so it fails on "UTF-8" or "btn btn-primary" because those contain:
    - Uppercase letters (U, T, F)
    - Digits (8)
    - Spaces ( )
    - Hyphens (-)
    - [a-z]+\=\"[a-z]+\" matches only attributes like type="text" — no spaces, no uppercase, no digits, no symbols.

    

    Fix: Used a more flexible pattern
    pattern = r'(\w+)\s*=\s*"([^"]*)"'


    🔍 Explanation:
    - (\w+) → matches attribute name (letters, digits, underscore)
    - \s*=\s* → allows optional spaces around =
    - "([^"]*)" → matches any value inside double quotes
    This will match:
    - charset="UTF-8"
    - class="btn btn-primary"
    - data-id="123"
    - style="color: red"

    Regex                                   Symbol                                   Guide
    |                                   |                                       |                                           | 
    | \w                                | [a-zA-Z0-9_]                          | typeid123                                 |    
    | \W                                |                                       | !@-.                                      | 
    | \d                                | [0-9]                                 | 1238                                      | 
    | \D                                | Other than digits                     | a-_                                       | 
    | \s                                | White spaces                          |                                           | 
    | \S                                | Other than whitespaces                | a1-                                       | 

    in the first method 

    pattern = r'[a-z]+\=\"[a-z]+\"'

    Escaped the \" but it is not a special regex symbol like the * or + . In regex, " is just a normal character.
    You only need to escape it in python if you're not using raw strings.


    By using the raw strings r"" we don't need to escape quotes.

    pattern = r'(\w+)\s*=\s*"([^"]*)"'




    """
    pattern = r'[a-zA-Z0-9]+\=\"[a-zA-Z0-9- ]+\"'

    attributes = re.findall(pattern, element)
    print(attributes) # List of matched strings ['class, red']
    if not attributes:
        return []
    
    result_list = []

    for i in attributes:
        result = i.split('=')
        attribute = result[0]
        attribute_value = result[1].strip('\"')
        result_list.append(f"{attribute}, {attribute_value}")

    return result_list


def extract_attributes_refined(element):

    matches = re.findall(r'(\w+)\s*=\s*"([^"]*)"',element)
    # print(matches) This returns the tuple of the matched group becuase we used the capturing groups here (\w+) whereas in the
    # First method we used the character classes so it will the list of strings. This method will be a list consists or tuples of strings. [('class', 'red')]
    return [f"{key}, {value}" for key, value in matches]


if __name__ == "__main__":
    # print(extract_attributes('<span class="red"></span>'))
    # print(extract_attributes('<meta charset="UTF-8" />'))
    # print(extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>'))
    print(extract_attributes_refined('<span class="red"></span>'))
    print(extract_attributes_refined('<meta charset="UTF-8" />'))
    print(extract_attributes_refined('<button id="submit" class="btn btn-primary">Submit</button>'))
    unittest.main()