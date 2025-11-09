"""
Word Search
Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

The given matrix will be filled with all lowercase letters (a-z).
The word to find will always be in the matrix exactly once.
The word to find will always be in a straight line in one of these directions:
left to right
right to left
top to bottom
bottom to top
For example, given the matrix:

[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]
And the word "cat", return:

[[0, 1], [2, 1]]
Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t" (end of the word).
"""

import unittest, snoop

class WordSearchTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]],"cat"),[[0,1], [2,1]])

    def test2(self):
         self.assertEqual(find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog"),[[0,0],[0,2]])

    def test3(self):
         self.assertEqual(find_word([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish"),[[3,3],[0,3]])

    def test4(self):
         self.assertEqual(find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox"),[[1,3], [1,1]])


# @snoop
def find_word(matrix,word):
   rows, cols = len(matrix) , len(matrix[0])
   word_len = len(word)

   directions = {
        "right":(0,1),
        "left":(0,-1),
        "down":(1,0),
        "up":(-1,0)
   }

   def in_bounds(r, c):
        return 0<= r < rows and 0 <= c < cols
   
   for r in range(rows):
        for c in range(cols):
             for dr , dc in directions.values():
                  path = []
                  for i in range(word_len):
                    nr , nc = r + dr * i, c + dc * i
                    if not in_bounds(nr, nc) or matrix[nr][nc] != word[i]:
                        break
                    path.append([nr,nc])
                  if len(path) == word_len:
                        return [path[0],path[-1]]
                  
   return None




    



if __name__ == "__main__":
        
        print(find_word([["a", "c", "t"], ["t", "a", "s"], ["c", "t", "c"]],"cat"))
        # unittest.main()
    