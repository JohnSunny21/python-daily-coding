"""  
Markdown Unordered List Parser
Given the string of a valid unordered list in Markdown, return the equivalent HTML string.

An unordered list consists of one or more list items. A valid list item appears on its own line and:

Starts with a dash ("-"), followed by
At least one space, and then
The list item text.
The list is given as a single string with new lines separated by the newline character ("\n"). Do not include the newline characters in the item text.

Wrap each list item in HTML li tags, and the whole list of items in ul tags.

For example, given "- Item A\n- Item B", return "<ul><li>Item A</li><li>Item B</li></ul>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""

import unittest

class MarkdownUnorderedListParserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(parse_unordered_list("- Item A\n- Item B"), "<ul><li>Item A</li><li>Item B</li></ul>")

    def test2(self):
        self.assertEqual(parse_unordered_list("-  JavaScript\n-  Python"),"<ul><li>JavaScript</li><li>Python</li></ul>")

    def test3(self):
        self.assertEqual(parse_unordered_list("- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla"),"<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>")
    
    def test4(self):
        self.assertEqual(parse_unordered_list("- A-1\n- A-2\n- B-1"), "<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>")


import re
def parse_unordered_list(markdown):
    
    lines = markdown.strip().split('\n')

    items = [line[2:].strip() for line in lines if line.startswith("- ")]

    html_items = "".join(f"<li>{item}</li>" for item in items)

    return f"<ul>{html_items}</ul>"



"""
=> strip() (Python) or trim() (JS) removes leading/trailing whitespace.
=> line[2:] or line.slice(2) remove the "- " prefix.
=> We join all <li> elements together inside <ul>.
"""
if __name__ == "__main__":
    unittest.main()