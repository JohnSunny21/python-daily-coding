"""  

Scaled Image
Given a string representing the width and height of an image, and a number to scale the image, return the scaled width and height.

The input string is in the format "WxH". For example, "800x600".
The scale is a number to multiply the width and height by.
Return the scaled dimensions in the same "WxH" format.
"""

import unittest

class ScaledImageTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(scale_image("800x600", 2), "1600x1200")

    def test2(self):
        self.assertEqual(scale_image("100x100", 10), "1000x1000")

    def test3(self):
        self.assertEqual(scale_image("1024x768", 0.5), "512x384")

    def test4(self):
        self.assertEqual(scale_image("300x200", 1.5), "450x300")





def scale_image(size, scale):
    
    width, height = size.split("x")

    scaled_width = int(int(width) * scale)
    scaled_height = int(int(height) * scale)


    return f"{scaled_width}x{scaled_height}"

"""
This solution is straightforward logic.
Correctly splits the input string into width and height.

But there are some minor issue with this code anyway.

1. Double int() conversion.
    we used double int(int(width) * scale). The inner int(width) is necessary, but the outer int() truncates decimals.

    -> Example: "800x600", scale = 0.5 -> 400x300
    -> But for "800x600", scale - 0.333... -> 266x200 (truncated, not roundedt)
    we can use the round instead int() to avoid the truncate.

2. And we can also add the guard clause:
    if 'x' not in size:
    

"""


def scale_image(size, scale):

    if "x" not in size:
        raise ValueError("Invalid format, expected, 'WxH'")

    width, height = map(int, size.split('x'))

    scaled_width = int(width * scale)
    scaled_height = int(height * scale)

    return f"{scaled_width}x{scaled_height}"



import re

def scale_image(size, scale):

    match = re.match(r'^(\d+)x(\d+)$', size)

    if not match:
        raise ValueError("Invalid format, expected 'WxH'")
    
    width, height = map(int, match.groups())
    scaled_width = round(width * scale)
    scaled_height = round(height * scale)

    return f"{scaled_width}x{scaled_height}"


if __name__ == "__main__":
    unittest.main()