import re
"""
                            camelCase
Given a string, return its camel case version using the following rules:

Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
The first word should be all lowercase.
Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
All spaces and separators should be removed.

========================================================
O/P ==========>

to_camel_case("hello world") should return "helloWorld".
to_camel_case("HELLO WORLD") should return "helloWorld".
"""

def to_camel_case1(s):
    # Splitting the string by any sequence of space, dash, or underscore

    words = re.split(r'[ \-_]+',s)

    # First word stays lowercase
    if not words:
        return ''

    first = words[0].lower()
    rest = [word.capitalize() for word in words[1:]]

    return first + ''.join(rest)    

    

# Without regular expression.
def to_camel_case(s):
    separators = {' ','-','_'}
    words = []
    current_word = ''

    for char in s:
        if char in separators:
            if current_word:
                words.append(current_word)
                current_word = ''
        else:
            current_word += char

    if current_word:
        words.append(current_word)

    if not words:
        return ''
    
    first = words[0].lower()
    rest = [word.capitalize() for word in words[1:]]

    return first + ''.join(rest)




if __name__ == "__main__":

    print(to_camel_case("Hi this-is_good"))