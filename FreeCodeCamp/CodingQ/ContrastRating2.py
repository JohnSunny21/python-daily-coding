""" 

Contrast Rating 2
Given two relative luminance values and a boolean indicating whether the text is large, return the WCAG contrast rating using the following method:

Calculate the contrast ratio by adding 0.05 to each luminance value, then dividing the lighter one by the darker one. The lighter one will always be the first argument.

Return the rating based on the contrast ratio using the following table:

Rating	Normal Text	Large Text
"AAA"	7.0+	4.5+
"AA"	4.5+	3.0+
"Fail"	below 4.5	below 3.0

"""


import unittest

class ContrastRating2Test(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_contrast_rating(1.0, 0.0, False), "AAA")

    def test2(self):
        self.assertEqual(get_contrast_rating(0.9015, 0.1364, False), "AA")

    def test3(self):
        self.assertEqual(get_contrast_rating(0.8965, 0.1628, False), "Fail")

    def test4(self):
        self.assertEqual(get_contrast_rating(0.7469, 0.0957, True), "AAA")

    def test5(self):
        self.assertEqual(get_contrast_rating(0.7489, 0.2018, True), "AA")

    def test6(self):
        self.assertEqual(get_contrast_rating(0.6571, 0.1974, True), "Fail")


TESTCASES = [
    ((1.0, 0.0, False,), "AAA"),
    ((0.9015, 0.1364, False,), "AA"),
    ((0.8965, 0.1628, False,), "Fail"),
    ((0.7469, 0.0957, True,), "AAA"),
    ((0.7489, 0.2018, True,), "AA"),
    ((0.6571, 0.1974, True,), "Fail")
]



def get_contrast_rating(l1, l2, is_large_text):

    l1 = l1 + 0.05
    l2 = l2 + 0.05

    # Ensure lighter is the larger value
    lighter = max(l1, l2)
    darker = min(l1, l2)

    # Contrast ratio
    ratio = lighter / darker


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

def contrast_rating(lighter, darker, is_large):

    ratio = (lighter + 0.05 ) / (darker + 0.05)

    if is_large:
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


    scores = benchmark({"first": get_contrast_rating, "second": contrast_rating}, TESTCASES, 10000)
    unittest.main()