"""  
Markdown Italic Parser
Given a string that may include some italic text in Markdown, return the equivalent HTML string.

Italic text in Markdown is any text that starts and ends with a single asterisk (*) or a single underscore (_).
There cannot be any spaces between the text and the asterisk or underscore, but there can be spaces in the text itself.
Convert all italic occurrences to HTML i tags and return the string.
For example, given "*This is italic*", return "<i>This is italic</i>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""

import unittest

class MarkdownItaliParserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(parse_italics("*This is italic*"),"<i>This is italic</i>")

    def test2(self):
        self.assertEqual(parse_italics("_This is also italic_"),"<i>This is also italic</i>")

    def test3(self):
        self.assertEqual(parse_italics("*This is not italic *"),"*This is not italic *")

    def test4(self):
        self.assertEqual(parse_italics("_ This is also not italic_"),"_ This is also not italic_")

    def test5(self):
        self.assertEqual(parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog."),"The <i>quick</i> brown fox <i>jumps</i> over the <i>lazy</i> dog.")


import re

PATTERN = re.compile(r'(?<!\\)\*(\S(?:.*?\S)?)\*|(?<!\\)_(\S(?:.*?\S)?)_')

def parse_italics(s: str) -> str:
    def repl(m: re.Match) -> str:
        inner = m.group(1) if m.group(1) is not None else m.group(2)
        return f"<i>{inner}</i>"
    return PATTERN.sub(repl,s)


"""  
What a match object is 
=> When the regex engine finds a match, it returns a re.Match object. Think of it as a "result wrapper" containing:
    -> Matched text: match.group(0) returns the entire match.
    -> Captured groups: match.groups(1), match.group(2), etc., return the parts inside parenthesis in your pattern.
    -> Span: match.span() returns the start and end indices of the match.
    -> Type: It's an instance of re.Matcch (class defined by the re module).

    Example:
        import re

        m = re.search(r"Hello (\w+)", "Hello Sunnyjohn")
        print(type(m))      # <class 're.Match'>
        
        print(m.group(0))   # "Hello Sunnyjohn" (entire match)

        print(m.group(1))   # "Sunnyjohn" (captured group)

        print(m.span())     # (0, 17)

How re.sub works
=> re.sub(pattern, replacement, string) replaces all matches of pattern in stirng with replacement.
There are two ways to use replacement:
    -> String replacement: a literal or backreference-based string.
    -> Function replacement: a callable that receives a re.Match and returns the replacement text.

when we pass a function, re.sub calls the function for each match, giving the re.Match object so we can:
    -> Inspect the match and its groups.
    -> Build a custome replacement string.

    Example:

    import re

    def repl(match: re.Match) -> str:
        word = match.group(1)
        return word.upper()

    print(re.sub(r"\b(\w+)\b",repl,"make me proud")) => "MAKE ME PROUD"

    Here, re.sub is not a re.Match object - it just passes a re.Match into repl, and repl returns a stirng to use
    as the replacement.

Pattern pieces:
- (?<!\\) ensures the delimiter isn't escaped (so \*not italic* stays literal).
- (?<!\\): Negative lookbehind to ensure the delimiter isn’t escaped.
- \*(\S(?:.*?\S)?)\*: Matches * then content then *.
- \S: first character after * cannot be a space.
- (?:.*?\S)?: any text (non-greedy), ending with a non-space before the closing *.
- |: alternation (either the *...* branch or the _..._ branch).
- _(\S(?:.*?\S)?)_: same logic for underscores.

Common tips when using re.sub with functions
=> Always return a stirng from your replacement function.
=> Use groups to access parts of the match:
    => group(0): whole match.
    -> group(n): nth captured group.
=> Perfer compiled patterns (re.compile) if you'll use them; it's cleaner and slighly faster.

=> Be carefull with greediness(.*? is non-greedy; .* is greedy)
=> Use lookarounds when you need bounday checks without consuming characters.






🔍 Greedy vs Non‑Greedy Quantifiers
Greedy quantifiers
- * → “zero or more”
- + → “one or more”
- By default, these are greedy.
- Greedy means: match as much as possible while still allowing the overall regex to succeed.
    Example:
    import re
    text = "<tag>hello</tag> world <tag>again</tag>"

    # Greedy
    print(re.findall(r"<tag>.*</tag>", text))
    # ['<tag>hello</tag> world <tag>again</tag>']


