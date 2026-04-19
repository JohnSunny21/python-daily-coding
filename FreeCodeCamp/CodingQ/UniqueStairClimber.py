""" 


Unique Stair Climber
Given a number of stairs, return how many distinct ways someone can climb them taking either 1 or 2 steps at a time.
"""


import unittest


class UniqueStairClimberTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_unique_climbs(4), 5)

    def test2(self):
        self.assertEqual(get_unique_climbs(5), 8)

    def test3(self):
        self.assertEqual(get_unique_climbs(10), 89)

    def test4(self):
        self.assertEqual(get_unique_climbs(18), 4181)

    def test5(self):
        self.assertEqual(get_unique_climbs(29), 832040)

    def test6(self):
        self.assertEqual(get_unique_climbs(50), 20365011074)


TESTCASES = [
    ((4,), 5),
    ((5,), 8),
    ((10,), 89),
    ((18,), 4181),
    ((29,), 832040),
    ((50,), 20365011074)
]



"""
    This is the classic staircase problem - the number of distinct ways to climb n stairs taking 1 or 2 steps
    at a time is given by the fibonacci sequence.

    Why the fibonacci?

    => To reach stair n, you could have come from:
        -> stair n = 1 (taking 1 step) , or
        -> stair n = 2 (taking 2 steps).


    => So the recurrence is: 

        ways(n) = ways(n - 1) + ways(n - 2)

    => Base cases:
        -> ways(1) = 1 (only one way: a single step)
        -> ways(2) = 2 (either two 1-steps or one 2-step)

    
    This problem is essentially Fibonaci shifted by one index. For n staairs, the number of ways equals fib(n + 1)

    The problem description is

    You have n stairs. You can climb either:
        -> 1 step at a time, or
        -> 2 steps at a time
    The question: How many distinct ways can you reach the top?


    Example with 5 stairs

    Let's list them out:

    -> All 1-steps : 1 + 1 + 1 + 1 + 1
    -> Two 2 - steps  + one-1-step:
        -> 2 + 2 + 1
        -> 2 + 1 + 2
        -> 1 + 2 + 2
    -> One 2-step + three 1-steps:
        -> 2 + 1 + 1 + 1
        -> 1 + 2 + 1 + 1
        -> 1 + 1 + 2 + 1
        -> 1 + 1 + 1 + 2

    That's 8 distinct ways to climb 5 stairs.


    The pattern here is :

    => To reach stair n, you must come from:
        -> stair n - 1 (taking a 1 - step), or 
        -> stair n - 2 (taking a 2 - step).

    => So the recurrence is:

            ways(n) = ways(n - 1) + ways(n - 2)

    This is exactly the Fibonacci sequence, shifted by one index.


    Base cases:

    -> ways(1) - 1( only one way: a single step)
    -> ways(2) = 2 (either two 1 - steps or one 2-steps)

    from there, you build up:
    => ways(3) = ways(2) + ways(1) = 2 + 1 = 3
    => ways(4) = ways(3) + ways(2) = 3 + 2 = 5
    => ways(5) = ways(4) + ways(3) = 5 + 3 = 8


    This manual listing shows why the recurrence relation works:

    => To get to stair n, you either add a  1 after a solution for n - 1, or add 2 after a solution for n - 2
    => That's why ways(n) = ways(n - 1) + ways(n - 2)
"""

def get_unique_climbs(steps):

    if steps <= 0:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return 2

    a, b = 1, 2

    for _ in range(3, steps + 1):

        a, b = b, a + b

    return b


# To generate all these possibilities manually we can write the code as

def stair_possibilities(n):

    result = []

    def backtrack(path, total):
        if total == n:
            result.append(path[:])   # found a valid sequence
            return
        
        if total > n:
            return  # overshoot, stop
        

        path.append(1)
        backtrack(path, total + 1)
        path.pop()

        # Try taking 2 steps
        path.append(2)
        backtrack(path, total + 2)
        path.pop()

    backtrack([], 0)
    
    return len(result)





from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark(
        {"first": get_unique_climbs,
         "second": stair_possibilities}, 
         TESTCASES,
         10000
    )
    unittest.main()



