"""
Reverse Parenthesis
Given a string that contains properly nested parentheses, return the decoded version of the string using the following rules:

All characters inside each pair of parentheses should be reversed.
Parentheses should be removed from the final result.
If parentheses are nested, the innermost pair should be reversed first, and then its result should be included in the reversal of the outer pair.
Assume all parentheses are evenly balanced and correctly nested.
=============================================
O/P ====> decode("(f(b(dc)e)a)") should return "abcdef".


"""
def decode(s):
    stack = []

    for char in s:
        if char == ')':
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()
            stack.extend(temp)
        else:
            stack.append(char)
    
    return ''.join(stack)



def encode(s, chunk_size= 2):
    chunks = []
    i = len(s)

    while i > 0:
        start = max(0, i-chunk_size)
        chunks.append(s[start:i])
        i -= chunk_size

    encoded = chunks[0]
    for chunk in chunks[1:]:
        encoded = f"({chunk}{encoded})"

    return encoded

if __name__ == "__main__":

    print(decode("(f(b(dc)e)a)"))
    print(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"))
    print(decode("f(Ce(re))o((e(aC)m)d)p"))