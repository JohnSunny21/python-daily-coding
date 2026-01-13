"""  
Odd or Even?
Given a positive integer, return "Odd" if it's an odd number, and "Even" is it's even.
"""

import unittest

class OddOrEvenTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(odd_or_even(1), "Odd")

    def test2(self):
        self.assertEqual(odd_or_even(2), "Even")

    def test3(self):
        self.assertEqual(odd_or_even(13), "Odd")

    def test4(self):
        self.assertEqual(odd_or_even(196), "Even")

    def test5(self):
        self.assertEqual(odd_or_even(123456789), "Odd")



def odd_or_even(n):

    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def odd_or_even(n):

    return "Even" if n % 2 == 0 else "Odd"
    
def odd_or_even_bit_wise(n):

    return "Odd" if (n & 1) else "Even"

""" 


1. What does n & 1 mean?
=> & is the bitwise AND operator.
=> It compares each bit of two numbers.
=> 1 in binary is ...0001.
=> So n & 1 checks only the last bit of n.


2. Why does the last bit matter?
=> In binary, even numbers always end with 0, odd numbers end with 1.
    Example:
        -> 4 -> 100 (last bit = 0 -> even)
        -> 7 -> 111 (last bit = 1 -> odd)

3. How the check works
=> If n & 1 == 1 -> last bit is 1 -> Odd.
=> If n & 1 == 0 -> last bit is 0 -> Even.

4. Why use bitwise instead of %?
-> % 2 is more readable and common in high-level code.
-> n & 1 is faster at the machine level because it directly inspects the binary representation.
-> In practice, modern compilers optimize % 2 into the same bitwise operation, so performance difference is negligible.
-> But n & 1 is a neat trick that shows you understand how numbers are represented in binary.


Method              Code                Idea

Modulus             n % 2 == 0          Divide by 2, check remainder

Bitwise AND         n & 1 == 0          Inspect last binary bit

Both are correct - modulus is more readable, bitwise is lower-level and faster in theory.

The paranthesis for the case of the remainder but not the other is

=> Here, n % 2 == 0 is a comparison expression.
-> Python's operator precedence makes it clear: % is evaluated first , then ==
=> so parathesis aren't needed = the intent is obvious.


In the next example 

-> n & 1 is a bitwisee operation.
-> It produces either 0 or 1.
-> Since 0 is falsy and 1 is truthy, we use it directly in the conditional expression.
-> Parentheses are added for clarity, not necessity, you could write.

return "Odd" if n & 1 else "Even"

-> it works the same as well. But many developers prefer parantheses around bitwise expressions to make it visually clear that the condition is based on a binary mask, not a logical comparison.

No functional difference - paranthesis are just stylistic clarity in the bitwise case.

Logical AND     , OR , NOT  work with truth values (True/ False)
    Example:
        if x > 0 and y > 0:
            print("Both positive")
        => Bitwise operators:
            & (AND), | (OR), ^(XOR), -(NOT) , <<(LEFT SHIFT), >> (RIGHT SHIFT)

        -> Work at the bit level of integers.
        -> Example: 
            a = 6       # 110 in binary
            b = 3       # 011 in binary

            print(a & b) # 2 (010)
            print(a | b) # 7 (111)
            print(a ^ b) # 5 (101)


Logical operators (and , or) work on truth values.
Bitwise operators (&, |, ^) work on the binary representation of integers .
"""

if __name__ == "__main__":

    print(odd_or_even(20))
    unittest.main()