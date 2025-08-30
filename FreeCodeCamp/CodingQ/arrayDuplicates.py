"""
=======================================>    Array Duplicates    <===================================================
Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in ascending order. If no values appear more than once, return an empty array.

Only include one instance of each value in the returned array.

======================================================================================================================
O/P : 
1. find_duplicates([1, 2, 3, 4, 5]) should return [].
2. find_duplicates([1, 2, 3, 4, 1, 2]) should return [1, 2].
3. find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]) should return [-6, 0, 2, 4, 5, 23].

"""
"""
 This solution is solid in terms of correctness — it does return the right result for most cases. 
 But if we're rating it from a performance and scalability standpoint, 
 it has room for improvement.

 Where It Can Improve ==>

1. Performance Bottleneck
- arr.count(i) runs in O(n) time for each element.
- So your loop becomes O(n²) in worst-case scenarios — especially with large arrays.
2. Redundant Checks
- You're checking arr.count(i) for every element, even if you've already processed it.

so i have used the collections.Counter method 
This runs in O(n) time.
It's cleaner and scales better for large datasets.



The first version  is functionally correct and readable, but not optimal for large inputs.



"""
def find_duplicates(arr):
    res = []
    for i in arr:
        if arr.count(i) > 1:
            if i not in res:
                res.append(i)

    return sorted(res) if res else []


# We can also use the counter function
def find_duplicates_counter(arr):
    from collections import Counter

    counts = Counter(arr)
    duplicates = [num for num, count in counts.items() if count > 1]
    return sorted(duplicates)



if __name__ == "__main__":
    print(find_duplicates([1, 2, 2, 3, 4, 5]))
    print(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]))