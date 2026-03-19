""" 


Inverted Matrix
Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

[
  ["a", "b"],
  ["a", "a"]
]
Return:

[
  ["b", "a"],
  ["b", "b"]
]
"""

import unittest
from utils.benchmark import benchmark

class InvertedMatrixTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(invert_matrix([["a", "b"], ["a", "a"]]), [["b", "a"], ["b", "b"]])

      def test2(self):
          self.assertEqual(invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]), [[0, 1, 0], [0, 0, 0], [1, 0, 1]])   

      def test3(self):
          self.assertEqual(invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]]), [["banana", "apple", "apple", "banana"], ["apple", "banana", "banana", "apple"], ["apple", "apple", "apple", "banana"]])

      def test4(self):
          self.assertEqual(invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]]), [[7, 6, 6, 6, 7], [6, 7, 6, 7, 6], [6, 6, 7, 6, 6], [6, 7, 6, 7, 6], [7, 6, 6, 6, 7]])

      def test5(self):
          self.assertEqual(invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]), [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]])


import timeit
def invert_matrix_manual(matrix):
    rows , cols = len(matrix), len(matrix[0])

    # WE CAN USE THE next() here to avoid this loops
    # b = next(matrix[i][j] for i in range(rows) for j in range(cols) if matrix[i][j]!=a)
    # It starts at matrix[0][0] , but since that equsls a, the if condition filters it out.
    # So it looks like it "skipped" the first element, but really it just dint yield it.
    # next() takes an iterator and returns the first item it produces.
    # next() stops at the first match and returns it.
    """
    So:

        next() = “give me the first element from this iterator.”

        If no element matches, you’d get a StopIteration error unless you provide a default:

        python
        next((...), None)
    """
    a = matrix[0][0]
    b = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != a:
                b = matrix[r][c]
                break
        if b:
            break

    # visited_matrix = [[False]* cols] * rows
    # new_matrix = [[0] * cols ] * rows
    #Python builds one list [0,0,0].
    #Then it repeats the reference to that list three times.
    #All rows point to the same object in memory.
    #Mutating one row mutates them all.
    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    #Python builds a fresh [0,0,0] for each row.
    #Each row is independent.
    #Mutating one row doesn’t affect the others.

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == a: #and not visited_matrix[r][c]:
                new_matrix[r][c] = b
            elif matrix[r][c] == b: #and not visited_matrix[r][c]:
                new_matrix[r][c] = a
        # visited_matrix[r][c] = True

    return new_matrix

"""
=> In python, [[False] * cols] * rows, doesn't create rows independant lists.
=> It creates one list of length cols, then repeats the referencce to that same list rows times.
=> So every row in visited_matrix ( and new_matrix) points to the same underlying object.
=> When you update new_matrix[0][0], it also changes new_matrix[1][0], new_matrix[2][0], etc., because they're all aliases of the same row.

That's why the second row will change before you even reached it.

To Fix:
=> use a list comprehension to ensure each row is a distinct object:
    see the above example
    -> now each row is independant, and updates won't leak into other rows.

And one more thing to remember 
=> We don't need visited_matrix at all
=> you're looping through every cell exactly once.
=> There's no risk of revisiting the same cell.
=> so the check if not visited_matrix[r][c] is redundant

by making these changes the above solution works fine.

Insights:
=> The above solution is to manually traverse and break early for the second value is good 
    -> it's O(n.m) worst case, O(1) best case.
=> The bug was purely from Python's list multiplication semantics. This is a classic pitfall even experienced devs hit.
=> Dropping visited_matrix makes the code simpler and avoids unnecessary memory.
=> Complexity: O(n.m) time, O(n.m)space for the new matrix. That's optimal since you must produce a new matrix anyway.
"""

def invert_matrix(matrix):

    values = {val for row in matrix for val in row}
    v1 , v2 = list(values)

    return [[v2 if cell == v1 else v1 for cell in row] for row in matrix]




if __name__ == "__main__":
    print(invert_matrix([["a", "b"], ["a", "a"]]))
    matrix = [[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]
    execution_time_manual = timeit.timeit(lambda: invert_matrix_manual(matrix), number=1000)
    # here number = 1000 means run the function 1000 times
    # This gives you a reliable average execution time.
    execution_time_concise = timeit.timeit(lambda: invert_matrix(matrix), number=1000)
    print(f"Execution time: {execution_time_manual:.6f} seconds")
    print(f"Execution time: {execution_time_concise:.6f} seconds")





    TESTCASES = [
    (([["a", "b"], ["a", "a"]],), [["b", "a"], ["b", "b"]]),
    (([[1, 0, 1], [1, 1, 1], [0, 1, 0]],), [[0, 1, 0], [0, 0, 0], [1, 0, 1]]),       
    (([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]],), [["banana", "apple", "apple", "banana"], ["apple", "banana", "banana", "apple"], ["apple", "apple", "apple", "banana"]]),
    (([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]],), [[7, 6, 6, 6, 7], [6, 7, 6, 7, 6], [6, 6, 7, 6, 6], [6, 7, 6, 7, 6], [7, 6, 6, 6, 7]]),
    (([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]],), [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]])
]
    scores = benchmark(
        {"manual": invert_matrix_manual, "concise": invert_matrix},
        TESTCASES,
        number= 1000
    )
    print(scores)
    unittest.main()
