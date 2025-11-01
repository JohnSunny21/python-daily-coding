"""
Signature Validation
Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

Letters in the message and secret key have these values:
a to z have values 1 to 26 respectively.
A to Z have values 27 to 52 respectively.
All other characters have no value.
Compute the signature by taking the sum of the message plus the sum of the secret key.
For example, given the message "foo" and the secret key "bar", the signature would be 57:

f (6) + o (15) + o (15) = 36
b (2) + a (1) + r (18) = 21
36 + 21 = 57
Check if the computed signature matches the provided signature.

"""

import unittest

class SignatureValidationTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(verify("foo","bar",57),True)
    
    def test2(self):
        self.assertEqual(verify("foo","bar",54),False)

    def test3(self):
        self.assertEqual(verify("freeCodeCamp","Rocks",238),True)

    def test4(self):
        self.assertEqual(verify("Is this valid?","No",210),False)

    def test5(self):
        self.assertEqual(verify("Is this valid?","Yes",233),True)

    def test6(self):
        self.assertEqual(verify("Check out the freeCodeCamp podcast,","in the mobile app",514),True)


def verify(message, key, signature):
    result = 0
    lower = {chr(i): ord(chr(i)) - ord('a') + 1 for i in range(97, 123)}
    upper = {chr(i): ord(chr(i)) - ord('A') + 27 for i in range(65, 91)}
    letters = {**lower, **upper}

    for char in message:
        if char in letters:
            result += letters[char]
        else:
            result += 0

    for char in key:
        if char in letters:
            result += letters[char]
        else:
            result += 0

    return signature == result


"""
Time complexity for the verify method 
- Dictionary lookup (letters[char]) is O(1) average-case time.
- Total time complexity:
    Let m be the length of message , and k be the length of key.
    This code runs in O(m + k) time.
This is efficient and scales well.

But the Time complexity for the verify_optimized method
Function call overhead is O(1) per call - python function calls are fast
but not free.
The logic inside also O(1).
Total time complexity : still O(m + k).
But here calling a function per character adds overhead, especially in tight loops or large-scale processing.


    Approach        lookup      Memory Usage        Readability         Scalability

    dictionary      O(1)        Slightly more           clear           Excellent
    approach    

    Optimized       O(1)            Minimal             Compact          Slightly overhead
"""


# Lets' talk about the performance here 
"""
The first verify method run in 0.001s to run the test case but the optimized method run in 0.000s
 
even though the lookup is fast but still the optimized is fast for this testcases.

1. Function call overhead
    - In CPython (the standard Python Interpreter), function calls are not free, Each call involves
    The stack frame setup, argument passing , and return handling.
    - So yes, calliing char_value() per character introduces micro-latency.

2. Dict Lookup
    - The Dictionary - look up in Python are amortized O(1) and extremely fast - especially for small, fixed-size dictionaries  like (52Keys) 
    in the verify method.

3. Real-World Performance
    - For short strings, the difference is negligible - both complete in undera millisecond.
    - For Large-scale inputs(e.g., validating millions of messages,) the verify() will scale better due to reduced function call 
    overhead and better CPU cache locality.

Final Conclusion:
The verify() is more performant in practice for large-scale workloads.



Benchmarking Reality

let's say we benchmark both approahes on a 1M - character input:
    Approach            Time (approx)
    
    Function per char       ~0.25s
    Dict lookup             ~0.18s

    The verify() wins in raw throughput


Production Engineering Perspective
If this was used in the production grade system, 

Factor              Dict-Based(verity)           Function-Based(verify_optimized)

Performance         Faster for large inputs             Slighly slower

Readability         clear, explicti mapping             Compact logic

Memory              Slightly higher(52key dict)         Minimal

Extensibility       Easy to add more chars              Needs more logic

Best for            High-throughout, large-scale        Lightweight scripts, clarity
                    validation                      
"""


def verify_optimized(message, key, signature):
    def char_value(c):
        if 'a' <= c <= 'z':
            return ord(c) - ord('a') + 1
        elif 'A' <= c <= 'Z':
            return ord(c) - ord('A') + 27
        else: 
            return 0
        
    result = sum([char_value(c) for c in message+key])
    return signature == result

if __name__ == "__main__":
    print(verify("foo","bar",57))
    unittest.main()
