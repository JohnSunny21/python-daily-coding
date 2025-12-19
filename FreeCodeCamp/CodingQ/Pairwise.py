"""   

Pairwise
Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.

For example, given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:

2 and 8 (2 + 8 = 10), whose indices are 0 and 4
4 and 6 (4 + 6 = 10), whose indices are 2 and 3
Add all the indices together to get a return value of 9.
"""

import unittest

class PairwiseTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(pairwise([2, 3, 4, 6, 8], 10), 9)

    def test2(self):
        self.assertEqual(pairwise([4, 1, 5, 2, 6, 3], 7), 15)

    def test3(self):
        self.assertEqual(pairwise([-30, -15, 5, 10, 15, -5 , 20, -40], -20), 22)

    def test4(self):
        self.assertEqual(pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24), 10)


def pairwise_bruteforce(arr, target):

    freq = dict()
    summ = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target :
                freq[i] = j

    print(freq)

    for key, value in freq.items():
        summ += key + value

    return summ

"""

This brute force solution has some issues

=> this solution overwrite freq[i] each, time, so if multiple pairs exist for the same i, only the last one is kept.
=> Here no marking of elements as "used", so technically the same element could be reused in another pair if you extended this.
=> The above test cases will pass but the solution itself is fragile.

The real time example:
arr = [1, 9, 9, 1]
target = 10

i = 0, j = 1 -> 1 + 9 = 10 -> freq[0] = 1
i = 0, j = 2 -> 1 + 9 = 10 -> overwrites freq[0] = 2 (previous pair lost)
i = 3, j = 1 -> 1 + 9 = 10 -> freq[3] = 1
i = 3, j = 2 -> 1 + 9 = 10 -> overwrites freq[3] = 2

Final freq = {0: 2, 3: 2} -> Only last matches kept, earlier valid paris discarded.
Flaw: You lose information because dictioanary keys must be unique. Multiple valid pairs for the same i overwrite each other.
"""




def pairwise_optimal(arr, target):

    freq = {}
    for i in range(len(arr)):
        freq[arr[i]] = i    # maps value -> last index


    summ = 0
    res = {}

    for i in range(len(arr)):
        compliment = target - arr[i]
        if compliment in freq and freq[compliment] != i:
            summ += i + freq[compliment]

""" 
This solution is partial but it has issues
=> Overwritting indices:
    freq[arr[i]] = i stores only the last index of each value. if a value appears multiple times, earlier indices are lost.
=> Double counting:
    when you loop over i, you find both (i, j) and (j, i) because the dictionary still contains the complement, 
    That's why you get twice the sum.
=> No "used" tracking:
    Once a pair is found, you don't mark those indices as consumed, so they can be reused.

The real time example:
Build freq:
{2 : 0, 8 : 1, 4 : 2, 6 : 3}
Loop:
=> i = 0 (val = 2), compliment = 8 -> found at index 1 -> summ += 0 + 1 = 1
=> i = 1 (val = 8), compliment = 2 -> found at index 0 -> summ += 1 + 0 = 1 (double counted!)
=> i = 2 (val = 4), compliment = 6 -> found at index 3 -> summ += 2 + 3 = 5
=> i = 3 (val = 6), compliment = 4 -> found at index 2 -> summ += 3 + 2 = 5(double counte!)

Total = 12, but correct answer should be 6 (pairs (2, 8) and (4, 6)).
Flaws:
1. Double counting: Both(i, j) and (j, i) are added.
2. Overwriting indices: if a value appears multile times, only the last index is stored.
"""

def pairwise_optimal_corrected(arr, target):
    used = [False] * len(arr)

    summ = 0
    index_map = {}

    for i, val in enumerate(arr):
        index_map.setdefault(val, []).append(i)

    for i, val in enumerate(arr):
        if used[i]:
            continue
        compliment = target - val
        if compliment in index_map:
            for j in index_map[compliment]:
                if j != i and not used[j]:
                    summ += i + j
                    used[i] = True
                    used[j] = True
                    break
    
    return summ

