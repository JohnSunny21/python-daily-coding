"""
Unnatural Prime
Given an integer, determine if that number is a prime number or a negative prime number.

A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
A negative prime number is the negative version of a positive prime number.
1 and 0 are not considered prime numbers.
"""

def is_unnatural_prime(n):

    n_abs = abs(n)

    if n_abs <= 1:
        return False
    
    # - Looping up to sqrt(n) is efficient and correct
    for i in range(2,int(n_abs ** 0.5) + 1):
        if n_abs%i == 0:
            return False
        
    return True


if __name__ == "__main__":
    print(is_unnatural_prime(7))