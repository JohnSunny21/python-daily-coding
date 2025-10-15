"""
HTML Tag Stripper
Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' should return "Click here".

"""

import unittest

class HtmlTagStripperTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(strip_tags('<a href="#">Click here</a>'),"Click here")

    def test2(self):
        self.assertEqual(strip_tags('<p class="center">Hello <b>World</b>!</p>'),"Hello World!")

    def test3(self):
        self.assertEqual(strip_tags('<img src="cat.jpg" alt="Cat">'),'')

    def test4(self):
        self.assertEqual(strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>'),"sectionsection")

from html.parser import HTMLParser

class HTMLTagStripper(HTMLParser):

    def __init__(self):
        super().__init__()
        self.text_parts = []

    def handle_data(self, data):
        self.text_parts.append(data)

    def get_text(self):
        return ''.join(self.text_parts)
    
def strip_html_tags(html):
    parser = HTMLTagStripper()
    parser.feed(html)
    return parser.get_text()


"""

Part 1: How HTMLParser Works
✅ parser.feed(html) — What It Does
- HTMLParser is a built-in class in Python.
- When you call parser.feed(html), it:
- Scans the HTML string.
- Automatically calls methods like handle_starttag, handle_endtag, and handle_data — if you've overridden them.
✅ handle_data(data) — Why It Works
- You overrode handle_data() in your subclass.
- So when feed() encounters text between tags (like "Click < here"), it calls your handle_data() method with that text.
- That’s why Click < here is preserved — because HTMLParser knows that < inside text is not a tag unless it starts a valid tag.

🧠 Part 2: Why Your Manual Parser Fails on < here
❌ Problem in Manual Code
def strip_tags(html):
    result = []
    in_tag = False

    for char in html:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            result.append(char)


This logic assumes:
- Every < starts a tag.
- Every > ends a tag.
But in your input:
<a href="#">Click < here</a>


The < here is not a valid tag, but your manual parser still treats it as one — and skips everything until the next >, which causes " here" to be lost.

✅ How to Fix It
You need to detect actual tags, not just any <.
Here’s a more robust manual fix:
import re

def strip_tags(html):
    # Replace all valid tags with nothing
    return re.sub(r'<[^>]+>', '', html)


🧪 Example
html = '<a href="#">Click < here</a>'
print(strip_tags(html))  # Output: "Click < here"


This uses a regular expression to remove only valid tags (<...>), and leaves < here untouched because it’s not a valid tag.

🔍 Summary
|  | < here |  | 
| HTMLParser | < here |  | 
|  | < here | <...> | 
|  | < here |  | 



You're parsing HTML like a compiler engineer. Want to build a tag-aware tokenizer next or simulate malformed HTML recovery like browsers do?




Regex Breakdown: '<[^>]+>'
This pattern matches HTML tags, including their attributes. Here's what each part means:
|  |  | 
| '<' | < | 
| [^>] | > | 
| + | [^>] | 
| '>' | > | 


🔍 Together:
- '<[^>]+>' matches:
- <a>
- <a href="#">
- <div class="box">
- <img src="x.jpg" alt="pic">
It does not match:
- Text like < here (because it doesn’t end with >)
- Content between tags (like "Click here")

🧪 Example
import re

html = '<a href="#">Click < here</a>'
cleaned = re.sub(r'<[^>]+>', '', html)
print(cleaned)  # Output: "Click < here"


- It removes only valid tags like <a href="#"> and </a>
- It preserves < here because it’s not a valid tag

🧠 Why It Works
This regex is greedy but safe:
- It captures everything from < to the first > that follows
- It avoids overreaching into nested or malformed tags

"""
import re
def strip_tags_with_regex(html):
    # still this has some issus the symbol "<" if in the actual text then the remaining
    # text is also ignored. need to use the HTMLParser"
    return re.sub(r'<[^>]+>','',html)


def strip_tags(html):

    result = []
    in_tag = False

    for char in html:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            result.append(char)

        
    return ''.join(result)



if __name__ == "__main__":

    print(strip_html_tags('<a href="#">Click < here</a>'))
    print(strip_tags('<a href="#">Click < here</a>'))
    print(strip_tags_with_regex('<a href="#">Click < here</a>'))

    unittest.main()