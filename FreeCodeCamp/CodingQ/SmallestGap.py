"""

Smallest Gap
Given a string, return the substring between the two identical characters that have the smallest number of characters between them (smallest gap).

There will always be at least one pair of matching characters.
The returned substring should exclude the matching characters.
If two or more gaps are the same length, return the characters from the first one.
For example, given "ABCDAC", return "DA".

Only "A" and "C" repeat in the string.
The number of characters between the two "A" characters is 3, and between the "C" characters is 2.
So return the string between the two "C" characters.
"""

import unittest


class SmallestGapTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(smallest_gap("ABCDAC"), "DA")  

      def test2(self):
          self.assertEqual(smallest_gap("racecar"), "e")  

      def test3(self):
          self.assertEqual(smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"), "#q6e&rkf(p")

      def test4(self):
          self.assertEqual(smallest_gap("Hello World"), "")

      def test5(self):
          self.assertEqual(smallest_gap("The quick brown fox jumps over the lazy dog."), "fox")


from collections import Counter
def smallest_gap1(s):
    

    count = Counter(s)
    refined_count = {}
    for key in count:
        if  count[key] > 1:
            refined_count[key] = count[key]

    print(refined_count)

    result = []
    for key in refined_count:
        first_index = s.index(key)
        last_index = s.index(key, first_index + 1)
        string_len = s[first_index+1: last_index]
        result.append((key, string_len))

    result.sort(key=lambda x :len(x[1]))
    print(result)
    return result[0][1]


"""  

There are issues with the above code
1. Only first two occurrences:
    You use s.index(key) and then s.index(key, first_index+1) . That only finds the first and second occurence
    of each character. if a character appears more than twice, you ignore later pairs that might have a smaller gap.

    1. Example: "ABCAAD"
        -> For "A", you'd only check between index 0 and 3 ("BC")
        -> But there's also a pair at indices 3 and 4 with gap length 0, which is smaller. The above code misses that.

2. No minimum gap tracking across all pairs:
    -> You sort at the end, but since you only collected one substring per character, you don't actually compare all possible paris.


    
Refining the above version

We can fix it by:
    => Iterating through the string.
    => For each character, track all indices where it appears.
    => Compare consecutive indices to find the smallest gap for that character.
    => keep track of the globla minimum.


"""


"""
------------------------------------------------------------------------------
APPROACH 1 (Educational but inefficient)

Store all positions of each character first, then compare gaps.

Time Complexity:  O(n)
Space Complexity: O(n)

This works but uses extra memory.
------------------------------------------------------------------------------
"""
from collections import defaultdict

def smallest_gap(s):

    positions = defaultdict(list)

    for i, ch in enumerate(s):
        positions[ch].append(i)

    min_gap = float('inf')
    result = ""

    # For each character with multiple occurences
    for ch, idx_list in positions.items():
        if len(idx_list) > 1:

            # Compare consecutive occurences
            for j in range(1, len(idx_list)):
                gap_len = idx_list[j] - idx_list[j-1] - 1
                if gap_len < min_gap:
                    min_gap = gap_len
                    result = s[idx_list[j-1]+1: idx_list[j]]
    
    return result





"""
------------------------------------------------------------------------------
APPROACH 1 (Educational but inefficient)

Store all positions of each character first, then compare gaps.

Time Complexity:  O(n)
Space Complexity: O(n)

This works but uses extra memory.
------------------------------------------------------------------------------
"""

def smallest_gap(s):
    min_gap = float('inf')
    result = ""

    # Dictionary to store first occurence of each character

    seen = {}

    for i, ch in enumerate(s):
        if ch in seen:
            # Calculate gap length

            gap_len = i - seen[ch] - 1
            if gap_len < min_gap:
                min_gap = gap_len
                result = s[seen[ch]+1: i] # substring between the two identicaal chars

        # Always update the last index
        seen[ch] = i

    return result


"""
Smallest Gap - Compact Solution

Idea : 

Scan the string once while remembering the most recent index
where each character appeared.

When we encounter the same character again, we compute the distance between the two occurrences.

If this gaap is smaller than the current minimum gap, we update the result substring.

Time Complexity: O(n)
Space Complexity: O(unique character)

"""

def smallest_gap(s):

    last_seen = {}  # Stores the most recent index of each character
    min_gap = len(s) # Initialize with maximum possible gap
    result = ""


    for i, ch in enumerate(s):

        # If the character was seen before,
        # compute the gap between current index and previous index
        if ch in last_seen:

            gap = i - last_seen[ch] - 1

            # Update smallest gap and substring if this gap is smaller
            if gap < min_gap:
                min_gap = gap
                result = s[last_seen[ch]+1 : i]

        # Always update the last seen index
        last_seen[ch] = i

    return result


if __name__ == "__main__":
    # print(smallest_gap("ABCDAC"))
    print(smallest_gap("The quick brown fox jumps over the lazy dog."))
    unittest.main()
    