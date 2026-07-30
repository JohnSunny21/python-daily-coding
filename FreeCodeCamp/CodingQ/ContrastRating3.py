""" 

Contrast Rating 3
Given two arrays representing RGB values and a boolean indicating whether the text is large, return the WCAG contrast rating using the following method:

First, convert each RGB value to relative luminance:

Divide each channel [R, G, B] by 255 to get a value between 0 and 1
Apply the gamma correction formula to each channel:
If the channel value is less than or equal to 0.04045: channel / 12.92
Otherwise: ((channel + 0.055) / 1.055) ^ 2.4
Calculate luminance: 0.2126 * R + 0.7152 * G + 0.0722 * B
Then, calculate the contrast ratio by adding 0.05 to each luminance value, then dividing the lighter one by the darker one. The lighter one will always be the first argument.

Return the rating based on the contrast ratio using the following table:

Rating	Normal Text	Large Text
"AAA"	7.0+	4.5+
"AA"	4.5+	3.0+
"Fail"	below 4.5	below 3.0

"""


import unittest

class ContrastRating3Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_contrast_rating([255,255, 255], [0, 0, 0], False), "AAA")

    def test2(self):
        self.assertEqual(get_contrast_rating([215,188, 188], [55, 55, 55], False), "AA")

    def test3(self):
        self.assertEqual(get_contrast_rating([143,144, 210], [46, 47, 61], False), "Fail")

    def test4(self):
        self.assertEqual(get_contrast_rating([167,167, 210], [53, 10, 53], True), "AAA")

    def test5(self):
        self.assertEqual(get_contrast_rating([135,147, 155], [60, 70, 90], True), "AA")

    def test6(self):
        self.assertEqual(get_contrast_rating([125,210, 195], [105, 130, 90], True), "Fail")


TESTCASES = [
    (([255, 255, 255], [0, 0, 0], False,), "AAA"),
    (([215, 188, 188], [55, 55, 55], False,), "AA"),
    (([143, 144, 210], [46, 47, 61], False,), "Fail"),
    (([167, 167, 210], [53, 10, 53], True,), "AAA"),
    (([135, 147, 155], [60, 70, 90], True,), "AA"),
    (([125, 210, 195], [105, 130, 90], True,), "Fail")
]



def get_contrast_rating(rgb1, rgb2, is_large_text):

    RGB1 = []
    RGB2 = []


    for item in rgb1:
        temp = item / 255
        if temp <= 0.04045:
            channel = temp / 12.92
        else:
            channel = ((temp + 0.055) / 1.055) ** 2.4
        RGB1.append(channel)


    for item in rgb2:
        temp = item / 255

        if temp <= 0.04045:
            channel = temp / 12.92
        else:
            channel = ((temp + 0.055) / 1.055) ** 2.4
        RGB2.append(channel)


    R1, G1, B1 = RGB1
    R2, G2, B2 = RGB2

    l1 = 0.2126 * R1 + 0.7152 * G1 + 0.0722 * B1
    l2 = 0.2126 * R2 + 0.7152 * G2 + 0.0722 * B2

    lighter_luminance = max(l1, l2)
    darker_luminance = min(l1, l2)


    contrast_ratio = (lighter_luminance + 0.05) / (darker_luminance + 0.05)

    if is_large_text:
        if contrast_ratio >= 4.5:
            return "AAA"
        elif contrast_ratio >= 3.0:
            return "AA"
        else:
            return "Fail"
    else:
        if contrast_ratio >= 7.0:
            return "AAA"
        elif contrast_ratio >= 4.5:
            return "AA"
        else:
            return "Fail"


def get_contrast_rating2(rgb1, rgb2, is_large_text):

    def to_luminance(rgb):
        def channel(c):
            c = c / 255.0
            if c <= 0.04045:
                return c / 12.92
            else:
                return ((c + 0.055) / 1.055) ** 2.4
        R, G, B = rgb
        return 0.2126 * channel(R) + 0.7152 * channel(G) + 0.0722 * channel(B)


    l1 = to_luminance(rgb1)
    l2 = to_luminance(rgb2)

    lighter = max(l1, l2)
    darker = min(l1, l2)

    ratio = (lighter + 0.05) / (darker + 0.05)

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

    scores = benchmark({"first": get_contrast_rating, "second": get_contrast_rating2}, TESTCASES, 10000)
    unittest.main()