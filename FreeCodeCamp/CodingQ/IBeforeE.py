""" 


I Before E
Given a word or sentence, return a corrected version where every word follows the "I before E except after C" rule.

If a word contains "ei" not preceded by "c", replace it with "ie".
If a word contains "ie" preceded by "c", replace it with "ei".
All other words are left unchanged.
"""



import unittest


class IBeforeETest(unittest.TestCase):


    def test1(self):
        self.assertEqual(i_before_e("beleive"), "believe")

    def test2(self):
        self.assertEqual(i_before_e("recieve"), "receive")

    def test3(self):
        self.assertEqual(i_before_e("we recieved a breif"), "we received a brief")

    def test4(self):
        self.assertEqual(i_before_e("she beleived the friendly niece could percieve the greif"), "she believed the friendly niece could perceive the grief")

    def test5(self):
        self.assertEqual(i_before_e("we recieved relief after the theif gave us a breif piece of feirce deceit"), "we received relief after the thief gave us a brief piece of fierce deceit")


TESTCASES = [
    (("beleive",), "believe"),
    (("recieve",), "receive"),
    (("we recieved a breif",), "we received a brief"),
    (("she beleived the friendly niece could percieve the greif",), "she believed the friendly niece could perceive the grief"),
    (("we recieved relief after the theif gave us a breif piece of feirce deceit",), "we received relief after the thief gave us a brief piece of fierce deceit")
]




def i_before_e(sentence):

    result = []

    n = len(sentence)

    i = 0

    while i < n :
        if i < n - 1 and sentence[i] + sentence[i + 1] == "ei":
            if sentence[i -1] != "c":
                result.append(sentence[i+1])
                result.append(sentence[i])
                i += 2

        elif i < n - 1 and sentence[i] + sentence[i + 1] == "ie":
            if sentence[i - 1] == "c":
                result.append(sentence[i+1])
                result.append(sentence[i])
                i += 2
            else:
                result.append(sentence[i])
                i += 1

        else:
            result.append(sentence[i])
            i += 1

    return "".join(result)

"""

There are some subtle issues here

=> Indexing at the start of the string
    -> You check sentence[i-1] without guarding for i == 0.
    -> At the very beginning, i - 1 is -1, which in Python means "last character of the string" and in javascript it is 'undefined' ".
    -> This can cause incorrect behavior if the word starts with "ei" or "ie".

    Fixing that:

    if i > 0 and sentence[i - 1] != "c":
        ...

=> Swapping logic
    -> You're appending sentence[i + 1] then sentence[i].
    -> That effectively flips "ei" -> "ie" and  "ie" -> "ei".
    -> This works, but it's a bit unintuitive to read.
    -> A clearer way is to directly append the replacement string ("ie" or "ei") instead of pushing characters separately.

=> Multiple occurences
    -> worth noting that overlapping patterns (like "eie") could be tricky.

"""

def I_before_E_two(sentence):

    result = []
    n = len(sentence)
    i = 0

    while i < n:
        if i < n - 1 and sentence[i: i+2] == "ei":
            if i == 0 or sentence[i - 1] != "c":
                result.append("ie")
                i += 2
                continue
        elif i < n - 1 and sentence[i: i+2] == "ie":
            if i > 0 and sentence[i - 1] == "c":
                result.append("ei")
                i += 2
                continue

        result.append(sentence[i])

        i += 1

    return "".join(result)



import re
def i_before_e(sentence):

    words = sentence.split()

    corrected = []

    for word in words:
        # Rule 1: "ei" not after "c" -> replace with "ie"
        word = re.sub(r'(?<!c)ei', 'ie', word)

        # Rule 2: "ie" after "c" -> replace with "ei"
        word = re.sub(r'cie','cei',word)
        corrected.append(word)

    return " ".join(corrected)

""" 
=> (?<!c) -> Negative lookbehind. Ensures "ei" is not preceded by "c".
"""


from utils.benchmark import benchmark


if __name__ == "__main__":

    # print(i_before_e("beleive"))
    print(i_before_e("she beleived the friendly niece could percieve the greif"))
    scores = benchmark(
        {"first": i_before_e},
        TESTCASES,
        10000
    )

    unittest.main()

