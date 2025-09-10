"""
Array Diff
Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

The returned array should be sorted in alphabetical order.
"""

def array_diff(arr1,arr2):

    res = []

    for item in arr1:
        if item not in arr2 and item not in res:
            res.append(item)

    for item in arr2:
        if item not in arr1 and item not in res:
            res.append(item)

    res.sort()
    return res

def array_diff_using_set_operations(arr1,arr2):

    return sorted(set(arr1).symmetric_difference(set(arr2)))
    
"""
 1. Set Difference (set(a) - set(b))
This operation returns all elements that are in set(a) but not in set(b).
Example:
a = {"apple", "banana", "cherry"}
b = {"banana", "date"}

print(set(a) - set(b))  # ➜ {'apple', 'cherry'}


- "banana" is removed because it’s in both
- Only items unique to a remain
Reverse:
print(set(b) - set(a))  # ➜ {'date'}


- This gives items unique to b

🔁 2. Symmetric Difference (set(a).symmetric_difference(set(b)))
This returns all elements that are in either set, but not in both — basically, the union of both differences.
Example:
print(set(a).symmetric_difference(set(b)))  
# ➜ {'apple', 'cherry', 'date'}


- "banana" is excluded because it’s in both
- All other unique items from a and b are included

🔍 Visual Summary
|  |  |  | 
| set(a) - set(b) | ab | {'apple', 'cherry'} | 
| set(b) - set(a) | ba | {'date'} | 
| set(a) ^ set(b) |  | {'apple', 'cherry', 'date'} | 



🧪 When to Use What
- Use set(a) - set(b) when you want to filter out shared items from a
- Use symmetric_difference when you want to find all unique items across both sets


"""

if __name__ == "__main__":
    print(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]))
    print(array_diff(["apple", "banana", "cherry"], ["apple", "banana"]))
    print(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))
    print(array_diff_using_set_operations(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))
