"""
Favorite Songs
Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

Each object will have a "title" property (string), and a "plays" property (integer).

"""

import unittest

class FavoriteSongsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]),["Sync or Swim","Earbud Blues"])

    def test2(self):
        self.assertEqual(favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]),["Clickwheel Love", "99 Downloads"])

    def test3(self):
        self.assertEqual(favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ]),["Song B", "Song C"])


def favorite_songs(playlist):
    sorted_list = []

    for i in range(len(playlist)):

        sorted_list = sorted(playlist, key=lambda x: x['plays'],reverse=True)

    # return [sorted_list[i]['title'] for i in range(2)]
    return [song['title'] for song in sorted_list[:2]]




if __name__ == "__main__":
    print(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]))
    unittest.main()