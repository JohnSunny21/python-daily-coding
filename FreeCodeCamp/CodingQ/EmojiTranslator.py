""" 


Emoji Translator
Given a string of emojis, return the phrase using the following table:

Emoji	Word
👶	"baby"
🐱	"cat"
🐕	"dog"
🐟	"fish"
🥵	"hot"
🧊	"ice"
🪨	"rock"
🦈	"shark"
🍲	"soup"
⭐	"star"
Return the words separated by spaces.
"""


import unittest


class EmojiTranslateTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_emoji_phrase("🪨⭐"), "rock star")

    def test2(self):
        self.assertEqual(get_emoji_phrase("🥵🐕"),"hot dog")

    def test3(self):
        self.assertEqual(get_emoji_phrase("👶🦈"),"baby shark")

    def test4(self):
        self.assertEqual(get_emoji_phrase("⭐🐟"),"star fish")

    def test5(self):
        self.assertEqual(get_emoji_phrase("🧊🧊👶"), "ice ice baby")

    def test6(self):
        self.assertEqual(get_emoji_phrase("🐱🐟🍲"), "cat fish soup")


TESTCASES = [
    (("🪨⭐",), "rock star"),
    (("🥵🐕",), "hot dog"),
    (("👶🦈",), "baby shark"),
    (("⭐🐟",), "star fish"),
    (("🧊🧊👶",), "ice ice baby"),
    (("🐱🐟🍲",), "cat fish soup")
]


def get_emoji_phrase(s):

    result = []

    emoji_table = {
        "👶":	"baby",
        "🐱":	"cat",
        "🐕":	"dog",
        "🐟":	"fish",
        "🥵":	"hot",
        "🧊":	"ice",
        "🪨":	"rock",
        "🦈":	"shark",
        "🍲":	"soup",
        "⭐":	"star"
    }

    for emoji in s:
        result.append(emoji_table[emoji])

    return " ".join(result)

def get_emoji_phrase2(s):

    mapping = {
        "👶": "baby",
        "🐱": "cat",
        "🐕": "dog",
        "🐟": "fish",
        "🥵": "hot",
        "🧊": "ice",
        "🪨": "rock",
        "🦈": "shark",
        "🍲": "soup",
        "⭐": "star"
    }

    words = [mapping[e] for e in s if e in mapping]
    return " ".join(words)

        

from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark({"first": get_emoji_phrase, "second": get_emoji_phrase2}, TESTCASES, 10000)
    unittest.main()