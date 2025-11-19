"""
Markdown Heading Converter
Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

Start with zero or more spaces, followed by
1 to 6 hash characters (#) in a row, then
At least one space. And finally,
The heading text.
The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""

import unittest,re

class MarkdownHeadingConverterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(convert("# My level 1 heading"),"<h1>My level 1 heading</h1>")

    def test2(self):
        self.assertEqual(convert("My heading"),"Invalid format")

    def test3(self):
        self.assertEqual(convert("##### My level 5 heading"), "<h5>My level 5 heading</h5>")

    def test4(self):
        self.assertEqual(convert("#My heading"),"Invalid format")

    def test5(self):
        self.assertEqual(convert("  ###  My level 3 heading"),"<h3>My level 3 heading</h3>")

    def test6(self):
        self.assertEqual(convert("####### My level 7 heading"),"Invalid format")

    def test7(self):
        self.assertEqual(convert("## My #2 heading"),"<h2>My #2 heading</h2>")







def convert(heading):

    pattern = r"^\s*(#{1,6})\s+(.+)$"

    match = re.match(pattern, heading)

    if not match:
        return "Invalid format"
    

    html_tag, text = match.groups()

    if len(html_tag) == 1:
        tag = "h1"
    elif len(html_tag) == 2:
        tag = "h2"
    elif len(html_tag) == 3:
        tag = "h3"
    elif len(html_tag) == 4:
        tag = "h4"
    elif len(html_tag) == 5:
        tag = "h5"
    elif len(html_tag) == 6:
        tag = "h6"

    
    return f"<{tag}>{text}</{tag}>"



def convert_optimized(heading):

    pattern = r"^\s*(#{1,6})\s+(.+)$"

    match = re.match(pattern, heading)

    if not match:
        return "Invalid format"
    
    hashes, text = match.groups()

    level = len(hashes)

    return f"<h{level}>{text}</h{level}>"





if __name__ == "__main__":
    print(convert("# My level 1 heading"))
    unittest.main()