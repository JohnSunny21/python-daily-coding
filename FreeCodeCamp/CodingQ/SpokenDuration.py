""" 
Spoken Duration
Given a number of seconds, return the duration in spoken English.

Break the duration into hours, minutes, and seconds.
Skip any zero values.
Use singular or plural as appropriate ("1 hour", "2 hours").
If present, join the last two units with "and", and the second and third to last units with a comma ("1 hour, 2 minutes and 3 seconds").
"""

import unittest

class SpokenDurationTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_spoken_duration(3723), "1 hour, 2 minutes and 3 seconds")

    def test2(self):
        self.assertEqual(get_spoken_duration(7295), "2 hours, 1 minute and 35 seconds")

    def test3(self):
        self.assertEqual(get_spoken_duration(8521), "2 hours, 22 minutes and 1 second")

    def test4(self):
        self.assertEqual(get_spoken_duration(435),"7 minutes and 15 seconds")

    def test5(self):
        self.assertEqual(get_spoken_duration(14455), "4 hours and 55 seconds")

    def test6(self):
        self.assertEqual(get_spoken_duration(72000), "20 hours")

    def test7(self):
        self.assertEqual(get_spoken_duration(1), "1 second")


TESTCASES = [
    ((3723,), "1 hour, 2 minutes and 3 seconds"),
    ((7295,), "2 hours, 1 minute and 35 seconds"),
    ((8521,), "2 hours, 22 minutes and 1 second"),
    ((435,), "7 minutes and 15 seconds"),
    ((14455,), "4 hours and 55 seconds"),
    ((72000,), "20 hours"),
    ((1,), "1 second")
]


def get_spoken_duration(seconds):

    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    parts = []

    if hours:
        parts.append(f"{hours} hour" + ("s" if hours > 1 else ""))
    if minutes:
        parts.append(f"{minutes} minute" + ("s" if minutes > 1 else ""))
    if seconds:
        parts.append(f"{seconds} second" + ("s" if seconds > 1 else ""))

    if not parts:
        return "0 seconds"

    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    else:
        return f"{', '.join(parts[:-1])} and {parts[-1]}"


def get_spoken_duration2(seconds):

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    result = []

    if hours:
        result.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes:
        result.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
    if seconds:
        result.append(f"{seconds} {'second' if seconds == 1 else 'seconds'}")


    if not result:
        return "0 seconds"

    if len(result) == 1:
        return result[0]
    if len(result) == 2:
        return f"{result[0]} and {result[1]}"
    return f"{', '.join(result[:-1])} and {result[-1]}"




from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": get_spoken_duration, "second": get_spoken_duration2}, TESTCASES, 1000)
    unittest.main()