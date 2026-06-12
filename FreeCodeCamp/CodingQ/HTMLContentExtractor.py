"""

HTML Content Extractor
Given a string of HTML, return the plain text content with all tags removed.
"""

import unittest


class HTMLContentExtractorTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(extract_content('<p>hello world</p>'), "hello world")

    def test2(self):
        self.assertEqual(extract_content('<p>hello <span>world</span></p>'), "hello world")

    def test3(self):
        self.assertEqual(extract_content('<a href="example.com">Click me</a>'), "Click me")

    def test4(self):
        self.assertEqual(extract_content('<p><button onClick="learnToCode()">Learn</button> to <code>code<code> <br/>for <strong>free</strong> <br/>on <a href="https://freecodecamp.org/" target="_blank"><span class="highlight">freecodecamp</span>.org</a>'), "Learn to code for free on freecodecamp.org")

    def test5(self):
        self.assertEqual(extract_content('<div class="container"><h1 id="title">Welcome to <strong>My</strong> Website.</h1><p>This is a <a href="https://example.com" target="_blank">link</a> to something <em>really</em> <span class="highlight">important</span>.</p><ul><li>Item <strong>one</strong></li><li>Item <em>two</em></li><li>Item three</li></ul><img src="pic.jpg" alt="A picture"/><p class="footer">Contact us at <a href="mailto:hello@example.com">hello@example.com</a> for <span>more <strong>info</strong></span>.</p></div>'), "Welcome to My Website.This is a link to something really important.Item oneItem twoItem threeContact us at hello@example.com for more info.")


TESTCASES = [
    (('<p>hello world</p>',), "hello world"),
    (('<p>hello <span>world</span></p>',), "hello world"),
    (('<a href="example.com">Click me</a>',), "Click me"),
    (('<p><button onClick="learnToCode()">Learn</button> to <code>code<code> <br/>for <strong>free</strong> <br/>on <a href="https://freecodecamp.org/" target="_blank"><span class="highlight">freecodecamp</span>.org</a>',), "Learn to code for free on freecodecamp.org"),
    (('<div class="container"><h1 id="title">Welcome to <strong>My</strong> Website.</h1><p>This is a <a href="https://example.com" target="_blank">link</a> to something <em>really</em> <span class="highlight">important</span>.</p><ul><li>Item <strong>one</strong></li><li>Item <em>two</em></li><li>Item three</li></ul><img src="pic.jpg" alt="A picture"/><p class="footer">Contact us at <a href="mailto:hello@example.com">hello@example.com</a> for <span>more <strong>info</strong></span>.</p></div>',), "Welcome to My Website.This is a link to something really important.Item oneItem twoItem threeContact us at hello@example.com for more info.")
]



import re
def extract_content(html):

    text = re.sub(r"<.*?>","",html)

    return text




from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark(
        {
        "first": extract_content
        },
        TESTCASES,
        10000

    )
    unittest.main()