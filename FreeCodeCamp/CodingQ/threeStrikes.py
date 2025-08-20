"""
3 Strikes
Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3.


O/P : ==>

squares_with_three(1) should return 0.
"""

def squares_with_three(n):
    count = 0

    for i in range(1, n+1):
        num = i ** 2
        if '3' in str(num):
            count += 1
    return count


# Optimal Optimization
# If the code ever need to be optimized and slightly faster for large n,
# we could avoid recomputing str(num) twice:

def squares_with_three_optimal(n):
    return sum('3' in str(i * i) for i in range(1,n+1))
# This uses a generator expression and is just as readable.

