""" 


URL Query Parser
Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.

The query string begins after the "?",
each parameter is separated by "&",
each key/value pair is separated by "="
For example, given "https://example.com/search?name=Alice&age=30", return:

{
  "name": "Alice",
  "age": "30"
}
All values should be returned as strings.


"""


import unittest


class UrlQueryParserTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(parse_url_query("https://example.com/search?name=Alice&age=30"), {"name": "Alice", "age": "30"})

    def test2(self):
        self.assertEqual(parse_url_query("https://freecodecamp.org/learn?skill=programming&language=python"), {"skill": "programming", "language": "python"})

    def test3(self):
        self.assertEqual(parse_url_query("https://freecodecamp.org/items?category=books&sort=asc&page=2"), {"category": "books", "sort": "asc", "page": "2"})

    def test4(self):
        self.assertEqual(parse_url_query("https://example.com?redirect=freecodecamp.org/learn&when=now"), {"redirect": "freecodecamp.org/learn", "when": "now"})


TESTCASES = [
    (("https://example.com/search?name=Alice&age=30",),{"name": "Alice", "age": "30"}),
    (("https://freecodecamp.org/learn?skill=programming&language=python",), {"skill": "programming", "language": "python"}),
    (("https://freecodecamp.org/items?category=books&sort=asc&page=2",), {"category": "books", "sort": "asc", "page": "2"}),
    (("https://example.com?redirect=freecodecamp.org/learn&when=now",), {"redirect": "freecodecamp.org/learn", "when": "now"})

]

def parse_url_query(url):

    _, query_parameters = url.split("?")

    parameters = query_parameters.split("&")
    
    result = {}

    for param in parameters:
        key, value = param.split("=")
        result[key] = value

    return result


def parse_query(url):

    result = {}

    if "?" not in url:
        return result
    
    query = url.split("?", 1)[1]
    params = query.split("&")

    for param in params:
        if "=" in param:
            key, value = param.split("=")
            result[key] = value
    return result




from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": parse_url_query,
         "second": parse_query},
        TESTCASES,
        10000
    )

    unittest.main()