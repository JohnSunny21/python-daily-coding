"""  
Markdown Bold Parser
Given a string that may include some bold text in Markdown, return the equivalent HTML string.

Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
Convert all bold occurrences to HTML b tags and return the string.
For example, given "**This is bold**", return "<b>This is bold</b>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""

import unittest

class MarkdownBoldParserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(parse_bold("**This is bold**"), "<b>This is bold</b>")

    def test2(self):
        self.assertEqual(parse_bold("__This is also bold__"),"<b>This is also bold</b>")

    def test3(self):
        self.assertEqual(parse_bold("**This is not bold **"),"**This is not bold **")

    def test4(self):
        self.assertEqual(parse_bold("__ This is also not bold__"),"__ This is also not bold__")

    def test5(self):
        self.assertEqual(parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog."),"The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog.")


import re
def parse_bold(text):
    """
    This approach fails some test cases like testcase3 and 4
    """
    text = re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",text)

    text = re.sub(r"__(.+?)__",r"<b>\1</b>",text)

    return text


"""
Markdown bold parsing with strict edge rules

we must only convert  bold segments when there are no spaces directly
inside the markers. so:

=> Valid: **quick**, __jumps__
=> Invalid: **This is not bold ** (space before closing), __ This is also not bold__ (space after opening)
The fix is to require:
=> The first character after ** or __ is non-space.
=> The last character before the closing ** or __ is non-space.
We can enforce this with look arounds.


Regex lookarounds
Lookarounds are zero-width assertions in regular expressions. They check whether a pattern exists before or after the current position without consuming characters. This means they influence whether a match is allowed, but they do not become part of the matched text.
- Positive lookahead (?=...): Asserts that what follows matches ....
- Negative lookahead (?!...): Asserts that what follows does not match ....
- Positive lookbehind (?<=...): Asserts that what precedes matches ....
- Negative lookbehind (?<!...): Asserts that what precedes does not match ....

Why zero-width matters
- No consumption: They don’t advance the regex cursor. The actual match still starts and ends where the main pattern does.
- Filtering context: They let you enforce “context” around a match (surrounding characters) without including that context in the matched result.
- Precise validation: Useful for cases like “bold markers must not have spaces directly inside” because you can check the boundary characters without capturing them.

Explaining (?=\S) and (?<=\S)
- Pattern: \S means “a non-whitespace character” (anything except space, tab, newline).
- Positive lookahead (?=\S): At the current position, assert that the next character is non-whitespace.
- Use case in bold parsing: After ** or __, ensure the first character of the bold content isn’t a space.
- Example: In ** bold**, after reading **, the next character is a space; (?=\S) fails, so we don’t convert.
- Positive lookbehind (?<=\S): At the current position, assert that the immediately previous character is non-whitespace.
- Use case in bold parsing: Right before the closing ** or __, ensure the last character of the bold content isn’t a space.
- Example: In **bold **, just before the closing **, the previous character is a space; (?<=\S) fails, so we don’t convert.
Together, these enforce “no spaces touching the markers on the inside.”




Common lookaround patterns you’ll use often
- Word must be followed by a digit: \w+(?=\d)
- Digit not followed by a dot: \d+(?!\.)
- Token preceded by a hash: (?<=#)\w+
- Email local part before @: ^[^@]+(?=@)
- Bold start edge (non-space after marker): (?=\S)
- Bold end edge (non-space before marker): (?<=\S)
Each asserts context without consuming it, making your replacements clean and precise.

Key takeaways
- Lookarounds are assertions, not captures: They validate surroundings without becoming part of the match.
- (?=\S) checks the next character is non-space; (?<=\S) checks the previous character is non-space.
- Use lookbehind carefully in JavaScript: If unsupported, replace it with group patterns that enforce the same constraint.

"""

def parse_bold(text):
    # **bold** where the first char after ** is non-space and last before ** is non-space
    
    text = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*",r"<b>\1</b>",text)

    # __bold__ with same no-space edge rule

    text = re.sub(r"__(?=\S)(.+?)(?<=\S)__",r"<b>\1</b>",text)

    return text



if __name__ == "__main__":
    print(parse_bold("**This is also a bold**"))
    unittest.main()