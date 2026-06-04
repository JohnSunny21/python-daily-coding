""" 
Schema Validator Part 4
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
Extra keys are allowed
"""


import unittest


class SchemaValidatorPart4Test(unittest.TestCase):



    def test1(self):
        self.assertEqual(is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True}), True)

    def test2(self):
        self.assertEqual(is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"}), True)

    def test3(self):
        self.assertEqual(is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55}), True)

    def test4(self):
        self.assertEqual(is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"}), False)

    def test5(self):
        self.assertEqual(is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True}), False)

    def test6(self):
        self.assertEqual(is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False}), False)

    def test7(self):
        self.assertEqual(is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True}), False)

    def test8(self):
        self.assertEqual(is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False}), False)


TESTCASES = [
    (({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True},), True),
    (({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"},), True),
    (({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55},), True),
    (({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"},), False),
    (({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True},), False),
    (({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False},), False),
    (({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True},), False),
    (({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False},), False)
]




def is_valid_schema(obj):

    roles = {"user", "creator", "moderator", "staff", "admin"}


    if not isinstance(obj, dict):
        return False
    
    if "username" not in obj or not isinstance(obj["username"], str):
        return False
    
    if "posts" not in obj or not isinstance(obj["posts"], (int, float)) or isinstance(obj["posts"], bool):
        return False
    
    if "verified" not in obj or not isinstance(obj["verified"], bool):
        return False
    
    if "role" not in obj or obj["role"] not in roles:
        return False
    
    if "supporter" in obj and not isinstance(obj["supporter"], bool):
        return False
    

    return True


"""
=> The testcase 
    -> is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True})

is returning True instead of False comes down to how Python treats bool and int.

In Python:

isinstance(True, int) # True
isinstance(False, int) # True

why?

=> bool is actuallly a subclass of int in Python.
=> True is essentially 1, and False is 0.
=> So when you check isinstance(obj["posts"]), int) ,it passes for True or False.
=> That's why your validator thinks "posts": True is valid

So i have added a check 
    -> if "posts" not in obj or not isinstance(obj["posts"], int) or isinstance(obj["posts"], bool):
    return False

    or more clearly:
    if "posts" not in obj or type(obj["posts"]) is not int:
         return False

    This way;
        -> type(True) is bool, not int
        -> Only actual integers like 5 or 42 will pass.

"""





from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": is_valid_schema},
        TESTCASES,
        10000
    )

    unittest.main()