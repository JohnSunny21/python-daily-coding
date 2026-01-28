"""  
Flatten the Array
Given an array that contains nested arrays, return a new array with all values flattened into a single, one-dimensional array. Retain the original order of the items in the arrays
"""

import unittest


class FlattenArrayTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(flatten_array([1, [2, 3], 4]), [1, 2, 3, 4])

    def test2(self):
        self.assertEqual(flatten_array([5, [4, [3, 2]], 1]), [5, 4, 3, 2, 1])

    def test3(self):
        self.assertEqual(flatten_array(["A", [[[["B"]]]], "C"]), ["A", "B", "C"])

    def test4(self):
        self.assertEqual(flatten_array([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]), ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

    def test5(self):
        self.assertEqual(flatten_array([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]), ["red","blue","green","yellow","purple","orange","pink","brown"])





def flatten_array(arr):

    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_array(item))
        else:
            result.append(item)


    return result

"""
Could have also used the itertools.chain.from_iterable works only for one level, so recursion is better.


The Recursion is the most robust way to flatten arbitrarily

Moder languages often provide built-in helpers .flat(infinity) in JS, numpy.flatten() in Python for numeric array).

"""

# This is the iterative stack - based approach to flatten arrays without recursion. This is useful when recursion depth could be a concern with
# very deepply nested arrays.

def flatten_array(arr):

    result = []
    stack = arr[::-1]

    while stack:
        item = stack.pop()
        if isinstance(item,list):
            stack.extend(item[::-1])
        else:
            result.append(item)

    return result


"""
=> We use a stack to simulate recursion.
-> Reverse the array so popping preserves the original
-> When encountering a nested array, push its elements back onto the stack(also reversed)
=> Continue until the stack is empty
"""

# This is the generator-based approach in Python that flattens arrays lazily, This way, you don't build
# entire flattened list at once, but yield values one by one (it is great for huge arrrays).

def flatten_array_generator_based(arr):
    for item in arr:
        if isinstance(item, list):
            yield from flatten_array(item)

        else:
            yield item


""" 
=> Lazy evaluation: Values are produced one at a time, so memory usage stays low.
-> Scalable: Handles very large or deeply nested arrays without building huge intermediate lists.
-> Flexible: You can consume results in a loop, stream them, or convert to a list when needed.

This is more Pythonic way to flatten arrays when you want efficiency and elegance.
"""

# This is a generator-based flatten function full generic, so it can handle not just lists, but any iterable(like tuples, sets, etc), while still preserving order to ordered types.

from collections.abc import Iterable

def flatten(iterable):

    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item

""" 

=> Exclude str and bytes so they don't get split into characters.
=> Works for lists, tuples, sets, frozensets, generators,etc.
=> Preserves order for ordered collections (lists, tuples).
=> For unordered collections (sets), order i naturally not guaranteed.
"""


from typing import Any, Iterable, Iterator, Union
from collections.abc import Iterable as ABCIterable

def flatten(iterable: Iterable[Any]) -> Iterator[Any]:
    """  
    Recursively flattens any nested iterable (except str/bytes) into a one-dimensional sequence.

    Args:
        iterable (Iterable[Any]): The nested iterable to flatten.

    Returns:
        Iterator[Any]: A generator yiellding flattened elements.
    """

    for item in iterable:
        if isinstance(item, ABCIterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item

""" 

=> Input type: Iterable[Any] -> accepts lists, typles, sets, generators, etc.
=> Output type: Iterable[Any] -> Yields values lazily.
-> Exclusions: str and bytes are treated as atomic values, not split into characters.
-> Type hints make it clear that this function is generic and works with any nested iterable.

"""


"""
typing.Iterable vs collections.abc.iterable

1. Their purpose
=> typing.Iterable
    -> Exists for type hints.
    -> Used to annotate function signature so tools like mypy or IDE's know what kinds of values are expected.
    -> Example:
        from typing import Iterable

        def process(items: Iterable[int]) -> None:
        
=> collections.abc.iterable
    -> Exists for runtime checks.
    -> You can use it with isinstance() or issubclass() to check if an object is iterable at runtime.
    -> Example:
        from collection.abc import Iterable

        print(isinstance([1, 2, 3]), Iterable)
        print(isinstance(42, Iterable))

2. Why the Difference Matters
    -> typing.Iterable is not designed for isintance() checks - it will raise a TypeError if you try:
        from typing import Itreable
            isinstance([1, 2, 3], Iterable) # TypeError

    -> collections.abc.Iterable works perfectly for runtime checks:
        from collections.abc import Iterable
        isinstacne([1, 2, 3], Iterable) # True
    
3. Best to use
    -> Use typing.Iterable in function signatures for type hints.
    -> Use collections.abc.iterable in runtime logic (like flattening arrays, validating inputs).


    
typing.iterable -> for static type hints.
collections.abc.Iterable -> for runtime checks.
They serve different rolse, so you often use both in the same project, one for annotations, one for actual logic.
"""



if __name__ == "__main__":

    nested = [1, [2, 3], [4, [5, 6]], 7]

    for val in flatten_array(nested):
        print(val, end=" ")


    nested_list = [1, (2, 3), {4, 5}, [6, [7, 8]], "hello"]
    print(list(flatten(nested_list)))
    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 'hello']

    nested_tuple = (1, (2, (3, 4)), 5)
    print(list(flatten(nested_tuple)))
    # Output: [1, 2, 3, 4, 5]

    nested_set = {1, (2, 3), frozenset([4, 5])}
    print(list(flatten(nested_set)))

    unittest.main()