"""
The real time example:
arr = [2, 8 , 4, 6]
target = 10

=> i = 0 (val = 2), compliment = 8 ->  j = 1 -> summ = 1, mark used[0] = True, used[1] = True
=> i = 1 -> continue because used[1] = True -> skip
=> i = 2 (val = 4), compliment = 6 -> j = 3 -> summ = 1 + 5 = 6, mark used[2] = True, used[3] = True

=> i = 3 -> continue because used[3] = True -> skip

Final sum = 6 

The use of j!=i 

Here, index_map[compliment] is a list of all indices where the complement value occurs.
That list can include the current index i itself if arr[i] equals its own complement.

When does i == j happen

It happens when the element can pair with itself to reach the target.

Example 1: self-pair case

arr = [5]
target = 10

=> i = 0, val = 5
=> compliment = 10 - 5 = 5
=> index_map[5] = [0]
=> So j = 0 -> same as i.

If we didn't check j != i, we'd incorrectly count the element pairing with itself.

Example 2: Multiple identical values

arr = [5, 5]
target = 10

=> i = 0, val = 5, compliment = 5
=> index_map[5] = [0, 1]
=> loop over j:
            => j = 0 -> same as i -> skip because of j!=i
            => j = 1 -> valid pair -> summ += 0 + 1
=> Without j!=i, the first iteration would try to pair index 0 with itself


* Why it matters:
==> Correctness: Prevents self-paring unless there are actually two distinct elements.
==> Safety: Avoids double counting when the complement equals the value itself.
==> Logic: We only want pairs of two different indices.

* Key Takeaway:
==> i == j happens when the value equals its own complement (e.g., target = 10, value = 5).
==> The check j!=i ensures we don't pair an element with itself unless another copy exists.
==> Yes, i always moves forward, but the inner loop iterates over all indices of the complement, which can include i itself. That's why the guard is necessary.


The real time example:

arr = [5, 5, 10]
target = 10

we want pairs that sum to 10.

Step 1: Build index_map

index_map = {
    5: [0, 1],
    10: [2]
}

So value 5 occurs at indices 0 and 1, and value 10 occurs at index 2.

Step 2: Iterate over array

i = 0, val = 5
=> compliment = 10 - 5 = 5
=> index_map[5] = [0, 1]
=> Loop over j:
        => j = 0 -> same as i -> skip because of j!=i
        => j = 1 -> valid pair -> summ += 0 + 1
        mark used[0] = True, used[1] = True

i = 1, val = 5
=> used[1] = True -> continue (skip this index)
i = 2, val = 10
=> compliment = 10 - 10 = 0
=> 0 not in index_map -> no pair

Step 3: Result
=> Only one valid pair: indices (0, 1) -> sum = 1
=> Without j!=i, the algorithm would have tried to pair index 0 with itself (0 + 0), which is invalid.

Which j!=i is essential
=> It prevents self-pairing when the value equals its own complement (like 5 + 5 = 10).
=> Ensures we only use two distinct indices.
=> Works correctly even when duplicates exist.


REAL-TIME ANALOGY:

Imagine you're pairing for a dance:

=> Each person has a "number" (array index).
=> The target is the total score tey must reach together.
=> If you allow someone to pair with themselves, they'd be dancing alone 
    - which breaks the rule.
    That's why we check j!=i : to ensure two different people form the pair.


"continue" means skip this person if they're already paired, and j!=i means don't let some pair with themselves.
"""


def pairwise(arr, target):

    used = [False] * len(arr) # Tracking used elements
    total = 0

    for i in range(len(arr)):
        if used[i]:
            continue
        for j in range(i + 1, len(arr)):
            if  not used[j] and arr[i] + arr[j] == target:
                total += i + j
                used[i] = True
                used[j] = True
                break   # move to next i after finding a pair

    return total

"""
This solution

=> Avoid double counting: Once an element is used in a pair, mark it as used so it doesn't get reused.
=> Efficiency: This is O(n^2) in worst case, but fine for moderate input sizes.
=> Correctness: Matches the example:
        pair(2, 8) -> indices 0 + 4 = 4
        pair(4, 6) -> indices 2 + 3 = 5
        Total = 9
"""

"""
Key Takeaways
=> Brute force flaw: dictionary overwrites earlier pairs for same i.
=> Optimal flaw: dictionary stores only last index per value, and double counts pairs.
=> Correct fix: store all indices, and use a used array.
                continue means: if this index is already paired, skip the rest of the loop body and move to the next iteration.
"""

if __name__ == "__main__":
    print(pairwise_optimal_corrected([2, 3, 4, 6, 8], 10))
    # unittest.main()
    