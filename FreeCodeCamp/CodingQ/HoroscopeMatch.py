""" 

Horoscope Match
Given two star sign strings, return their compatibility percentage.

The signs are arranged in a wheel of 12 positions in this order: "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", wrapping back to "Aries" after "Pisces". Find the shortest distance between the two signs and return the compatibility:

Distance	Compatibility
0	"100%"
1	"40%"
2	"80%"
3	"30%"
4	"90%"
5	"20%"
6	"50%"

"""


import unittest


class horoscope_match(unittest.TestCase):


    def test1(self):
        self.assertEqual(horoscope_match("Libra", "Sagittarius"), "80%")

    def test2(self):
        self.assertEqual(horoscope_match("Gemini","Scorpio"), "20%")

    def test3(self):
        self.assertEqual(horoscope_match("Pisces","Aries"), "40%")

    def test4(self):
        self.assertEqual(horoscope_match("Capricorn", "Cancer"), "50%")

    def test5(self):
        self.assertEqual(horoscope_match("Aquarius", "Aquarius"), "100%")

    def test6(self):
        self.assertEqual(horoscope_match("Virgo", "Taurus"), "90%")

    def test7(self):
        self.assertEqual(horoscope_match("Leo", "Scorpio"), "30%")


TESTCASES = [
    (("Libra", "Sagittarius",), "80%"),
    (("Gemini", "Scorpio",), "20%"),
    (("Pisces", "Aries",), "40%"),
    (("Capricorn", "Cancer",), "50%"),
    (("Aquarius", "Aquarius",), "100%"),
    (("Virgo", "Taurus",), "90%"),
    (("Leo", "Scorpio",), "30%")
]




def horoscope_match(sign1, sign2):

    sign_dict = {
        "Aries": 1,
        "Taurus": 2,
        "Gemini": 3,
        "Cancer": 4,
        "Leo": 5,
        "Virgo": 6,
        "Libra": 7,
        "Scorpio": 8,
        "Sagittarius": 9,
        "Capricorn": 10,
        "Aquarius": 11,
        "Pisces": 12,
    }

    compatibility_dict = {
        0: "100%",
        1: "40%",
        2: "80%",
        3: "30%",
        4: "90%",
        5: "20%",
        6: "50%"
    }

    # if(sign_dict[sign1] < sign_dict[sign2]):
    #     diff = sign_dict[sign2] - sign_dict[sign1]
    #     return compatibility_dict[diff]
    
    # else:
    #     diff = (sign_dict[sign1] + sign_dict[sign2]) % len(sign_dict)

    #     return compatibility_dict[diff]
    

    back_diff = abs(sign_dict[sign1] - sign_dict[sign2])
    forward_diff = sign_dict[sign1] % len(sign_dict) + sign_dict[sign2]

    return compatibility_dict[min(back_diff, forward_diff)]


"""

=> back_diff is fine: it's the direct difference between the two positions.
=> forward_diff is wrong.You're adding indices instead of computing the circular distance.
    -> For example, Aries (1) and Pises(12):
        -> back_diff = 11
        -> forward_diff = 1 % 12 + 12 = 13
        -> min(11, 13) = 11 -> but the correct shortest distance is 1 (wrap around).
"""

def horoscope_match2(sign1, sign2):

    signs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
            "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
    

    s1, s2 = signs.index(sign1), signs.index(sign2)
    diff = abs(s1 - s2)
    distance = min(diff, 12 - diff)


    mapping = {
        0: "100%",
        1: "40%",
        2: "80%",
        3: "30%",
        4: "90%",
        5: "20%",
        6: "50%"
    }

    return mapping[distance]


""" 
=> The zodiac wheel is circular, so you always take the shortest path between two signs.
=> Distances beyond 6 wrap around(e.g., Aries , Pisces is distances 1).
=> Compatibility is a direct lookup from the distance.
"""

def horoscope_match3(sign1, sign2):
    sign_dict = {
        "Aries": 0, "Taurus": 1, "Gemini": 2, "Cancer": 3,
        "Leo": 4, "Virgo": 5, "Libra": 6, "Scorpio": 7,
        "Sagittarius": 8, "Capricorn": 9, "Aquarius": 10, "Pisces": 11
    }

    compatibility_dict = {
        0: "100%",
        1: "40%",
        2: "80%",
        3: "30%",
        4: "90%",
        5: "20%",
        6: "50%"
    }

    diff = abs(sign_dict[sign1] - sign_dict[sign2])
    distance = min(diff, 12 - diff)  # shortest path around the wheel
    return compatibility_dict[distance]


""" 

=> Always compute distance = min(diff, 12 - diff) for circular structure.
=> The forward_diff was adding indices instead of wrapping around.
=> Switch to 0-based indices (0 - 11 instead of 1 - 12) also makes the math cleaner.

"""





from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark({"first": horoscope_match, "second": horoscope_match2, "third": horoscope_match3}, TESTCASES, 10000)


    unittest.main()