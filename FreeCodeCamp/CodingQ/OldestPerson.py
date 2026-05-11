""" 


Oldest Person
Given an array of objects, each with a "name" and "age" property, return an array containing the name of the oldest person.

If multiple people share the oldest age, return all of their names in the order they appear in the input.
"""

import unittest


class OldestPersonTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_oldest([{ "name": "Brenda", "age": 40 }]), ["Brenda"])

    def test2(self):
        self.assertEqual(get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]), ["Alice"])

    def test3(self):
        self.assertEqual(get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }]), ["Bill", "Carol"])

    def test4(self):
        self.assertEqual(get_oldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]), ["George", "Holly", "Zach"])


TESTCASES = [
    (([{ "name": "Brenda", "age": 40 }],), ["Brenda"]),
    (([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }],), ["Alice"]),
    (([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }],), ["Bill", "Carol"]),
    (([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }],), ["George", "Holly", "Zach"])
]





def get_oldest(people):
    
    result = []

    max_age = max(people, key=lambda x: x['age'])['age']

    for item in people:
        item_dict = dict(item)

        if item_dict['age'] == max_age:
            result.append(item_dict['name'])

    return result


def oldest_person(people):

    max_age = max(p['age'] for p in people)

    return [p["name"] for p in people if p["age"] == max_age]





from utils.benchmark import benchmark


if __name__ == "__main__":

    scores = benchmark(
        {"first": get_oldest
         ,"second": oldest_person},
        TESTCASES,
        10000
    )
    unittest.main()