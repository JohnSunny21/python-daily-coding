""" 
Pascal's Triangle Row
Given an integer n, return the nth row of Pascal's triangle as an array.

In Pascal's Triangle, each row begins and ends with 1, and each interior value is the sum of the two values directly above it.

Here's the first 5 rows of the triangle:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""

import unittest


class PascalsTriangleRowTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(pascal_row(5), [1, 4, 6, 4, 1]) 

    def test2(self):
        self.assertEqual(pascal_row(3), [1, 2, 1])       

    def test3(self):
        self.assertEqual(pascal_row(1), [1])

    def test4(self):
        self.assertEqual(pascal_row(10), [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])

    def test5(self):
        self.assertEqual(pascal_row(15), [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1])



def pascal_row_build(n):

    # Building the triangle approach
    # Start with the first row
    triangle = [[1]]

    # Build the rows up to n
    for i in range(1, n+1):
        prev = triangle[-1]
        row = [1]    # Every row starts with 1
        # interior values are sums of two above
        for j in range(1, i):
            row.append(prev[j-1] + prev[j])
        row.append(1) # every row ends with 1
        triangle.append(row)

    return triangle[n-1]



import math

def pascal_row(n):
    """ 
    To generate the nth row of Pascal’s Triangle, you can use the property that each entry is a binomial coefficient:

            Row 𝑛= [(𝑛0),(𝑛1),(𝑛 2),…, (𝑛  𝑛)]

        where (𝑛 𝑘)=𝑛! / 𝑘!(𝑛−𝑘)!
.
    """

    return [math.comb(n-1, k) for k in range(n)]


from utils.benchmark import benchmark
if __name__ == "__main__":


    TESTCASES = [
    ((5,), [1, 4, 6, 4, 1]),
    ((3,), [1, 2, 1]),
    ((1,), [1]),
    ((10,), [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]),     
    ((15,), [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1])
]
    scores = benchmark(
        {"build_approach": pascal_row_build,
         "binomial_coefficient_approach": pascal_row},
        TESTCASES,
        10000
    )
    print(scores)
    
    unittest.main()