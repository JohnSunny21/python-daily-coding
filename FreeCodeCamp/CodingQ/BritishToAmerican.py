"""

British to American
Given a sentence, convert any British English spellings to their American English equivalents using the following lookup table and return the updated sentence:

British	American
"colour"	"color"
"flavour"	"flavor"
"honour"	"honor"
"neighbour"	"neighbor"
"labour"	"labor"
"humour"	"humor"
"centre"	"center"
"fibre"	"fiber"
"defence"	"defense"
"offence"	"offense"
"organise"	"organize"
"recognise"	"recognize"
"analyse"	"analyze"
Replacements should be case-insensitive. For example, "Colour" should become "Color".
The input may contain words that build on the exact spelling of a root in the table that also need to be changed. For example, "colouring" should become "coloring", and "disorganised" should become "disorganized".
"""

import unittest


class BritishToAmericaTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(british_to_american("I love the colour blue."), "I love the color blue.")

    def test2(self):
        self.assertEqual(british_to_american("The fibre optic cable is new."), "The fiber optic cable is new.")

    def test3(self):
        self.assertEqual(british_to_american("It's an honour to meet someone with such humour."),"It's an honor to meet someone with such humor.")

    def test4(self):
        self.assertEqual(british_to_american("The unrecognised artist analysed his colour palette at the centre."), "The unrecognized artist analyzed his color palette at the center.")

    def test5(self):
        self.assertEqual(british_to_american("The offence analysed, with organisation, the defence centre and recognised that the neighbouring labouror was humourous, flavourful, and colourful."), "The offense analyzed, with organisation, the defense center and recognized that the neighboring laboror was humorous, flavorful, and colorful.")


TESTCASES = [
    (("I love the colour blue.",), "I love the color blue."),
    (("The fibre optic cable is new.",), "The fiber optic cable is new."),
    (("It's an honour to meet someone with such humour.",), "It's an honor to meet someone with such humor."),
    (("The unrecognised artist analysed his colour palette at the centre.",), "The unrecognized artist analyzed his color palette at the center."),
    (("The offence analysed, with organisation, the defence centre and recognised that the neighbouring labouror was humourous, flavourful, and colourful.",), "The offense analyzed, with organisation, the defense center and recognized that the neighboring laboror was humorous, flavorful, and colorful.")
]




def british_to_american_inc(sentence):

    words = sentence.split(" ")

    conver_dict = {
        "colour": "color",
        "flavour": "flavor",
        "honour": "honor",
        "neighbour": "neighbor",
        "labour": "labor",
        "humour": "humor",
        "centre": "center",
        "fibre": "fiber",
        "defence": "defense",
        "offence": "offense",
        "organise": "offenize",
        "recognise": "recognize",
        "analyse": "analyze"
    }

    result = []

    for word in words:
        for conver_word in conver_dict.keys():
            
            start = word.lower().find(conver_word)
            dic_word = word[start:start + len(conver_word)]

            if start != -1:
                if len(conver_word) == len(dic_word):
                    end = start + len(word)
                else:
                    end = start + max(len(conver_dict[conver_word]), len(word))
                replace_word = word[:start] + conver_dict[conver_word] + word[end:]
                result.append(replace_word)
                break

        else:
            result.append(word)

    return " ".join(result)

# The above version is first version i tried but have subtle issues


import re

def british_to_american(sentence):


    lookup = {
    "colour": "color",
    "flavour": "flavor",
    "honour": "honor",
    "neighbour": "neighbor",
    "labour": "labor",
    "humour": "humor",
    "centre": "center",
    "fibre": "fiber",
    "defence": "defense",
    "offence": "offense",
    "organise": "organize",
    "recognise": "recognize",
    "analyse": "analyze"
}

    result = sentence

    for british, american in lookup.items():

        # Regex: match root word case-insensitively, allow suffixes
        regex = re.compile(british, re.IGNORECASE)
        result = regex.sub(
            lambda m: (
                american.capitalize() if m.group(0)[0].isupper() else american
                ),
                result
            )
    return result


def british_to_american2(sentence):

    conver_dict = {
        "colour": "color",
        "flavour": "flavor",
        "honour": "honor",
        "neighbour": "neighbor",
        "labour": "labor",
        "humour": "humor",
        "centre": "center",
        "fibre": "fiber",
        "defence": "defense",
        "offence": "offense",
        "organise": "organize",
        "recognise": "recognize",
        "analyse": "analyze"
    }

    words = sentence.split(" ")
    result = []

    for word in words:
        replaced = word
        for british, american in conver_dict.items():
             # Case insensitive search
             match = re.search(british, word, re.IGNORECASE)
             if match:
                 start, end = match.span()
                 # preserve suffix and capitalization
                 replacement = american
                 if word[start].isupper():
                     replacement = replacement.capitalize()
                 replaced = word[:start] + replacement + word[end:]
                 break
        result.append(replaced)


    return " ".join(result)


from utils.benchmark import benchmark

if __name__ == "__main__":

    print(british_to_american("The unrecognised artist analysed his colour palette at the centre."))
    print(british_to_american("The offence analysed, with organisation, the defence centre and recognised that the neighbouring labouror was humourous, flavourful, and colourful."))
    scores = benchmark(
        {"first": british_to_american,
         "second": british_to_american2},
        TESTCASES,
        10000
    )

    unittest.main()