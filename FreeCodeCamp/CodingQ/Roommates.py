""" 

Roommates
Given an array of people and their roommate group, return the room assignments for a hotel stay using the following rules:

Each person has a name and a group property:
[
  { "name": "Alice", "group": "A" },
  { "name": "Bob", "group": "B" },
  { "name": "Carol", "group": "A" }
]
People can only share a room with someone from the same group and are paired in the order they are given.
Return an array of strings with names separated by " and " for a shared room, and just the name for a solo room. Names must appear in the order they were paired. For the example above, return ["Alice and Carol", "Bob"].
"""


import unittest

class RoommatesTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_roommates([{ "name": "Alice", "group": "A" }, { "name": "Bob", "group": "B" }, { "name": "Carol", "group": "A" }]), ["Alice and Carol", "Bob"])

    def test2(self):
        self.assertEqual(get_roommates([{ "name": "John", "group": "C" }, { "name": "Julia", "group": "C" }, { "name": "Jim", "group": "C" }]), ["John and Julia", "Jim"])

    def test3(self):
        self.assertEqual(get_roommates([{ "name": "Adam", "group": "D" }, { "name": "Abraham", "group": "E" }, { "name": "Austin", "group": "E" },{ "name": "Augustus", "group": "D" }, { "name": "Angelica", "group": "D" }, { "name": "Aaron", "group": "E" }]), ["Adam and Augustus", "Angelica","Abraham and Austin", "Aaron"])

    def test4(self):
        self.assertEqual(get_roommates([{ "name": "Frank", "group": "A" }, { "name": "Emitt", "group": "B" }, { "name": "Daria", "group": "F" }, {"name": "Charles", "group": "D" }, { "name": "Bailey", "group": "A" }, { "name": "Albert", "group": "F" }]), ["Frank and Bailey", "Emitt", "Daria and Albert", "Charles"])

    def test5(self):
        self.assertEqual(get_roommates([{ "name": "Kevin", "group": "A" }, { "name": "Yuri", "group": "A" }, { "name": "Hugo", "group": "B" }, { "name": "Violet", "group": "A" }, { "name": "Brett", "group": "A" }, { "name": "Wayne", "group": "B" }]), ["Kevin and Yuri", "Violet and Brett", "Hugo and Wayne"])


TESTCASES = [
    (([{ "name": "Alice", "group": "A" }, { "name": "Bob", "group": "B" }, { "name": "Carol", "group": "A" }],), ["Alice and Carol", "Bob"]),
    (([{ "name": "John", "group": "C" }, { "name": "Julia", "group": "C" }, { "name": "Jim", "group": "C" }],), ["John and Julia", "Jim"]),
    (([{ "name": "Adam", "group": "D" }, { "name": "Abraham", "group": "E" }, { "name": "Austin", "group": "E" },{ "name": "Augustus", "group": "D" }, { "name": "Angelica", "group": "D" }, { "name": "Aaron", "group": "E" }],), ["Adam and Augustus", "Angelica", "Abraham and Austin", "Aaron"]),
    (([{ "name": "Frank", "group": "A" }, { "name": "Emitt", "group": "B" }, { "name": "Daria", "group": "F" }, { "name": "Charles", "group": "D" }, { "name": "Bailey", "group": "A" }, { "name": "Albert", "group": "F" }],), ["Frank and Bailey", "Emitt", "Daria and Albert", "Charles"]),
    (([{ "name": "Kevin", "group": "A" }, { "name": "Yuri", "group": "A" }, { "name": "Hugo", "group": "B" }, { "name": "Violet", "group": "A" }, { "name": "Brett", "group": "A" }, { "name": "Wayne", "group": "B" }],), ["Kevin and Yuri", "Violet and Brett", "Hugo and Wayne"])
]






from collections import defaultdict


def get_roommates(people):

    result = defaultdict(list)

    for person in people:
            result[person["group"]].append(person["name"])

    # print(result)
    result_str = []

    for items in result.values():
        if len(items) % 2 == 0:
            result_str.extend(clear_items(items))
        else:
            result_str.extend(clear_items(items[:-1]))
            result_str.append(items[-1])
    

    return result_str
             
                       
              
def clear_items(items):
    
    temp_lis = []
    while items:
            
        temp_lis.append(" and ".join(items[:2]))
        items.pop(0)
        items.pop(0) 

    return temp_lis


def assign_rooms(people):

    rooms = []
    used = [False] * len(people)

    for i in range(len(people)):
        if used[i]:
            continue
        name_i, group_i = people[i]["name"], people[i]["group"]
        # Try to find a roommate later in the list
        roommate = None
        for j in range(i+1, len(people)):
            if not used[j] and people[j]["group"] == group_i:
                roommate = people[j]["name"]
                used[j] = True
                break
        if roommate:
            rooms.append(f"{name_i} and {roommate}")
        else:
            rooms.append(name_i)
        used[i] = True

    return rooms





from utils.benchmark import benchmark

if __name__ == "__main__":

    # get_roommates([{ "name": "Alice", "group": "A" }, { "name": "Bob", "group": "B" }, { "name": "Carol", "group": "A" }])
    print(get_roommates([{ "name": "Adam", "group": "D" }, { "name": "Abraham", "group": "E" }, { "name": "Austin", "group": "E" }, { "name": "Augustus", "group": "D" }, { "name": "Angelica", "group": "D" }, { "name": "Aaron", "group": "E" }]))

    # get_roommates([{ "name": "Kevi ", "group": "A" }, { "name": "Yuri", "group": "A" }, { "name": "Hugo", "group": "B" }, { "name": "Violet", "group": "A" }, { "name": "Brett", "group": "A" }, { "name": "Wayne", "group": "B" }])

    
    scores = benchmark(
        {"first": get_roommates,
         #"second": 
         }, 
        TESTCASES, 
        10000
    )

    unittest.main()