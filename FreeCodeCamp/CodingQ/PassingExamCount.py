""" 

Passing Exam Count
Given an array of student exam scores and the score needed to pass it, return the number of students that passed the exam.
"""

import unittest

class PassingExamCountTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(passing_count([90, 85, 75, 60, 50], 70), 3)

    def test2(self):
        self.assertEqual(passing_count([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75), 6)

    def test3(self):
        self.assertEqual(passing_count([79, 60, 88, 72, 74, 59, 75, 71, 80, 92], 60), 9)

    def test4(self):
        self.assertEqual(passing_count([76, 79, 80, 70, 71, 65, 79, 78, 59, 72], 85), 0)

    def test5(self):
        self.assertEqual(passing_count([84, 65, 98, 53, 58, 71, 91, 80, 92, 70, 73, 83, 86, 69, 84, 77, 72, 58, 69, 75, 66, 68, 72, 96, 90, 63, 88, 63, 80, 67], 60), 27)



def passing_count(scores, passing_score):

    return sum(1 for score in scores if score >= passing_score)


from utils.benchmark import benchmark
if __name__ == "__main__":
    TESTCASES = [
    (([90, 85, 75, 60, 50], 70,), 3),
    (([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75,), 6),        
    (([79, 60, 88, 72, 74, 59, 75, 71, 80, 92], 60,), 9),
    (([76, 79, 80, 70, 71, 65, 79, 78, 59, 72], 85,), 0),
    (([84, 65, 98, 53, 58, 71, 91, 80, 92, 70, 73, 83, 86, 69, 84, 77, 72, 58, 69, 75, 66, 68, 72, 96, 90, 63, 88, 63, 80, 67], 60,), 27)
]
    
    scores = benchmark(
        {"optimized": passing_count},
        TESTCASES,
        10000
    )
    print(scores)
    
    unittest.main()