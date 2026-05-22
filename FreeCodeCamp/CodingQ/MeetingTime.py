""" 

Meeting Time
Given a 3D array representing availability windows for multiple people, return the earliest time where everyone has one hour free. If no such time exists, return "None".

Each person's availability is an array of [start, end] integer pairs in 24-hour time. For example, [10, 12] would mean the person is available from 10 to 12. Start times range from 0-23, and end times range from 1-24.
For example, given:

[
  [[10, 12], [15, 16]], // person 1
  [[11, 14], [15, 16]]  // person 2
]
Return 11, the start of their first shared free hour.
"""


import unittest


class MeetingTimeTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_meeting_time([[[10, 12], [15, 16]], [[11, 14], [15, 16]]]), 11)

    def test2(self):
        self.assertEqual(get_meeting_time([[[9, 10], [12, 15]], [[10, 11], [13, 14]], [[9, 11], [10, 14]]]), 13)

    def test3(self):
        self.assertEqual(get_meeting_time([[[7, 8], [9, 11], [12, 14], [15, 16]], [[8, 11], [12, 13], [14, 15]]]), 9)

    def test4(self):
        self.assertEqual(get_meeting_time([[[7, 8], [10, 12], [13, 15]], [[8, 11], [12, 13], [14, 15]], [[6, 7], [8, 9], [12, 13]]]), "None")

    def test5(self):
        self.assertEqual(get_meeting_time([[[1, 3], [4, 6], [8, 10], [20, 23]], [[15, 16], [17, 18], [19, 22], [23, 24]], [[14, 16], [17, 23]], [[2, 4], [5, 6], [18, 19], [21, 22], [23, 24]]]), 21)


TESTCASES = [
    (([[[10, 12], [15, 16]], [[11, 14], [15, 16]]],), 11),
    (([[[9, 10], [12, 15]], [[10, 11], [13, 14]], [[9, 11], [10, 14]]],), 13),
    (([[[7, 8], [9, 11], [12, 14], [15, 16]], [[8, 11], [12, 13], [14, 15]]],), 9),
    (([[[7, 8], [10, 12], [13, 15]], [[8, 11], [12, 13], [14, 15]], [[6, 7], [8, 9], [12, 13]]],), "None"),
    (([[[1, 3], [4, 6], [8, 10], [20, 23]], [[15, 16], [17, 18], [19, 22], [23, 24]], [[14, 16], [17, 23]], [[2, 4], [5, 6], [18, 19], [21, 22], [23, 24]]],), 21)
]






def get_meeting_time_first(availability):

    possible = [(0, 24)]

    for person in availability:
        new_possible = []

        for interval in person:
            for p in possible:
                start = max(interval[0], p[0])
                end = min(interval[1], p[1])

                if start < end:
                    new_possible.append((start, end))

        possible = new_possible

    for start, end in sorted(possible):
        if end - start >= 1:
            return start

    return "None"


def get_meeting_time(availability):

    if not availability:
        return "None"
    
    common_hours = None

    for person in availability:
        hours = set()

        for start, end in person:
            for hour in range(start, end):
                hours.add(hour)

        if common_hours is None:
            common_hours = hours
        else:
            common_hours &= hours
    

    return min(common_hours) if common_hours else "None"

    
def get_meeting_time_cleaner(availability):

    common = None

    for person in availability:
        hours = set()

        for start, end in person:
            hours.update(range(start, end))

        common = hours if common is None else common & hours


    return min(common) if common else "None"


def get_meeting_time_second(availability):

    if not availability:
        return "None"
    
    # Start with first person's availability
    common = availability[0]

    # Intersect with each remaining person's availability
    for person in availability[1:]:
        new_common = []

        i = j = 0

        while i < len(common) and j < len(person):
            start = max(common[i][0], person[j][0])
            end = min(common[i][1], person[j][1])


            if end - start >= 1:
                new_common.append([start, end])

            # Move the interval that ends first
            if common[i][1] < person[j][1]:
                i += 1
            else:
                j += 1

        common = new_common
            
        if not common:
            return "None"
        
    return common[0][0] if common else "None"



from utils.benchmark import benchmark
if __name__ == "__main__":

    scores = benchmark({
        "zero": get_meeting_time_first,
        "first": get_meeting_time,
        "second": get_meeting_time_cleaner,
        "third": get_meeting_time_second
    }, TESTCASES, 10000)

    unittest.main()