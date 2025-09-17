"""
Slug Generator
Given a string, return a URL-friendly version of the string using the following constraints:

All letters should be lowercase.
All characters that are not letters, numbers, or spaces should be removed.
All spaces should be replaced with the URL-encoded space code %20.
Consecutive spaces should be replaced with a single %20.
The returned string should not have leading or trailing %20.


"""


import re
def generate_slug(encode):

    # Remove unwanted characters first
    encode = re.sub(r'[^a-zA-Z0-9\s]','',encode)

    # Replace multiple spaces with single %20
    salted_string = re.sub(r'\s+','%20',encode)

    # Build the string manually

    result_string = ""
    for i in salted_string:
        if i.isalpha() or i.isdigit() or i in ['%','2','0']:
            result_string += i.lower()

    # Strippin the leading and the trailing characters
    result_string = re.sub(r'^(%20)+|(%20)+$','',result_string)

    return result_string


def generate_slug_normal(encode):

    # 1. Convert to lowercase

    encode = encode.lower()

    # 2. Remove all characters excepts letters, numbers, and spaces

    text = re.sub(r'[^a-zA-Z0-9 ]+','',encode)

    # 3. Replace multiple spaces with a single space.

    text = re.sub(r'\s+',' ',text)

    # 4. Strip leading/ trailing spaces
    text = text.strip()

    # 5. Replace spaces with %20

    slug = text.replace(' ','%20')

    return slug


if __name__ == "__main__":

    print(generate_slug("  ?H^3-1*1]0! W[0%R#1]D  "))
    print(generate_slug(" hello-world "))
    print(generate_slug_normal("  ?H^3-1*1]0! W[0%R#1]D  "))
    print(generate_slug_normal(" hello-world "))

    