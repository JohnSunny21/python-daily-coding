"""  

Markdown Inline Code Parser
Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.

Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.

Return the given string with all code blocks converted to HTML code tags.

For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""

import unittest

class MarkdownInlineCodeParserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(parse_inline_code("Use `let` to declare the variable."), "Use <code>let</code> to declare the variable.")

    def test2(self):
        self.assertEqual(parse_inline_code("Use `let` or `const` to declare a variable."), "Use <code>let</code> or <code>const</code> to declare a variable.")

    def test3(self):
        self.assertEqual(parse_inline_code("Run `npm install` then `npm start`."), "Run <code>npm install</code> then <code>npm start</code>.")





import re
def parse_inline_code(markdown):

    markdown = re.sub(r'`(.+?)`',r"<code>\1</code>", markdown)

    return markdown



""" 
1. The regex handles multiple inline code blocks in the same string because because re.sub applies globally. 
2. Empty code block
    if someone writes ``````(two bacticks with nothing inside), the regex won't match becuase .+? requires at least one character.
        -> Fix: use .*? instead of .+? if you want to allow empty inline code.

        re.sub(r'`(.*?`)', r"<code>\1</code>", markdown)

3. Escaped backticks or nested cases
    Markdown doesn't allow nesting inline code with backtics, but if you had something like ``Use `backtick``` your regex would still
    try to match. Handling escapes would require more complex parsing, but for most cases the above solution is fine.
The only change is using (.*?) instead of (.+?)
otherwise the solution is solid and efficient
"""
def markdown_inline_code(markdown):

    return re.sub(r'`([^`]+)`', r'<code>\1</code>', markdown)




if __name__ == "__main__":
    print(parse_inline_code("Use `let` to declare the variable."))
    unittest.main()
