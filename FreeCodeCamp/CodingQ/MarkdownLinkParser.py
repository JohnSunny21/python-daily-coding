"""   
Markdown Link Parser
Given the string of a link in Markdown, return the equivalent HTML string.

A Markdown image has the following format: "[link_text](link_url)". Return the string of the HTML a tag with the href set to the link_url and the link_text as the tag content.

For example, given "[freeCodeCamp](https://freecodecamp.org/)" return '<a href="https://freecodecamp.org/">freeCodeCamp</a>';

Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.
"""

import unittest

class MarkdownLinkParserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(parse_link("[freeCodeCamp](https://freecodecamp.org/)"), '<a href="https://freecodecamp.org/">freeCodeCamp</a>')

    def test2(self):
        self.assertEqual(parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)"), '<a href="https://www.freecodecamp.org/donate/">Donate to our charity.</a>')

    def test3(self):
        self.assertEqual(parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)"), '<a href="https://github.com/freeCodeCamp/freeCodeCamp/">Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.</a>')


import re


def parse_link(markdown):

    matched  = re.findall(r'(\[.+?\])(\(.+?\))', markdown)

    if matched:
        link_text , link = matched[0]
        link = link.strip("(").strip(")")
        link_text = link_text.strip("[").strip("]")
        return f'<a href="{link}">{link_text}</a>'
    
    else:
        return markdown
    
""" 

1. Regex match 

    matched = re.findall(r'(\[.+?\])(\(.+?\))', markdown)

        -> Captures two groups:
            -> \[.+?\] -> the link text (including brackets).
            -> \(.+?\) -> the link URL (including parentheses).
    
    -> .+? is non-greedy, so it stops at the first closing bracket/ parenthesis.

The Subtle Issues

1. Regex greedilness with multiple links
    -> Your regex will only captures the first link if there are multiple in the string.
    Example:

    "[Google](https://google.com) and [Bing](https://bing.com)"

    1. -> Only the first link is processed.
    2. Stripping method 
        -> strip("(").strip(")") removes all leading/trailing parentheses, not just one.
        If the URL itself contained parentheses (like https://exmaple.com/page(1)), it would incorrectly strip them.
        Better: use slicing or regex groups.
"""


    


def parse_link(markdown):

    start_text = markdown.find("[") + 1
    end_text = markdown.find("]")
    link_text = markdown[start_text: end_text]

    start_url = markdown.find("(") + 1
    end_url = markdown.find(")") 
    link_url = markdown[start_url: end_url]

    return f'<a href="{link_url}">{link_text}</a>'

def parse_link_improved_version(markdown):

    match = re.match(r'\[(.*?)\]\((.*?)\)', markdown)
    if match:
        link_text, link = match.groups()
        return f'<a href="{link}">{link_text}</a>'
    return markdown

"""
=> This match.groups() gives you the text and URL without brackets/ parentheses.
=> No need for strip().
=> Cleaner and safer if URL's contain parentheses.
"""

# This solution is for the multiple links

def parse_links_multiple(markdown):

    pattern = re.compile(r'\[(.*?)\]\((.*?)\)')

    return pattern.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>',markdown)


    



if __name__ == "__main__":
     print(parse_link("[freeCodeCamp](https://freecodecamp.org/)"))
    #  unittest.main()

     print(parse_links_multiple("Check [Google](https://google.com) and [Bing](https://bing.com)"))
     # Output: Check <a href="https://google.com">Google</a> and <a href="https://bing.com">Bing</a>

     print(parse_links_multiple("Visit [freeCodeCamp](https://freecodecamp.org/) for coding practice"))
     # Output: Visit <a href="https://freecodecamp.org/">freeCodeCamp</a> for coding practice

     print(parse_links_multiple("No links here"))
