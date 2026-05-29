""" 

Wider Aspect Ratio
Given two strings for different image dimensions, return the aspect ratio of the image with a greater width-to-height ratio.

The given strings will be in the format "WxH", for example, "1920x1080".
The aspect ratio is the ratio of width to height, reduced to the lowest whole numbers. For example, "1920x1080" reduces to "16:9".
Return a string in format "W:H", for example, "16:9".
"""


import unittest

class WiderAspectRatioTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(get_wider_aspect_ratio("1920x1080", "800x600"), "16:9")

    def test2(self):
        self.assertEqual(get_wider_aspect_ratio("1080x1350", "2048x1536"), "4:3")

    def test3(self):
        self.assertEqual(get_wider_aspect_ratio("640x480", "2440x1220"), "2:1")

    def test4(self):
        self.assertEqual(get_wider_aspect_ratio("360x640", "1080x1920"), "9:16")

    def test5(self):
        self.assertEqual(get_wider_aspect_ratio("3440x1440", "2048x858"), "43:18")

    def test6(self):
        self.assertEqual(get_wider_aspect_ratio("12345x61234", "12534x51234"), "2089:8539")


TESTCASES = [
    (("1920x1080", "800x600",), "16:9"),
    (("1080x1350", "2048x1536",), "4:3"),
    (("640x480", "2440x1220",), "2:1"),
    (("360x640", "1080x1920",), "9:16"),
    (("3440x1440", "2048x858",), "43:18"),
    (("12345x61234", "12534x51234",), "2089:8539")
]




def gcd(a, b):

    while(b != 0):
        a, b = b, a % b
    
    return a



def get_wider_aspect_ratio(a, b):

    first_image_width, first_image_height = map(int, a.split("x"))
    second_image_width, second_image_height = map(int, b.split("x"))


    first_image_width_ratio = first_image_width / first_image_height
    second_image_width_ratio = second_image_width / second_image_height

    if first_image_width_ratio > second_image_width_ratio:
        gcdVAlue = gcd(first_image_width, first_image_height)
        return f"{first_image_width // gcdVAlue}:{first_image_height // gcdVAlue}"
    
    else:
        gcdVAlue = gcd(second_image_width, second_image_height)
        return f"{second_image_width // gcdVAlue}:{second_image_height // gcdVAlue}"
    


import math

def parse_dimension(dim):
    w, h = map(int, dim.split("x"))

    return w, h

def reduce_ratio(w, h):
    g = math.gcd(w, h)
    return f"{w // g}:{h//g}"

def wider_aspect_ratio(dim1, dim2):
    w1, h1 = parse_dimension(dim1)
    w2, h2, =  parse_dimension(dim2)

    ratio1 = w1 / h1
    ratio2 = w2 / h2

    if ratio1 > ratio2:
        return reduce_ratio(w1, h1)
    else:
        return reduce_ratio(w2, h2)






from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark(
        {"first": get_wider_aspect_ratio,
         "second": wider_aspect_ratio},
        TESTCASES,
        10000
    )
    unittest.main()