"""
=======================================================================>        Factorializer       <=====================================================================
Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.

The factorial of zero is 1.

====================================================================================================================================================================
O/P : ====>

factorial(0) should return 1.
"""

def factorial(n):
    fact = 1

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    
    # while n > 0:
    #     fact *= n
    #     n -= 1

    # We can also use the for -loop here
    for i in range(1, n+1):
        fact *= i

    return fact



if __name__ == "__main__":
    print(factorial(7))