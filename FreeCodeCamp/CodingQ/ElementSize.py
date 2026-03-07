""" 

Element Size
Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.

The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.

"vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.

"vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window.
"""


import unittest

class ElementSizeTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(get_element_size("1200 x 800", "50vw", "50vh"), "600 x 400")

      def test2(self):
          self.assertEqual(get_element_size("320 x 480", "25vw", "50vh"), "80 x 240")

      def test3(self):
          self.assertEqual(get_element_size("1000 x 500", "7vw", "3vh"), "70 x 15")

      def test4(self):
          self.assertEqual(get_element_size("1920 x 1080", "95vw", "100vh"), "1824 x 1080")

      def test5(self):
          self.assertEqual(get_element_size("1200 x 800", "0vw", "0vh"), "0 x 0")

      def test6(self):
          self.assertEqual(get_element_size("1440 x 900", "100vw", "114vh"), "1440 x 1026")



def get_element_size(window_size, element_vw, element_vh):

    width, height = map(int, window_size.split(" x "))
    element_vw, _ = element_vw.split("vw")
    element_vh, _ = element_vh.split("vh")

    width_in_pixels = width * (int(element_vw) / 100)
    height_in_pixels = height * (int(element_vh) / 100)

    return f"{width_in_pixels:.0f} x {height_in_pixels:.0f}"


def element_size(window_size, element_width, element_height):

    win_w, win_h = map(int, window_size.split("x"))

    if element_width.endswith("vw"):
        w_percent = float(element_width[:-2])
        elem_w = int(win_w * (w_percent / 100))

    else:
        raise ValueError("Width must be in vw units")
    
    if element_height.endswith("vh"):
        h_percent = float(element_height[:-2])
        elem_h = int(win_h * (h_percent / 100))
    else:
        raise ValueError("Height must be in vh units")
    
    return f"{elem_w} x {elem_h}"


if __name__ == "__main__":
    print(get_element_size("1200 x 800", "50vw", "50vh"))
    unittest.main()