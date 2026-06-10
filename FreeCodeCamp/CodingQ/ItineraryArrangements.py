"""


Itinerary Arrangements
Given an array of at least two optional stops for a day trip, return the number of valid itinerary arrangements.

The itinerary always includes "breakfast", "lunch", and "dinner", these will not be passed in as arguments. The optional stops can be placed anywhere in the itinerary, subject to the following rules:

"breakfast" is always first, with at least one stop before "lunch".
"lunch" must appear before "dinner", with at least one stop in between.
At most, one optional stop may appear after "dinner".
Return the number of valid arrangements.
"""


import unittest

class ItineraryArrangementsTest(unittest.TestCase):



    def test1(self):
        self.assertEqual(get_itinerary_count(["library", "park"]), 2)

    def test2(self):
        self.assertEqual(get_itinerary_count(["library", "park", "arcade"]), 18)

    def test3(self):
        self.assertEqual(get_itinerary_count(["library", "park", "arcade", "store"]), 120)

    def test4(self):
        self.assertEqual(get_itinerary_count(["library", "park", "arcade", "store", "cafe"]), 840)

    def test5(self):
        self.assertEqual(get_itinerary_count(["library", "park", "arcade", "store", "cafe", "market", "museum"]), 55440)


TESTCASES = [
    ((["library", "park"],), 2),
    ((["library", "park", "arcade"],), 18),
    ((["library", "park", "arcade", "store"],), 120),
    ((["library", "park", "arcade", "store", "cafe"],), 840),
    ((["library", "park", "arcade", "store", "cafe", "market", "museum"],), 55440)
]

import itertools

def get_itinerary_count4(stops):

    if len(stops) < 2:
        return 0
    
    count = 0

    for perm in itertools.permutations(stops):
        
        # Build itinerary: breakfast + perm + Lunch + dinner
        itinerary = ["breakfast"] + list(perm) + ["lunch", "dinner"]

        # Rule 1: At least one stop before lunch
        before_lunch = itinerary[1: itinerary.index("lunch")]
        if not before_lunch:
            continue

        # Rule 2: At least one stop between lunch and dinner
        between = itinerary[itinerary.index("lunch")+1:itinerary.index("dinner")]
        if not between:
            continue


        # Rule 3: At most one stop after dinner
        after_dinner = itinerary[itinerary.index("dinner")+1:]
        if len(after_dinner) > 1:
            continue

        count += 1


    return count

""" 
=> The above code doesn't actually generate different positions for lunch and dinner.

for every permutation, you're building:
    ["breakfast"] + perm + ["lunch", "dinner"]

    So the itinerary always looks like:
        breakfast stop1 stop2 ... stopN lunch dinner

    As a result 
    -> there are always stops before lunch
    -> there are never any stops between lunch and dinner
    -> there are never any stops after dinner
    Therefore:

    between = itinerary[itinerary.index("lunch")+1: itinerary.index("dinner")]

    is always:
        []

        and every permutation gets rejected.
    
    For example:

    stops = ["museum", "park"]

    itinerary = 
    [ 
    "breakfast",
    "museum",
    "park",
    "lunch",
    "dinner",
    ]


    Between lunch and dinner

    []

    So continue executes

    To brute force correctly, you must place lunch and dinner among the optional stops,
    not always at the end.

    Example brute-force approach:

    
"""

import itertools


def get_itinerary_count2(stops):

    n = len(stops)
    count = 0

    for perm in itertools.permutations(stops):

        # Choose position of lunch
        for lunch_pos in range(2, n + 1):
            
            #choose position of dinner
            for dinner_pos in range(lunch_pos + 2, n + 3):

                itinerary = ["breakfast"] + list(perm)

                itinerary.insert(lunch_pos, "lunch")
                itinerary.insert(dinner_pos, "dinner")

                after_dinner = len(itinerary) - itinerary.index("dinner") - 1

                if after_dinner <= 1:
                    count += 1

    return count


# But this is very inefficient O(n! * n^2)



from math import factorial

def get_itinerary_count3(stops):
    n = len(stops)
    return factorial(n) * (2 * n - 3)


# Without imports
"""
=> let there be n optional stops.

    the fixed itinerary items are:
        -> breakfast (B) - always first
        -> lunch (L)
        -> dinner (D)

    Rules:
        1. B is first.
        2. At least one optional stop before L.
        3. L before D.
        4. At least one optional stop between L and D.
        5. At most one optional stop after D.

    Counting approach
    => partition the n optional stops into three groups:
        -> a stops before L
        -> b stops before L and D
        -> c stops after D

    Constraints:
        -> a >= 1
        => b >= 1
        => c ∈ {0,1}
        => a + b + c = n

        for each valid (a, b, c):
        1. choose which stops go into each groups:
                n! / a!b!c!

        2. Arrange stops within each groups:    
                    a! b! c!

        Multiplying gives simply:
            n!


        for every valid partition.
        So the answer is:

        n! * (number of valid(a, b, c))

        NUmber of valid partitions:
           c = 0:
            a + b = n, a,b ≥ 1
            n - 1 possibilities
            c = 1:
            a + b = n - 1, a,b ≥ 1
            n - 2 possibilities

            Total:

            (n−1)+(n−2)=2n−3

            Therefore:

            (2n−3)n!
	​


"""

def get_itinerary_count(stops):

    n = len(stops)

    fact = 1
    for i in range(2, n + 1):
        fact *= i

    return fact * (n * 2 - 3)

"""
=> stops = ["museum", "park"]

    -> 2! * ( 2 * 2 - 3)
    -> 2 * 1
    -> 2

    The two valid itineraries are:
    breakfast museum lunch park dinner
    breakfast part lunch museum dinner

"""


from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({
        "first": get_itinerary_count,
        "second": get_itinerary_count2,
        "third": get_itinerary_count3
    }, TESTCASES, 10
    
    
    )

    unittest.main()
