""" 
Schema Validator Part 2
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

{
  username: string,
  posts: number,
  verified: boolean
}
Extra keys are allowed
"""


import unittest



class SchemaValidatorPart2Test(unittest.TestCase):



    def test1(self):
        self.assertEqual(is_valid_schema({"username": "alice", "posts": 10, "verified": False}), True)

    def test2(self):
        self.assertEqual(is_valid_schema({"username": "carol", "posts": 15, "verified": True, "followers": 25}), True)

    def test3(self):
        self.assertEqual(is_valid_schema({"username": "frank", "posts": "21", "verified": True}), False)

    def test4(self):
        self.assertEqual(is_valid_schema({"username": "sam", "posts": 17, "verified": "false"}), False)

    def test5(self):
        self.assertEqual(is_valid_schema({"username": "bill", "verified": True}), False)

    def test6(self):
        self.assertEqual(is_valid_schema({"username": "fred", "verified": True}), False)

    def test7(self):
        self.assertEqual(is_valid_schema({"username": 5, "posts": 10, "verified": True}), False)


TESTCASES = [
    (({"username": "alice", "posts": 10, "verified": False},), True),
    (({"username": "carol", "posts": 15, "verified": True, "followers": 25},), True),
    (({"username": "frank", "posts": "21", "verified": True},), False),
    (({"username": "sam", "posts": 17, "verified": "false"},), False),
    (({"username": "bill", "verified": True},), False),
    (({"username": "fred", "verified": True},), False),
    (({"username": 5, "posts": 10, "verified": True},), False)
]




def is_valid_schema(obj):

    if not "username" in obj or not isinstance(obj["username"], str):
        return False
    
    if not "posts" in obj or not isinstance(obj["posts"], int):
        return False
    
    if not "verified" in obj or not isinstance(obj["verified"], bool):
        return False
    
    return True


def is_valid_schema_2(obj):

    if not isinstance(obj, dict):
        return False
    
    return (
        "username" in obj and isinstance(obj["username"], str) and
        "posts" in obj and isinstance(obj["posts"], (int, float)) and
        "verified" in obj and isinstance(obj["verified"], bool)
    )








from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": is_valid_schema,
         "second": is_valid_schema_2},
        TESTCASES,
        10000
    )

    unittest.main()