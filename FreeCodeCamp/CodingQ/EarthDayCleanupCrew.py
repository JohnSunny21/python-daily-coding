""" 


Earth Day Cleanup Crew
Today is Earth Day. Given an array of items you cleaned up, return your total cleanup score based on the rules below.

Given items will be one of:

Item	Base Value
"bottle"	10
"can"	6
"bag"	8
"tire"	35
"straw"	4
"cardboard"	3
"newspaper"	3
"shoe"	12
"electronics"	25
"battery"	18
"mattress"	38
A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items do not get a streak bonus.

Streak bonus: If the same item appears consecutively, it gets increasing bonus points.

First consecutive occurrence: base value
Second: base value + 1
Third: base value + 2
etc.
Fifth Item Multiplier: Every fifth item collected gets a multiplier.

Fifth item: *2
Tenth item: *3
etc.
Apply the multiplier after calculating any bonuses.
"""


import unittest

class EarthDayCleanupCrewTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_cleanup_score(["bottle", "straw", "shoe", "battery"]), 44)

    def test2(self):
        self.assertEqual(get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]), 58)

    def test3(self):
        self.assertEqual(get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]), 79)

    def test4(self):
        self.assertEqual(get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]), 358)

    def test5(self):
        self.assertEqual(get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"]), 383)


TESTCASES = [
    ((["bottle", "straw", "shoe", "battery"],), 44),
    ((["electronics", "straw", "newspaper", "bottle", "bag"],), 58),
    ((["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"],), 79),
    ((["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]],), 358),
    ((["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"],), 383)
]




def cleanup_score(items):

    total_cleanup_score = 0
    consec_multiplier = 0

    items_dict = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38
    }

    for i in range(len(items)):

        if i % 5 == 0 and i > 0:
            if isinstance(items[i], list):
                if items[i][0] == "rare":
                    current_sum = items[i][1]
                    multiplier = i // 5 + 1
                    total_cleanup_score += current_sum * multiplier

        
            multiplier = i // 5 + 1
            total_cleanup_score += items_dict[items[i]] * multiplier

        elif isinstance(items[i], list):
            if items[i][0] == "rare":
                total_cleanup_score += items[i][1]



        elif i < len(items) - 1 and  items[i] == items[i+1]:
                
                current_sum = items_dict[items[i]] + consec_multiplier + items_dict[items[i+1]] + consec_multiplier + 1
                consec_multiplier += 1
                total_cleanup_score += current_sum
            


        
        else:
            consec_multiplier = 0
            total_cleanup_score += items_dict[items[i]]


    return total_cleanup_score

"""
The problem misunderstood and made an incomplete solution
"""



def get_cleanup_score(items):
    base_values = {
        "bottle": 10, "can": 6, "bag": 8, "tire": 35,
        "straw": 4, "cardboard": 3, "newspaper": 3,
        "shoe": 12, "electronics": 25, "battery": 18,
        "mattress": 38
    }

    total = 0
    streak_item = None
    streak_count = 0

    for i, item in enumerate(items, start=1):
        # Handle rare items
        if isinstance(item, list) and item[0] == "rare":
            value = item[1]
            streak_item = None
            streak_count = 0
        else:
            # Base value
            value = base_values[item]

            # Streak bonus
            if item == streak_item:
                streak_count += 1
                value += streak_count
            else:
                streak_item = item
                streak_count = 0  # first occurrence, no bonus

        # Fifth item multiplier
        if i % 5 == 0:
            multiplier = (i // 5) + 1
            value *= multiplier

        total += value

    return total





from utils.benchmark import benchmark

if __name__ == "__main__":

    # print(get_cleanup_score(["bottle", "straw", "shoe", "battery"]))
    print(get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]))
    scores = benchmark({
        "first": get_cleanup_score
    },
    TESTCASES,
    10000)

    unittest.main()