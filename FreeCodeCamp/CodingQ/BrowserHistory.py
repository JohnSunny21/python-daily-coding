""" 

Browser History
Given an array of browser commands, return an array with two values: the history as an array of URLs, and the index of the current page.

Valid commands are:

"URL" - Where URL is a web address ("freecodecamp.org" for example). Navigates to the given URL, adds it to the history at the next position, and discards any forward history.
"Back" - moves to the previous page in history, or stays on the current page if there isn't one.
"Forward" - moves to the next page in history, or stays on the current page if there isn't one.
For example, given ["freecodecamp.org", "freecodecamp.org/learn", "Back"], return [["freecodecamp.org", "freecodecamp.org/learn"], 0].
"""

import unittest

class BrowserHistoryTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_browser_history(["freecodecamp.org", "freecodecamp.org/learn", "Back"]), [["freecodecamp.org", "freecodecamp.org/learn"], 0])

    def test2(self):
        self.assertEqual(get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog"]), [["example.com", "example.com/about", "example.com/contact", "example.com/blog"], 3])

    def test3(self):
        self.assertEqual(get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"]), [["example.com", "example.com/contact", "example.com/blog"], 1])

    def test4(self):
        self.assertEqual(get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog", "Back", "Back", "Forward", "freecodecamp.org"]), [["example.com", "example.com/about", "example.com/contact", "freecodecamp.org"], 3])

    def test5(self):
        self.assertEqual(get_browser_history(["example.com", "example.com/about", "Back", "Back"]),  [["example.com", "example.com/about"], 0])   

    def test6(self):
        self.assertEqual(get_browser_history(["example.com", "example.com/about", "Forward"]), [["example.com", "example.com/about"], 1]) 





def get_browser_history(commands):
    history = []
    current = -1    # no page yet

    for cmd in commands:
        if cmd == "Back":
            if current > 0:
                current -= 1
        elif cmd == "Forward":
            if current < len(history) - 1:
                current += 1
        else:
            # It's a URL
            # discard forward history
            history = history[:current+1]
            history.append(cmd)
            current += 1


    return [history, current]



from utils.benchmark import benchmark
if __name__ == "__main__":


    TESTCASES = [
    ((["freecodecamp.org", "freecodecamp.org/learn", "Back"],), [["freecodecamp.org", "freecodecamp.org/learn"], 0]),
    ((["example.com", "example.com/about", "example.com/contact", "example.com/blog"],), [["example.com", "example.com/about", "example.com/contact", "example.com/blog"], 3]),
    ((["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"],), [["example.com", "example.com/contact", "example.com/blog"], 1]),
    ((["example.com", "example.com/about", "example.com/contact", "example.com/blog", "Back", "Back", "Forward", "freecodecamp.org"],), [["example.com", "example.com/about", "example.com/contact", "freecodecamp.org"], 3]),
    ((["example.com", "example.com/about", "Back", "Back"],), [["example.com", "example.com/about"], 0]),
    ((["example.com", "example.com/about", "Forward"],), [["example.com", "example.com/about"], 1])
]
    scores = benchmark(
        {"first": get_browser_history},
        TESTCASES,
        10000
    )
    unittest.main()
    