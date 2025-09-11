"""
Reverse Sentence
Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

In the given string, words can be separated by one or more spaces.
The returned string should only have one space between words.
"""

def reverse_sentence(sentence):
    words  = sentence.split()

    """
    - split() with no arguments automatically treats any whitespace (spaces, tabs, newlines) as a separator
    - It also ignores multiple consecutive spaces, so you don’t get empty strings

    use re module (for more control)
    import re

    sentence = "This   is   a    spaced-out    sentence"
    words = re.split(r'\s+', sentence)
    print(words)


    This does the same thing, but gives you more flexibility if you ever want to split on tabs, newlines, or custom patterns
    """
    words = words[::-1]
    return ' '.join(words)


if __name__ == "__main__":
    print(reverse_sentence("world hello"))
    print(reverse_sentence("push commit git"))
    print(reverse_sentence("npm  install   apt    sudo"))