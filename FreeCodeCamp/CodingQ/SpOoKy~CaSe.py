"""
SpOoKy~CaSe
Given a string representing a variable name, convert it to "spooky case" using the following constraints:

Replace all underscores (_), and hyphens (-) with a tilde (~).
Capitalize the first letter of the string, and every other letter after that, ignore the tilde character when counting.
For example, given hello_world, return HeLlO~wOrLd.
"""

import unittest

class SpookyCaseTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(spookify("hello_world"),"HeLlO~wOrLd")

    def test2(self):
        self.assertEqual(spookify("Spooky_Case"),"SpOoKy~CaSe")

    def test3(self):
        self.assertEqual(spookify("TRICK-or-TREAT"),"TrIcK~oR~tReAt")

    def test4(self):
        self.assertEqual(spookify("c_a-n_d-y_-b-o_w_l"),"C~a~N~d~Y~~b~O~w~L")

    def test5(self):
        self.assertEqual(spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts"),"ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS")

        
def spookify(boo):

    count = 0
    result = ''
    flag = False

    while count < len(boo):

        if boo[count].isalpha() and not flag:
            result += boo[count].upper()
            count += 1
            flag = True
        elif boo[count] in ['-','_']:
            result += '~'
            # flag=not flag
            count+= 1
        else:
            flag = False
            result += boo[count].lower()
            count+= 1


    return 


def spookify_optimized(boo):
    boo = boo.replace('-','~').replace('_','~')
    result = ''
    count = 0

    for char in boo:
        if char == '~':
            result += '~'
        else:
            if count % 2 == 0:
                result += char.upper()
            else:
                result += char.lower()
            count += 1
    return result




if __name__ == "__main__":
    # print(spookify("hello_world"))
    print(spookify("Spooky_Case"))
    unittest.main()