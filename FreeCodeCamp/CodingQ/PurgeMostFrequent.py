"""  
Purge Most Frequent
Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

If multiple values are tied for most frequent, remove all of them.
Do not change any of the other elements or their order.

"""

import unittest

class PurgeMostFrequentTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(purge_most_frequent([1, 2, 2, 3]), [1, 3])

    def test2(self):
        self.assertEqual(purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]), ["a", "b", "b", "c", "c", "c"])

    def test3(self):
        self.assertEqual(purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]), ["red", "green", "red", "green"])

    def test4(self):
        self.assertEqual(purge_most_frequent([5, 5, 5, 5]), [])


def purge_most_frequent(arr):

    max_element = max(arr, key=arr.count)

    while max_element in arr:
        arr.remove(max_element)

    return arr

"""
Strengths:

=> max(arr, key=arr.count) finds the element with the highest frequency.
=> The while loop removed all occurences of that element.
=> Preserves the order of the other elements.

Example:
    print(purge_most_frequent([5, 1, 5, 2, 2, 3]))
    # Output: [1, 2, 2, 3] (removes all 5s)

Limitations:

1. Ties are ignored
    if multiple elements are tied for most frequent, only one is removed.
Example:
    print(purge_most_frequent([5, 2, 5, 2, 3]))
    # Expected: [3] (remove both 5 and 2)

    # Got: [2, 2, 3] (only removed 5s)

2. Efficiency
    => arr.count(x) scans the list each time, so max(arr,key=arr.count) is O(n^2) in worst case.
    => For large arrays, this become slow.

The above code is correct but incomplete: it handles only one most frequent element.
The improved version handles ties and is O(n) instead of O(n^2).
If you only care about one most frequent element, The above code is fine. If you want to fully match the problem
statement ("remove all tied most frequent"), you need the Counter approch.

"""

from collections import Counter
# improved version
def purge_most_frequent(arr):


    freq = Counter(arr)

    max_freq = max(freq.values())

    most_frequent_element = {val for val, count in freq.items() if count == max_freq}

    result = [x for x in arr if x not in most_frequent_element]

    return result

"""
=> Counter/frequency map is the cleanest way to find the most frequent elements.
=> Set is used to store all tied elements for quick lookup.
=> List comprehension / filter rebuilds the array without those elements.
=> Preserves order because we iterate over the original array.
"""


if __name__ == "__main__":

    """

    lis = [5, 5, 5, 5] if => removed 5 using the loop still some 5 exists in the list.
    List-Mutation trap:

    what happens with list.remove()
    => lis.remove(5) removes only the first occurences of 5.
    => if you call it once, only one 5 goes away.

    Why the loop leave some 5's

    lis = [5, 5, 5, 5]
    for char in lis:
        if char == 5:
            lis.remove(5)

    => You're iterating over lis while modifying it.
    => when you remove an element, the list shrinks, and the indices shift.
    => The loop's internal index moves forward, so it skips over some elements.

    Step-by-Step Tracing:

    Inital : [5, 5, 5, 5]
    => Iteration 1: char = 5, remove first -> [5, 5, 5]
    => Iteration 2: next index points to the second element, but because of the shift, you skip one 5.
    => Result: not all removed.

    Correct ways to remove all 5's
    1. Use a while loop

        lis = [5, 5, 5, 5]
        while 5 in lis:
            lis.remove(5)
        
        print(lis) # []

    2. Use list comprehension (cleanest)
        lis = [5, 5, 5, 5]
        lis = [x for x in lis if x != 5]
        print(lis) # []
    
    3. use filter
        lis = [5, 5, 5, 5]
        lis = list(filter(lambda x: x!=5, lis))
        print(lis) # []

    Takeaway:
    => Never modify a list while iterating over it - you'll skip elements.
    => remove() deletes only the first match.
    => To remove all occurences, either:
        => Loop with while value in list: remove(value), or
        => Rebuild the list with a comphrehension.
    
    """

    print(purge_most_frequent([1, 2, 2, 3]))
    unittest.main()