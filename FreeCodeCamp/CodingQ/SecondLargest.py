"""
2nd Largest
Given an array, return the second largest distinct number.
"""

# Normal method
def second_largest(arr):

    if len(arr) < 2:
        return None
    result = sorted(set(arr)) # set(arr) - O(n) and sorted() is O(logn)

    return result[-2] # Final access O(1)

#Nor mal method
def second_largest_2(arr):
    distinct = list(set(arr))

    if len(distinct) < 2:
        return None 
    
    distinct.sort(reverse=True)
    return distinct[1]

def second_largest_optimized(arr):

    first = second = float('-inf')

    seen = set()

    for num in arr:
        if num not in seen:
            seen.add(num)
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
    
    return second if len(seen) >=2 else None






if __name__ == "__main__":
    print(second_largest_optimized([1,2,3,4]))
    print(second_largest_optimized([20,139,94,67,31]))
    print(second_largest_optimized([2,3,4,6,6]))
    