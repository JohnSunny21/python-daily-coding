"""
Acronym Finder
Given a string representing an acronym, return the full name of the organization it belongs to from the list below:

"National Avocado Storage Authority"
"Cats Infiltration Agency"
"Fluffy Beanbag Inspectors"
"Department Of Jelly"
"Wild Honey Organization"
"Eating Pancakes Administration"
Each letter in the given acronym should match the first letter of each word in the organization it belongs to, in the same order.
"""

import unittest


class AcronymFinderTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(find_org("NASA"), "National Avocado Storage Authority")

    def test2(self):
        self.assertEqual(find_org("CIA"), "Cats Infiltration Agency")

    def test3(self):
        self.assertEqual(find_org("FBI"), "Fluffy Beanbag Inspectors")

    def test4(self):
        self.assertEqual(find_org("DOJ"), "Department Of Jelly")

    def test5(self):
        self.assertEqual(find_org("WHO"), "Wild Honey Organization")

    def test6(self):
        self.assertEqual(find_org("EPA"), "Eating Pancakes Administration")


TESTCASES = [
    (("NASA",), "National Avocado Storage Authority"),
    (("CIA",), "Cats Infiltration Agency"),
    (("FBI",), "Fluffy Beanbag Inspectors"),
    (("DOJ",), "Department Of Jelly"),
    (("WHO",), "Wild Honey Organization"),
    (("EPA",), "Eating Pancakes Administration")
]




def find_org(acronym):

    acr = {
        "NASA": "National Avocado Storage Authority",
        "CIA": "Cats Infiltration Agency",
        "FBI": "Fluffy Beanbag Inspectors",
        "DOJ": "Department Of Jelly",
        "WHO": "Wild Honey Organization",
        "EPA": "Eating Pancakes Administration"
    }

    return acr.get(acronym, None)


def acronym_find(acronym: str) -> str:

    organizations = [
        "National Avocado Storage Authority",
        "Cats Infiltration Agency",
        "Fluffy Beanbag Inspectors",
        "Department Of Jelly",
        "Wild Honey Organization",
        "Eating Pancakes Administration"
    ]

    acronym = acronym.upper()

    for org in organizations:

        org_acronym = "".join([w[0].upper() for w in org.split() if w[0].isalpha()])
        if org_acronym == acronym:
            return org
        

    return "No match found"


""" 

The dictionary based approach is perfectly valid - it's essentially a direct lookup table

=> The dictionary version:
    -> Very concise.
    -> Constant-time lookup (O(1)).
    -> Easy to read and maintain if the list of organizations is fixed and small.

=> The dynamic acronym builder:
    -> More flexible  - it can handle new organizations without manually updating the dictionary.
    -> Slightly more complex logic, but scales better if the list changes often.

For this specific challenge (with a fixed set of six organizations) , the first dictionary solution is arguably the cleanest and most efficient. In an 
interview, can be said like 
 
-> If the dataset is static, I'd use a dictionary for direct lookup.
-> If the dataset is dynamic, I'd generate acroyms on the fly.
"""

from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": find_org,
         "second": acronym_find},
        TESTCASES,
        10000
    )

    unittest.main()