""" 

Good Day
Given a time string in "HH:MM" format (24-hour clock), return:

"Good morning" for times 05:00 to 11:59
"Good afternoon" for times 12:00 to 17:59
"Good evening" for times 18:00 to 21:59
"Good night" for times 22:00 to 04:59
"""



import unittest


class GoodDayTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_greeting("06:30"), "Good morning")

    def test2(self):
        self.assertEqual(get_greeting("12:00"), "Good afternoon")

    def test3(self):
        self.assertEqual(get_greeting("21:59"), "Good evening")

    def test4(self):
        self.assertEqual(get_greeting("00:01"), "Good night")

    def test5(self):
        self.assertEqual(get_greeting("11:30"), "Good morning")


TESTCASES = [
    (("06:30",), "Good morning"),
    (("12:00",), "Good afternoon"),
    (("21:59",), "Good evening"),
    (("00:01",), "Good night"),
    (("11:30",), "Good morning")
]



def get_greeting(s):

    hour, minutes = map(int, s.split(":"))

    if hour >= 5 and hour <= 11:
        return "Good morning"
    elif hour >= 12 and hour <= 17:
        return "Good afternoon"
    elif hour >= 18 and hour <= 21:
        return "Good evening"
    else:
        return "Good night"
    




def good_day(s):

    hour, minutes = map(int, s.split(":"))

    if 5 <= hour <= 11:
        return "Good morning"
    elif 12 <= hour <= 17:
        return "Good afternoon"
    elif 18 <= hour <= 21:
        return "Good evening"
    else:
        return "Good night"
    





from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark(
        {"first": get_greeting,
         "second": good_day},
         TESTCASES,
         10000
    )

    unittest.main()
