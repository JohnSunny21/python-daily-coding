"""

Navigator
On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

You always start on the "Home" page, which will not be included in the commands array.
Valid commands are:
"Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
"Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
"Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
"""

import unittest
import snoop

class NavigatorTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(navigate(["Visit About Us", "Back", "Forward"]),"About Us")

    def test2(self):
        self.assertEqual(navigate(["Back"]),"Home")

    def test3(self):
        self.assertEqual(navigate("Forward"),"Home")

    def test4(self):
        self.assertEqual(navigate(["Visit About Us", "Visit Gallery"]),"Gallery")

    def test5(self):
        self.assertEqual(navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]),"Home")

    def test6(self):
        self.assertEqual(navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]),"Contact")

    def test7(self):
        self.assertEqual(navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]),"Visit Us")


def navigate(commands):
    pointer = 0
    current = ["Home"]
    
    for command in commands:
        if command.startswith("Visit "):
            page = command[6:]

            # Discard forward history

            current = current[:pointer + 1]
            
            current.append(page)
            pointer += 1
        elif command == "Back":
            if pointer > 0:
                pointer -= 1
        elif command == "Forward":
            if pointer < len(current) - 1:
                pointer += 1
        
        
    return current[pointer]


@snoop
def navigate(commands):
    back_stack = []
    forward_stack = []
    current = "Home"

    for command in commands:
        if command.startswith("Visit "):
            page = command[6:]
            back_stack.append(current)
            current = page
            forward_stack.clear()
        elif command == "Back":
            if back_stack:
                forward_stack.append(current)
                current = back_stack.pop()
        elif command == "Forward":
            if forward_stack:
                back_stack.append(current)
                current = forward_stack.pop()

    return current




if __name__ == "__main__":
    print(navigate(["Visit About us","Back","Forward"]))
    # print(navigate(["Forward"]))
    # print(navigate_optimized(["Visit About Us","Visit Visit Us", "Forward","Visit Contact Us","Back"]))
    # unittest.main()