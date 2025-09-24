"""
Perfect Square
Given an integer, determine if it is a perfect square.

A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.
"""

# Normal execution O(n)
def is_perfect_square_normal(n):

    for i in range(n):
        if i * i == n:
            return True
    return False


# The Optimal execution O(logn)
def is_perfect_square_optimal(n):

    if n < 0:
        return False
    if n in (0,1):
        return True
    
    low , high = 0 , (n//2) + 1

    while low <= high:
        mid = (low + high) // 2
        squared = mid * mid

        if squared == n:
            return True
        elif squared < n:
            low = mid + 1
        elif squared > n:
            high = mid - 1

    return False

# Constant time solution O(1)
def is_perfect_square(n):
    if n < 0:
        return False
    if n in (0,1):
        return True
    
    root = int(n**0.5)
    return root * root == n


if __name__ == "__main__":
    print(is_perfect_square(9))
    print(is_perfect_square(49))
    print(is_perfect_square(1))
    print(is_perfect_square(2))
