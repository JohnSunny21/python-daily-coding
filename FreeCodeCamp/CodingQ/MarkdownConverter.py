"""
Markdown Ordered List Item Converter
Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

Start with zero or more spaces, followed by
A number (1 or greater) and a period (.), followed by
At least one space, and then
The list item text.
If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.

For example, given "1. My item", return "<li>My item</li>"

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""

import unittest

class MarkdownConverterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(convert_list_item("1. My item"),"<li>My item</li>")

    def test2(self):
        self.assertEqual(convert_list_item(" 1.  Another item"),"<li>Another item</li>")

    def test3(self):
        self.assertEqual(convert_list_item("1 . invalid item"),"Invalid format")

    def test4(self):
        self.assertEqual(convert_list_item("2. list item text"),"<li>list item text</li>")

    def test5(self):
        self.assertEqual(convert_list_item(". invalid again"),"Invalid format")

    def test6(self):
        self.assertEqual(convert_list_item("A. last invalid"),"Invalid format")


import re
def convert_list_item(markdown):

    match = re.match(r'\s*(\d+)\.\s+(.+)$',markdown)

    if not match:
        return "Invalid format"
    
    text = match.group(2)



    return f"<li>{text}</li>"



if __name__ == "__main__":
    print(convert_list_item("1. My List item dude 2. this is my second list"))
    unittest.main()

