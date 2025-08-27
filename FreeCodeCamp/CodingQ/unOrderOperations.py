"""
Given an array of integers and an array of string operators, apply the operations to the numbers sequentially from left-to-right. 
Repeat the operations as needed until all numbers are used. Return the final result.

For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 1 + 2 * 3 + 4 * 5 from left-to-right 
ignoring standard order of operations.

Valid operators are +, -, *, /, and %.
"""

def evaluate(numbers,operations):

    result = numbers[0]
    op_len = len(operations)

    for i in range(1,len(numbers)):
        op = operations[(i-1) % op_len]
        num = numbers[i]

        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            result /= num
        elif op == '%':
            result %= num
        
    return result


if __name__ == "__main__":
    print(evaluate([5, 6, 7, 8, 9], ['+', '-']))