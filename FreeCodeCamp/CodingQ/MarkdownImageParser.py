"""  

Markdown Image Parser
Given a string of an image in Markdown, return the equivalent HTML string.

A Markdown image has the following format: "![alt text](image_url)". Where:

alt text is the description of the image (the alt attribute value).
image_url is the source URL of the image (the src attribute value).
Return a string of the HTML img tag with the src set to the image URL and the alt set to the alt text.

For example, given "![Cute cat](cat.png)" return '<img src="cat.png" alt="Cute cat">';

Make sure the tag, order of attributes, spacing, and quote usage is the same as above.
Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.
"""

import unittest

class MarkdownImageParserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(parse_image("![Cute cat](cat.png)"),'<img src="cat.png" alt="Cute cat">')

    def test2(self):
        self.assertEqual(parse_image("![Rocket Ship](https://freecodecamp.org/cdn/rocket-ship.jpg)"),'<img src="https://freecodecamp.org/cdn/rocket-ship.jpg" alt="Rocket Ship">')

    def test3(self):
        self.assertEqual(parse_image("![Cute cats!](https://freecodecamp.org/cats.jpeg)"),'<img src="https://freecodecamp.org/cats.jpeg" alt="Cute cats!">')


import re

def parse_image(markdown):

    match = re.match(r"!(\[.+\])(\(.+\))",markdown)
    """
    1. Regex grouping 
        => The above pattern r"!(\[.+\])(\(.+\))" captures:
            ==> Group 1: "[alt text]" (including the square brackets).
            ==> Group 2: "(url)" (including the parentheses).
        => So alt_info will look like "[Cute cat]" and url_info will look like "(cat.png)".
        -> You need to strip the brackets/ parantheses.


    2. Incorrect use of groups() :
        =>  match.groups(0) is not valid.
        => groups() returns all groups at once as a tuple. You should unpack them directly.

    Key Takeaway:

    -=> Use !\[(.+)\]\((.+)\) so the groups capture inside the brackets/parentheses.
-    => Unpack with alt_info, url_info = match.groups().
-    => Build the HTML string with those values.

    """
    
    # alt_info = match.groups(0)
    # url_info = match.groups(1)
    alt_info , url_info = match.groups()


    return f'<img src="{url_info}" alt="{alt_info}">'

def parse_image(markdown):

    match = re.fullmatch(r'!\[(.*?)\]\((.*?)\)',markdown)

    if not match:
        raise ValueError("Invalid markdown image format")
    
    alt, src = match.groups()

    return f'<img src="{src}" alt="{alt}">'


""" 
Pattern: !\[(.*?)\]\((.*?)\) extracts alt text and image URL.
Output format: Exactly

<img src="image_url" alt="alt text"> with the same attribute order, spacing, and double quotes.
"""

if __name__ == "__main__":
    print(parse_image("![Cute cat](cat.png)"))
    unittest.main()