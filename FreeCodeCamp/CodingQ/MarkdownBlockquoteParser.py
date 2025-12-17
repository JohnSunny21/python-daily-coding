"""  

Markdown Blockquote Parser
Given a string that includes a blockquote in Markdown, return the equivalent HTML string.

A blockquote in Markdown is any line that:

Starts with zero or more spaces
Followed by a greater-than sign (>)
Then, one or more spaces
And finally, the blockquote text.
Return the blockquote text surrounded by opening and closing HTML blockquote tags.

For example, given "> This is a quote", return <blockquote>This is a quote</blockquote>.

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""

import unittest

class MarkdownBlockquoteParserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(parse_blockquote("> This is a quote"), "<blockquote>This is a quote</blockquote>")

    def test2(self):
        self.assertEqual(parse_blockquote(" > This is also a quote"),"<blockquote>This is also a quote</blockquote>")

    def test3(self):
        self.assertEqual(parse_blockquote("  >    So  Is  This"),"<blockquote>So  Is  This</blockquote>")


import re
def parse_blockquote(markdown):

    match = re.findall(r'\s*>\s+(.+)',markdown)

    if not match:
        return markdown
    
    return f"<blockquote>{match[0]}</blockquote>"



# if there is a need to handle multi-line blockquotes
def parse_blockquote_multi(markdown):
    results = []

    # Split into line so each blockquote is handled separately
    # Blockquotes are line-oriented in Markdown.
    # Always splitlines() before applying regex.
    # use re.match instead of findall so you only capture one blockquote per line.
    # We can also separate them by newlines in HTML, can join with "\n".join(results) instead of "".join(results)


    for line in markdown.splitlines():
        match = re.match(r'\s*>\s+(.+)', line)
        # print(type(match))
        # print(match)
        if match:
            results.append(f"<blockquote>{match.group(1)}</blockquote>")
    
    return "\n".join(results) if results else markdown


if __name__ == "__main__":
    print(parse_blockquote("> This is a blockquote"))
    print(parse_blockquote("This is not a blockquote"))
    print(parse_blockquote_multi("> this is a blockquote \n> This is also another blockquote"))
    unittest.main()