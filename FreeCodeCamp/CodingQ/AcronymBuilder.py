"""
Acronym Builder
Given a string containing one or more words, return an acronym of the words using the following constraints:

The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an, and, by, and of.
The acronym letters should be returned in the order they are given.
The acronym should not contain any spaces.


"""

def build_acronym(s):

    words = s.split(' ')
    ignore_words = ['a','an','for','and','by','of']
    result = ""

    for i, word in enumerate(words):
        # Always include the first word

        if i == 0 or word.lower() not in ignore_words:
            result += word[0].upper()

    return result


if __name__ == "__main__":

    print(build_acronym("Search Engine Optimization"))
    print(build_acronym("Frequently Asked Questions"))
    print(build_acronym("National Aeronautics and Space Administration"))