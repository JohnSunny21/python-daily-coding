"""
Frontmatter Parser
Given a string representing a frontmatter block, parse it and return an object (JavaScript) or dictionary (Python) with the keys and values.

Frontmatter is wrapped in --- delimiters and contains key: value pairs within them, one per line. For example:

---
title: My Post
draft: false
views: 100
---
Should return:

{
  title: "My Post",
  draft: false,
  views: 100
}
Numbers, Booleans, and Strings should all be returned as their respective type.
The given string will have new lines separated with the newline character ("\n"). The above example would be given as: "---\ntitle: My Post\ndraft: false\nviews: 100\n---".
"""


import unittest


class FrontmatterParserTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---"), { "title": "My Post", "draft": False, "views": 100 })

    def test2(self):
        self.assertEqual(parse_frontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---"), { "id": "6a174db57256a112f932195c", "title": "My Book", "locale": "en", "wordCount": 10000, "published": False })

    def test3(self):
        self.assertEqual(parse_frontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---"), { "version": "1.0.0", "url": "https://example.com", "private": True })

    def test4(self):
        self.assertEqual(parse_frontmatter("---\nrating: 4.5\nprice: 9.99\n---"), { "rating": 4.5, "price": 9.99 })


TESTCASES = [
    (("---\ntitle: My Post\ndraft: false\nviews: 100\n---",), { "title": "My Post", "draft": False, "views": 100 }),
    (("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---",), { "id": "6a174db57256a112f932195c", "title": "My Book", "locale": "en", "wordCount": 10000, "published": False }),
    (("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---",), { "version": "1.0.0", "url": "https://example.com", "private": True }),
    (("---\nrating: 4.5\nprice: 9.99\n---",), { "rating": 4.5, "price": 9.99 })
]



def parse_frontmatter(s):

    s = s.replace("---\n", "").replace("\n---","")

    result = {}

    lis = s.split("\n")

    for item in lis:
        key, value = item.split(": ")

        if value.isdigit():
            result[key] = int(value)
        elif value.lower() == "true":
            result[key] = True
        elif value.lower() == "false":
            result[key] = False
        else:
            try:
                result[key] = float(value)
            except ValueError:
                result[key] = value
    return result

""" 

=> The replace("---\n", "").replace("\n---", "") works, but it assumes the delimieters are exactly in that format. A safer appraoch is to strip the first and last lines
    if they equal "---".
=> Overall, this is clean and efficient.
"""



def parse_frontmatter2(text):

    lines = text.strip().split("\n")
    if lines[0] == "---":
        lines = lines[1:]
    if lines[-1] == "---":
        lines = lines[:-1]

    result = {}

    for line in lines:
        if ": " in line:
            key, value = line.split(": ", 1)

            if value.lower() == "true":
                result[key] = True
            elif value.lower() == "false":
                result[key] = False
            elif value.isdigit():
                result[key] = int(value)
            else:
                try:
                    result[key] = float(value)
                except ValueError:
                    result[key] = value

    return result


from utils.benchmark import benchmark


if __name__ == "__main__":
    scores = benchmark(
        {"first": parse_frontmatter,
         "second": parse_frontmatter2},
        TESTCASES,
        10000
    )
    unittest.main()
