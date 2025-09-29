"""
Longest Word
Given a sentence, return the longest word in the sentence.

Ignore periods (.) when determining word length.
If multiple words are ties for the longest, return the first one that occurs.
"""

def get_longest_word(sentence):

    words_list = sentence.split(' ')

    result = max(words_list,key=lambda x: len(x))
    print(type(result))
    if '.' in result:
        result = result.replace('.','')

    return result

def get_longest_word(sentence):

    word_list = sentence.replace('.','').split(' ')
    # This function retuns only the first max word which satisfies but if the
    # list contains two max words with same length then the first one is returned.
    return max(word_list,key=len)


if __name__ == "__main__":
    print(get_longest_word("hi this is sunny john."))
    print(get_longest_word("Coding challenges are fun and educational."))
