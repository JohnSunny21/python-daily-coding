"""

String Math
Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters between the numbers.

If the count of characters separating two numbers is even, use addition.
If it's odd, use subtraction.
Consecutive digits form a single number.
Operations are applied left to right.
Ignore leading and trailing characters that aren't digits.
For example, given "3ab10c8", return 5. Add 3 and 10 to get 13 because there's an even number of characters between them. Then subtract 8 from 13 because there's an odd number of characters between the result and 8.
"""


import unittest


class StringMathTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(do_math_1("3ab10c8"), 5)

    def test2(self):
        self.assertEqual(do_math_1("6MINUS4"), 2)

    def test3(self):
        self.assertEqual(do_math_1("9plus3"), 12)

    def test4(self):
        self.assertEqual(do_math_1("5fkwo#10i#%.<>15P=@20!#B/25"), 15)

    def test5(self):
        self.assertEqual(do_math_1("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt"), 67)


TESTCASES = [
    (("3ab10c8",), 5),
    (("6MINUS4",), 2),
    (("9plus3",), 12),
    (("5fkwo#10i#%.<>15P=@20!#B/25",), 15),
    (("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt",), 67)
]




def do_math(s):

    num_list = []
    count = 0

    start_index = 0
    for i, char in enumerate(s):
        if char.isdigit():
            start_index = i
            break

    s = s[start_index:]
    
    i = 0


    while i < len(s):


        if s[i].isdigit():
            num = s[i]
            j = i
            if count > 0 and count % 2 == 0:
                while j < len(s) - 1 and  s[j+1].isdigit():
                    num += s[j+1]
                    j += 1
                    i = j
                num_list.append(num_list.pop() + int(num))
                count = 0

            elif count > 0 and count % 2 != 0:
                while j < len(s) - 1 and s[j+1].isdigit():
                    num += s[j+1]
                    j += 1
                    i = j
                num_list.append(num_list.pop() - int(num))
                count = 0
            else:
                num_list.append(int(num))
            i += 1


        else:
            count += 1
            i += 1

    return num_list[0]



def do_math_1(s):

    num_list = []
    count = 0

    start_index = 0
    for i, char in enumerate(s):
        if char.isdigit():
            start_index = i
            break

    s = s[start_index:]
    
    i = 0


    while i < len(s):


        if s[i].isdigit():
            num = s[i]
            j = i
            while j < len(s) - 1 and  s[j+1].isdigit():
                    num += s[j+1]
                    j += 1
                    i = j
            if count > 0 and count % 2 == 0:
                
                num_list.append(num_list.pop() + int(num))
                count = 0

            elif count > 0 and count % 2 != 0:
                
                num_list.append(num_list.pop() - int(num))
                count = 0
            else:
                num_list.append(int(num))
            i += 1


        else:
            count += 1
            i += 1

    return num_list[0]


import re


def string_math(s: str) -> int:

    numbers = []
    positions = []

    for match in re.finditer(r'\d+', s):
        numbers.append(int(match.group()))
        positions.append(match.span())

    if not numbers:
        return 0
    
    result = numbers[0]

    for i in range(1, len(numbers)):
        prev_end = positions[i-1][1]
        curr_start = positions[i][0]

        gap = curr_start - prev_end

        if gap % 2 == 0:
            result += numbers[i]

        else:
            result -= numbers[i]

    return result

"""
=> Regex groups consecutive digits automatically -> no need to manually loop and build numbers.
=> Positions from match.span() give you exact indices -> you can calculate gap lengths directly.
=> The first solution need to be levelled up for Readability, Abstraction: Instead of manually managing count, you could compute gap 
lengths directly from indices  - less state to juggle.

=> Leveraging built-ins (re.finditer, list comprehensions) can make your solutions shorter and cleaner without losing clarity.

"""



from utils.benchmark import benchmark
if __name__ == "__main__":
    # print(do_math("3ab10c8"))
    # print(do_math("9plus3"))
    print(do_math_1("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt"))

    scores = benchmark(
        {"first" : do_math_1,
         "second": string_math},
        TESTCASES,
        10000
    )
    unittest.main()