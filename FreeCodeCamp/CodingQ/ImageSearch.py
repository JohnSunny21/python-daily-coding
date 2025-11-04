"""

Image Search
On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

Given an array of image names and a search term, return an array of image names containing the search term.

Ignore the case when matching the search terms.
Return the images in the same order they appear in the input array.
"""

import unittest

class ImageSearchTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(image_search(["dog.png", "cat.jpg", "parrot.jpeg"],"dog"),["dog.png"])

    def test2(self):
        self.assertEqual(image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"],"sun"),["Sunset.jpg", "sunflower.jpeg"])

    def test3(self):
        self.assertEqual(image_search(["Moon.png", "sun.jpeg", "stars.png"],"PNG"),["Moon.png", "stars.png"])

    def test4(self):
        self.assertEqual(image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"],"Cat"),["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"])



def image_search(images,term):
    result = []
    for image in images:
        if term.lower() in image.lower():
            result.append(image)

    return result



if __name__ == "__main__":
    print(image_search(["dog.png", "cat.jpg", "parrot.jpeg"],"dog"))
    unittest.main()