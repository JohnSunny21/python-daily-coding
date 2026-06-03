""" 


Schema Validator Part 3
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
Extra keys are allowed
"""


import unittest


class SchemaValidatorPart3Test(unittest.TestCase):



    def test1(self):
        self.assertEqual(is_valid_schema({"username": "henry", "posts": 0, "verified": True, "role": "staff"}), True)

    def test2(self):
        self.assertEqual(is_valid_schema({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70}), True)

    def test3(self):
        self.assertEqual(is_valid_schema({"username": "penelope", "posts": 20, "verified": True, "role": "admin"}), True)

    def test4(self):
        self.assertEqual(is_valid_schema({"username": "kevin", "posts": 0, "verified": False, "role": "user"}), True)

    def test5(self):
        self.assertEqual(is_valid_schema({"username": "george", "posts": 15, "verified": True, "role": "moderator"}), True)

    def test6(self):
        self.assertEqual(is_valid_schema({"username": "david", "posts": 0, "verified": False, "role": "guest"}), False)

    def test7(self):
        self.assertEqual(is_valid_schema({"username": "wendy", "posts": 10, "verified": True}), False)

    def test8(self):
        self.assertEqual(is_valid_schema({"username": "fabian", "posts": 1, "verified": True, "role": True}), False)

    def test9(self):
        self.assertEqual(is_valid_schema({"username": 8, "posts": 1, "verified": True, "role": "user"}), False)

    def test10(self):
        self.assertEqual(is_valid_schema({"username": "penny", "posts": "10", "verified": True, "role": "staff"}), False)

    def test11(self):
        self.assertEqual(is_valid_schema({"username": "john", "posts": "1", "verified": "true", "role": "admin"}), False)


TESTCASES = [
    (({"username": "henry", "posts": 0, "verified": True, "role": "staff"},), True),
    (({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70},), True),
    (({"username": "penelope", "posts": 20, "verified": True, "role": "admin"},), True),
    (({"username": "kevin", "posts": 0, "verified": False, "role": "user"},), True),
    (({"username": "george", "posts": 15, "verified": True, "role": "moderator"},), True),
    (({"username": "david", "posts": 0, "verified": False, "role": "guest"},), False),
    (({"username": "wendy", "posts": 10, "verified": True},), False),
    (({"username": "fabian", "posts": 1, "verified": True, "role": True},), False),
    (({"username": 8, "posts": 1, "verified": True, "role": "user"},), False),
    (({"username": "penny", "posts": "10", "verified": True, "role": "staff"},), False),
    (({"username": "john", "posts": "1", "verified": "true", "role": "admin"},), False)
]




def is_valid_schema(obj):


    roles = {"user", "creator", "moderator", "staff", "admin"}

    if not isinstance(obj, dict):
        return False

    return (
        "username" in obj and isinstance(obj["username"], str) and
        "posts" in obj and isinstance(obj["posts"], (int, float)) and
        "verified" in obj and isinstance(obj["verified"], bool) and
        "role" in obj and obj["role"] in roles
    )


def is_valid_schema_2(obj):
    roles = {"user", "creator", "moderator", "staff", "admin"}

    if not isinstance(obj, dict):
        return False

    if not "username" in obj or not isinstance(obj["username"], str):
        return False
    
    if not "posts" in obj or not isinstance(obj["posts"], (int, float)):
        return False

    if not "verified" in obj or not isinstance(obj["verified"], bool):
        return False

    if not "role" in obj or obj["role"] not in roles:
        return False


    return True

"""
=> In Python, we check membership in a set.
=> Python isinstance() expects the second argument to be either a single type or a typle of types.
=> A list is not allowed - Python will raise a TypeError.
"""


from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": is_valid_schema,
         "second": is_valid_schema_2},
         TESTCASES,
         10000
    )

    unittest.main()