""" 

Schema Validator Part 1
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

{
  username: string
}
Extra keys are allowed
"""




import unittest


class SchemaValidaotorPart1Test(unittest.TestCase):



    def test1(self):
        self.assertEqual(is_valid_schema({"username": "bob"}), True)

    def test2(self):
        self.assertEqual(is_valid_schema({"username": "jen", "posts": 30}), True)

    def test3(self):
        self.assertEqual(is_valid_schema({"username": ""}), True)

    def test4(self):
        self.assertEqual(is_valid_schema({"username": 7}), False)

    def test5(self):
        self.assertEqual(is_valid_schema({"posts": 25}), False)


TESTCASES = [
    (({"username": "bob"},), True),
    (({"username": "jen", "posts": 30},), True),
    (({"username": ""},), True),
    (({"username": 7},), False),
    (({"posts": 25},), False)
]





def is_valid_schema(obj):

    if not isinstance(obj, dict):
        return False
    
    for (key, value) in obj.items():
        if isinstance(key, str) and isinstance(value, str):
            return True
        
    return False



""" 
here the rules are 

-> The Object must have a key username.
-> The value of username must be a string.
-> Extra keys are allowed (we don't reject them).

but above solution doesn't quite match the schema requirement.

it returns true if any key is a string and any value is a string.
That means ["id": "123" ] would incorrectly pass, even through the schema requires specifically a "username" key.

The only thing we need to validate is:

1. The object has a key "username".
2. The value of "username" is a string.
3. Extra keys are allowed.

"""


def validate_schema(obj):


    if "username" in obj and isinstance(obj["username"], str):
        return True
    
    return False





from utils.benchmark import benchmark

if __name__ == "__main__":
    
    scores = benchmark(
        {"first": is_valid_schema,
         "second": validate_schema},
         TESTCASES,
         10000
    )

    unittest.main()