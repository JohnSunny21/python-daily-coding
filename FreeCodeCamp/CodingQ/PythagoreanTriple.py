"""  
A Pythagorean triple is a set of integers (a, b, c) such that: a^2 + b^2 = c^2

where c is the hypotenuse.

We want all triples with c <= N.
"""

import math

def pythagorean_triples(limit):

    triples = []
    for a in range(1, limit):
        for b in range(a, limit):

            c2 = a*a + b*b
            c = int(math.isqrt(c2))

            if c*c == c2 and c <= limit:
                triples.append((a, b, c))

    return triples



"""  
=> We loop over possible legs a and b.
=> Compute c2 = a2 + b2
=> If c2 is a perfect square, we've found a triple.
=> Restrict c <= limit.
=> This finds primitive triples (like (3, 4, 5)) and multiples (like (6,8, 10))
"""

if __name__ == "__main__":

    print(pythagorean_triples(20))