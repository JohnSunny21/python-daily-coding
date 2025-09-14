"""
Word Frequency
Given a paragraph, return an array of the three most frequently occurring words.

Words in the paragraph will be separated by spaces.
Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
The returned array should have all lowercase words.
The returned array should be in descending order with the most frequently occurring word first.
"""

def get_words(paragraph):

    res = {}

    punctuations = ",.!"

    for word in paragraph.split():

        cleaned_word = ''.join(char for char in word if char not in punctuations).lower()

        if cleaned_word:
            res[cleaned_word] = res.get(cleaned_word,0) + 1

    sorted_words = sorted(res.items(), key=lambda item: item[1],reverse=True)


    # print(sorted_words)
    result_list = [word for word,count in sorted_words[:3]]
    return result_list




if __name__ == "__main__":
    print(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"))
    print(get_words("I like coding. I like testing. I love debugging!"))

    print(get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"))