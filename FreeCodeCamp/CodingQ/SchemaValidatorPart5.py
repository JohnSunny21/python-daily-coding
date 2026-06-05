""" 

Schema Validator Part 5
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
The brackets [] after string means that badges should be an array of strings (or empty).
Extra keys are allowed
"""


import unittest

class SchemaValidatorPart5Test(unittest.TestCase):



    def test1(self):
        self.assertEqual(is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False, "badges": ["early-adopter", "popular"]}), True)

    def test2(self):
        self.assertEqual(is_valid_schema({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True, "badges": ["streak-master", "veteran"], "followers": 1233}),True)

    def test3(self):
        self.assertEqual(is_valid_schema({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}), True)

    def test4(self):
        self.assertEqual(is_valid_schema({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False, "badges": ["first-post", 18]}), False)

    def test5(self):
        self.assertEqual(is_valid_schema({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False}), False)

    def test6(self):
        self.assertEqual(is_valid_schema({"username": "charlie", "posts": 0, "verified": False, "role": "user", "supporter": "no", "badges": ["first-post", "anniversary"]}), False)

    def test7(self):
        self.assertEqual(is_valid_schema({"username": "wanda", "posts": 15, "verified": True, "role": "friend", "supporter": True, "badges": ["popular"]}), False)

    def test8(self):
        self.assertEqual(is_valid_schema({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": True, "badges": ["helper"]}), False)

    def test9(self):
        self.assertEqual(is_valid_schema({"username": "carrie", "verified": True, "role": "moderator", "supporter": True, "badges": ["helper", "sharer"]}), False)

    def test10(self):
        self.assertEqual(is_valid_schema({"username": True, "posts": 75, "verified": True, "role": "creator", "supporter": True, "badges": ["veteran"]}), False)


TESTCASES = [
    (({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False,"badges": ["early-adopter", "popular"]},), True),
    (({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True, "badges": ["streak-master", "veteran"], "followers": 1233},), True),
    (({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []},), True),
    (({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False, "badges": ["first-post", 18]},), False),
    (({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False},), False),
    (({"username": "charlie", "posts": 0, "verified": False, "role": "user", "supporter": "no", "badges": ["first-post", "anniversary"]},), False),
    (({"username": "wanda", "posts": 15, "verified": True, "role": "friend", "supporter": True, "badges": ["popular"]},), False),
    (({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": True, "badges": ["helper"]},), False),
    (({"username": "carrie", "verified": True, "role": "moderator", "supporter": True, "badges": ["helper", "sharer"]},), False),
    (({"username": True, "posts": 75, "verified": True, "role": "creator", "supporter": True, "badges": ["veteran"]},), False)
]





def is_valid_schema(obj):

    if not isinstance(obj, dict):
        return False
    
    roles = {"user", "creator", "moderator", "staff", "admin"}


    if not "username" in obj or not isinstance(obj["username"], str):
        return False

    if not "posts" in obj or not isinstance(obj["posts"], (int, float)) or isinstance(obj["posts"], bool):
        return False

    if not "verified" in obj or not isinstance(obj["verified"], bool):
        return False

    if not "role" in obj or obj["role"] not in roles:
        return False
    
    if "supporter" in obj and not isinstance(obj["supporter"], bool):
        return False
    
    if not "badges" in obj or not isinstance(obj["badges"], list):
        return False
    
    if not all(isinstance(item, str) for item in obj["badges"]):
        return False


    return True




from utils.benchmark import benchmark

if __name__ == "__main__":
    scores = benchmark({
        "first": is_valid_schema
    },
    TESTCASES,
    10000)

    unittest.main()