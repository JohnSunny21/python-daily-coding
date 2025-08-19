"""
================================================================>       Sum of Squares       <====================================================================================
Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.

==========================================================================================================================================================================================
O/P : ====>

1. sum_of_squares(5) should return 55.
2. sum_of_squares(10) should return 385.
3. sum_of_squares(25) should return 5525.

"""

def sum_of_squares(n):
    return sum(num**2 for num in range(1,n+1))


# Bonus : Which is a Mathematical Formula
# If we optimize the code further, the sum of squares from 1 to n can be computed directly:
# sum = n(n+1)(2n + 1) // 6

def sum_of_squares_optimal(n):
    return n * (n + 1) * (2 * n + 1) // 6
# This avoids iteration entirely and is lighting -fast especially usefull if n gets very large.


if __name__ == "__main__":
    print(sum_of_squares(5))