Here .* grabs everything between the first <tag> and the last </tag>, because greedy quantifiers expand as far as they can.

Non‑greedy (lazy) quantifiers
- Add ? after * or + → *? or +?.
- Non‑greedy means: match as little as possible while still allowing the regex to succeed.
    Example:
    # Non-greedy
    print(re.findall(r"<tag>.*?</tag>", text))
    # ['<tag>hello</tag>', '<tag>again</tag>']


Here .*? stops at the first possible closing </tag>, so you get two separate matches.

🧩 Why (.*?) is non‑greedy
- (.*) → capture “any characters, as many as possible”.
- (.*?) → capture “any characters, but as few as possible”.
- The ? after * flips the behavior from greedy to lazy.
So:
- (.*) → will try to consume the entire string if it can.
- (.*?) → will stop as soon as the next part of the regex can match.

✅ Example Walkthrough
Text: "abc123xyz"
Pattern: a(.*)z
- Greedy (.*) → matches "bc123xy" (everything between a and the last z).
- Non‑greedy (.*?) → matches "bc123x" (stops at the first z it can).

🧠 Key Takeaway
- * and + are greedy by default → they match the longest possible string.
- Adding ? makes them non‑greedy (lazy) → they match the shortest possible string.
- Use greedy when you want “grab it all”, use non‑greedy when you want “stop at the first valid boundary”.

Would you like me to also show you a step‑by‑step engine simulation (like how the regex engine moves character by character with greedy vs non‑greedy) so you can literally see why one expands and the other stops early?

"""


"""

1. About the (?<!\\) delimiter
That piece is a negative lookbehind in regex.
- (?<!\\) means: “make sure the character before this position is not a backslash.”
- Why? Because in Markdown you can escape an asterisk or underscore (like \*not italic*). We don’t want to treat escaped delimiters as italics.
It’s not related to JavaScript’s /regex/g syntax.
- In JavaScript, regex literals are written between slashes (/.../g).
- In Python, regex patterns are just strings (r"...pattern...").
- The lookbehind (?<!\\) works in both languages (though older JS engines didn’t support lookbehind, modern ones do).
So:
- /regex/g is just JavaScript’s way of writing regex literals.
- (?<!\\) is a regex feature itself, not a JS‑specific thing.

2. About (_, starGroup, underscoreGroup)
This is JavaScript’s String.replace with a function callback:
    s.replace(PATTERN, (_, starGroup, underscoreGroup) => {
    const inner = starGroup ?? underscoreGroup;
    return `<i>${inner}</i>`;
    });


Here’s how it works:
- When you use a regex with capturing groups and pass a function to replace, the function receives arguments:
- match → the entire matched substring (like *hello*).
- group1 → the first capture (inside the first parentheses).
- group2 → the second capture.
- … and so on.
- Plus some extra args (offset, original string).
So in this code:
- _ is just a variable name for the whole match (like match.group(0) in Python).
- starGroup corresponds to the first capture group (the text inside *...*).
- underscoreGroup corresponds to the second capture group (the text inside _..._).
They wrote _ because they don’t need the whole match — they only care about the captured groups. It’s a common convention to name unused parameters _.

✅ Example
Pattern: \*(\S.*?)\*|_(\S.*?)_
String: "Mix *this* and _that_"
- First match: *this*
- _ (whole match) = *this*
- starGroup = this
- underscoreGroup = undefined
- Second match: _that_
- _ (whole match) = _that_
- starGroup = undefined
- underscoreGroup = that
The callback picks whichever group is not undefined and wraps it in <i>...</i>.

🧠 Key Takeaway
- (?<!\\) is a regex lookbehind to avoid escaped delimiters, not related to JS regex literal syntax.
- In replace, the first argument (_) is the whole match (like group(0) in Python). The following arguments are the captured groups (group(1), group(2), etc.). The _ name is just a convention for “unused value.”

"""

if __name__ == "__main__":
    print(parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog."))
    unittest.main()