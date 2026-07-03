""" 

Database Migration
Given two database objects, return the second object with any missing properties from the first filled in.

Fields that already exist in the record should not be overwritten.
"""


import unittest


class DatabaseMigrationTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(migrate_record({ "username": "", "posts": 0 }, { "verified": True }), { "username": "", "posts": 0, "verified": True })

    def test2(self):
        self.assertEqual(migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "posts": 5 }), { "username": "camper", "posts": 5 })

    def test3(self):
        self.assertEqual(migrate_record({ "username": "", "posts": 0, "verified": False }, { "username": "camper" }), { "username": "camper", "posts": 0, "verified": False })

    def test4(self):
        self.assertEqual(migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "role": "admin" }), { "username": "camper", "role": "admin", "posts": 0 })

    def test5(self):
        self.assertEqual(migrate_record({ "username": "", "email": "", "posts": 0, "verified": False,"role": "user", "banned": False }, { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin" }), { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin", "posts": 0, "verified": False, "banned": False})


TESTCASES = [
    (({ "username": "", "posts": 0 }, { "verified": True },), { "username": "", "posts": 0, "verified": True }),
    (({ "username": "", "posts": 0 }, { "username": "camper", "posts": 5 },), { "username": "camper","posts": 5 }),
    (({ "username": "", "posts": 0, "verified": False }, { "username": "camper" },), { "username": "camper", "posts": 0, "verified": False }),
    (({ "username": "", "posts": 0 }, { "username": "camper", "role": "admin" },), { "username": "camper", "role": "admin", "posts": 0 }),
    (({ "username": "", "email": "", "posts": 0, "verified": False, "role": "user", "banned": False }, { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin" },), { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin", "posts": 0, "verified": False, "banned": False})
]





def migrate_record(schema, record):

    for key in schema.keys():
        if key in record:
            pass
        else:
            record[key] = schema[key]

    return record


def migrate_db(obj1, obj2):

    result = obj2.copy()

    for key, value in obj1.items():
        if key not in result:
            result[key] = value

    return result


from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark({"first": migrate_record, "second": migrate_db}, TESTCASES, 10000)

    unittest.main()