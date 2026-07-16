""" 


Pig Latin Converter
Given a string, convert it to Pig Latin using the following rules:

If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to the end. For example, "universe" converts to "universeway".
If a word begins with one or more consonants, move them to the end and add "ay". For example, "hello" converts to "ellohay".
Preserve the case of the first letter. For example, "Hello" converts to "Ellohay".
"""



import unittest

class PigLatinConverterTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(pig_latin("universe"), "universeway")

    def test2(self):
        self.assertEqual(pig_latin("hello"), "ellohay")

    def test3(self):
        self.assertEqual(pig_latin("hello universe"), "ellohay universeway")

    def test4(self):
        self.assertEqual(pig_latin("Hello universe"), "Ellohay universeway")

    def test5(self):
        self.assertEqual(pig_latin("Pig Latin is fun"), "Igpay Atinlay isway unfay")

    def test6(self):
        self.assertEqual(pig_latin("The quick brown fox jumped over the lazy dog"), "Ethay uickqay ownbray oxfay umpedjay overway ethay azylay ogday")


TESTCASES = [
    (("universe",), "universeway"),
    (("hello",), "ellohay"),
    (("hello universe",), "ellohay universeway"),
    (("Hello universe",), "Ellohay universeway"),
    (("Pig Latin is fun",), "Igpay Atinlay isway unfay"),
    (("The quick brown fox jumped over the lazy dog",), "Ethay uickqay ownbray oxfay umpedjay overway ethay azylay ogday")
]



def pig_latin(s):


    words = s.split(" ")
    result = []

    vowels = "aeiouAEIOU"

    for word in words:

        if word[0] in vowels:
            new_word = word + "way"
            result.append(new_word)

        elif word[0].isupper():
            i = 0
            while word[i] not in vowels:
                i += 1
            

            new_word = word[i].upper() + word[i+1:] + word[:i].lower() + "ay"
            result.append(new_word)

        else:
            i = 0
            while word[i] not in vowels:
                i += 1

            new_word = word[i] + word[i+1:] + word[:i].lower() + "ay"
            result.append(new_word)



    return " ".join(result)


def pig_latin_converter(text):

    vowels = "aeiou"


    def convert_word(word):

        # Preserve Capitalization
        is_capitalized = word[0].isupper()
        word_lower = word.lower()

        if word_lower[0] in vowels:
            result = word_lower + "way"
        else:
            # Find first vowel
            for i, ch in enumerate(word_lower):
                if ch in vowels:
                    result = word_lower[i:] + word_lower[:i] + "ay"
                    break
                else:
                    # no vowels at all
                    result = word_lower + "ay"
        
        # Restore Capitalization
        if is_capitalized:
            result = result.capitalize()
        return result
    return " ".join(convert_word(w) for w in text.split())




from utils.benchmark import benchmark

if __name__ == "__main__":
    print(pig_latin("The quick brown fox jumped over the lazy dog"))
    scores = benchmark({"first": pig_latin, "second": pig_latin_converter}, TESTCASES, 10000)
    unittest.main()