"""
Missing Numbers
Given an array of integers from 1 to n, inclusive, return an array of all the missing integers between 1 and n (where n is the largest number in the given array).

The given array may be unsorted and may contain duplicates.
The returned array should be in ascending order.
If no integers are missing, return an empty array.
"""

def find_missing_numbers(arr):

    if not arr:
        return []
    
    max_num = max(arr)
    num_set = set(arr)


    return [i for i in range(1,max_num + 1) if i not in num_set]


def first_solution(arr):
    
    max_num = max(arr)
    res = []
    for i in range(1,max_num + 1):
        if i not in arr:
            res.append(i)

    return res


if __name__ == "__main__":
    print(find_missing_numbers([1,3,5]))
    print(find_missing_numbers([1,2,3,4,5]))
    print(find_missing_numbers([1,10]))
    print(first_solution([1,3,5]))
    print(first_solution([1,2,3,4,5]))
    print(first_solution([1,10]))
    