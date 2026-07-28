""" 

Contrast Rating 1
Given a contrast ratio and a boolean indicating whether the text is large, return the WCAG rating using the following table:

Rating	Normal Text	Large Text
"AAA"	7.0+	4.5+
"AA"	4.5+	3.0+
"Fail"	below 4.5	below 3.0

"""


import unittest


class ContrastRating1Test(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_contrast_rating("7.5", False), "AAA")

    def test2(self):
        self.assertEqual(get_contrast_rating("4.8", False), "AA")

    def test3(self):
        self.assertEqual(get_contrast_rating("4.2", False), "Fail")

    def test4(self):
        self.assertEqual(get_contrast_rating("4.5", True), "AAA")

    def test5(self):
        self.assertEqual(get_contrast_rating("3.0", True), "AA")

    def test6(self):
        self.assertEqual(get_contrast_rating("2.7", False), "Fail")


TESTCASES = [
    (("7.5", False,), "AAA"),
    (("4.8", False,), "AA"),
    (("4.2", False,), "Fail"),
    (("4.5", True,), "AAA"),
    (("3.0", True,), "AA"),
    (("2.7", False,), "Fail")
]



def get_contrast_rating(ratio, is_large_text):

    ratio = float(ratio)

    if is_large_text:
        if ratio >= 4.5:
            return "AAA"
        elif ratio >= 3.0:
            return "AA"
        else:
            return "Fail"

    else:
        if ratio >= 7.0:
            return "AAA"
        elif ratio >= 4.5:
            return "AA"
        else:
            return "Fail"


from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark({"first": get_contrast_rating}, TESTCASES, 10000)
    unittest.main()