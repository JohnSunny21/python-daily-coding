"""
================================================>       Targeted Sum        <====================================================================================
Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.

The returned array should have the indices in ascending order.


=======================================================================================================================================
O/P : ====>

1. find_target([2, 7, 11, 15], 9) should return [0, 1].
2. find_target([3, 2, 4, 5], 6) should return [1, 2].
3. find_target([1, 3, 5, 6, 7, 8], 15) should return [4, 5].
4. find_target([1, 3, 5, 7], 14) should return 'Target not found'.
"""

# Brute force 
# Time complexity : O(n**2)
# Space Complexity : O(1)
def find_target_brute(arr,target):

    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return [i,j]
    else:
        return "Target not found"
    
def find_target(arr,target):
    c = {}
    for i in range(len(arr)):
        c[arr[i]] = i

    for i in range(len(arr)):
        y = target - arr[i]

        if y in c and c[y] != i:
            return [i,c[y]]
    else:
        return "Target not found"
    

if __name__ == "__main__":
    print(find_target([2,7,11,15],9))

