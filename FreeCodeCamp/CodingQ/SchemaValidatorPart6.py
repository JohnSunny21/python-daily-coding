""" 

Schema Validator Part 6
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

UserProfile = {
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

{
  users: UserProfile[]
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
UserProfile[] denotes an array of UserProfile objects. An empty array is valid.
Extra keys are allowed
"""


import unittest


class SchemaValidatorPart6Test(unittest.TestCase):



    def test1(self):
        self.assertEqual(is_valid_schema({"users": [{"username": "ron", "posts": 14, "verified": True, "role": "creator", "badges": ["early-adopter"]}, {"username": "cher", "posts": 25, "verified": True, "role": "moderator", "supporter": True, "followers": 20, "badges": ["helper"]}]}), True)

    def test2(self):
        self.assertEqual(is_valid_schema({"users": []}), True)

    def test3(self):
        self.assertEqual(is_valid_schema({"users": {"username": "anne", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}}), False)

    def test4(self):
        self.assertEqual(is_valid_schema({"users": [{"username": "tony", "posts": 10, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", 6]}]}), False)

    def test5(self):
        self.assertEqual(is_valid_schema({"users": [{"username": "ursula", "posts": 3, "verified": False, "role": "user", "supporter": "false", "badges": ["comeback"]}]}), False)

    def test6(self):
        self.assertEqual(is_valid_schema({"users": [{"username": "benny", "posts": 55, "verified": True, "role": "superstar", "supporter": True, "badges": ["veteran"]}]}), False)

    def test7(self):
        self.assertEqual(is_valid_schema({"users": [{"username": "chase", "posts": 1, "verified": "yes", "role": "staff", "supporter": False, "badges": ["superstar"]}]}), False)

    def test8(self):
        self.assertEqual(is_valid_schema({"users": [{"username": "carla", "posts": "10", "verified": False, "role": "user", "supporter": False, "badges": ["newbie"]}]}), False)

    def test9(self):
        self.assertEqual(is_valid_schema({"users": [{"posts": 4, "verified": False, "role": "admin", "supporter": False, "badges": ["superuser", "veteran"]}]}), False)

    def test10(self):
        self.assertEqual(is_valid_schema({"users": [{"username": "harold", "posts": 80, "verified":True, "role": "creator", "supporter": True, "badges": ["liked", "hero"]}, {"username": "kim", "posts": 11, "verified": False, "role": "admin", "supporter": True, "badges": ["first"]}, {}]}), False)


TESTCASES = [
    (({"users": [{"username": "ron", "posts": 14,"verified": True, "role": "creator", "badges": ["early-adopter"]}, {"username": "cher", "posts": 25, "verified": True, "role": "moderator", "supporter": True, "followers": 20, "badges": ["helper"]}]},), True),
    (({"users": []},), True),
    (({"users": {"username": "anne", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}},), False),
    (({"users": [{"username": "tony", "posts": 10, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", 6]}]},), False),
    (({"users": [{"username": "ursula", "posts": 3, "verified": False, "role": "user", "supporter":"false", "badges": ["comeback"]}]},), False),
    (({"users": [{"username": "benny", "posts": 55, "verified": True, "role": "superstar", "supporter": True, "badges": ["veteran"]}]},), False),
    (({"users": [{"username": "chase", "posts": 1, "verified": "yes", "role": "staff", "supporter":False, "badges": ["superstar"]}]},), False),
    (({"users": [{"username": "carla", "posts": "10", "verified": False, "role": "user", "supporter": False, "badges": ["newbie"]}]},), False),
    (({"users": [{"posts": 4, "verified": False, "role": "admin", "supporter": False, "badges": ["superuser", "veteran"]}]},), False),
    (({"users": [{"username": "harold", "posts": 80, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", "hero"]}, {"username": "kim", "posts": 11, "verified": False, "role": "admin", "supporter": True, "badges": ["first"]}, {}]},), False)
]



def is_valid_userprofile(obj):

    roles = {"user", "creator", "moderator", "staff", "admin"}

    if not isinstance(obj, dict):
        return False
    
    if "username" not in obj or not isinstance(obj["username"], str):
        return False
    
    if "posts" not in obj or not isinstance(obj["posts"], (int, float)) or isinstance(obj["posts"], bool):
        return False
    
    if "verified" not in obj or not  isinstance(obj["verified"], bool):
        return False
    
    if "role" not in obj or obj["role"] not in roles:
        return False
    
    if "supporter" in obj and not isinstance(obj["supporter"], bool):
        return False
    
    if "badges" not in obj or not isinstance(obj["badges"], list):
        return False
    
    if not all(isinstance(b, str) for b in obj["badges"]):
        return False
    
    return True


def is_valid_schema(obj):

    if not isinstance(obj, dict):
        return False
    
    if "users" not in obj or not isinstance(obj["users"], list):
        return False
    
    return all(is_valid_userprofile(user) for user in obj["users"])





from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": is_valid_schema}, TESTCASES, 10000)
    unittest.main()
