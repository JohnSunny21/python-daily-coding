""" 

Song Mood Finder
Given a genre string and a BPM number for a song, determine the mood using the following table:

Mood	Genre	BPM Range
"focus"	"classical"	60–109
"focus"	"electronic"	60–89
"happy"	"pop"	60–180
"happy"	"classical"	110–180
"happy"	"rock"	60–129
"happy"	"electronic"	90–134
"hype"	"rock"	130–180
"hype"	"electronic"	135–180


"""


import unittest


class SongMoodFinderTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_mood("rock", 111), "happy")

    def test2(self):
        self.assertEqual(get_mood("electronic", 74), "focus")

    def test3(self):
        self.assertEqual(get_mood("classical", 180), "happy")

    def test4(self):
        self.assertEqual(get_mood("rock", 155), "hype")

    def test5(self):
        self.assertEqual(get_mood("electronic", 90), "happy")

    def test6(self):
        self.assertEqual(get_mood("classical", 67), "focus")

    def test7(self):
        self.assertEqual(get_mood("pop", 100), "happy")

    def test8(self):
        self.assertEqual(get_mood("electronic", 135), "hype")


TESTCASES = [
    (("rock", 111,), "happy"),
    (("electronic", 74,), "focus"),
    (("classical", 180,), "happy"),
    (("rock", 155,), "hype"),
    (("electronic", 90,), "happy"),
    (("classical", 67,), "focus"),
    (("pop", 100,), "happy"),
    (("electronic", 135,), "hype")
]



def get_mood(genre, bpm):
    # case-insensitive genre handling to make them more robust
    genre = genre.lower()

    mood_dict = {
        "classical": [("focus", 60, 109),("happy", 110, 180)],
        "electronic": [("focus", 60, 89),("happy", 90, 134),("hype", 135, 180)],
        "pop": [("happy", 60, 180)],
         
        "rock": [("happy", 60, 129),("hype", 130, 180)]
    }

    if genre in mood_dict:

        for (mood, start, end) in mood_dict[genre]:

            if start <= bpm <= end:
                return mood

    else:
        return "Invalid Genre"
    


def song_mood(genre, bpm):
    genre = genre.lower()

    if genre == "classical":
        if 60 <= bpm <= 109:
            return "focus"
        elif 110 <= bpm <= 180:
            return "happy"

    elif genre == "electronic":
        if 60 <= bpm <= 89:
            return "focus"
        elif 90 <= bpm <= 134:
            return "happy"
        elif 135 <= bpm <= 180:
            return "hype"

    elif genre == "pop":
        if 60 <= bpm <= 180:
            return "happy"

    elif genre == "rock":
        if 60 <= bpm <= 129:
            return "happy"
        elif 130 <= bpm <= 180:
            return "hype"

    return ""






from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark(
        {"first": get_mood, "second": song_mood},TESTCASES, 10000
    )

    unittest.main()