""" 

Mirror Image
Given two strings, determine if the second string is a mirror image of the first.

A mirror image is formed by reversing the string and replacing each character with its mirror equivalent.

Symmetric characters look like themselves in a mirror:
W, T, Y, U, I, O, H, A, X, V, M, w, o, x, v, 0, 8, =, +, :, |, -, _, *, ^, !, ., and the space ( ).

Mirrored pairs swap with each other in a mirror:
Character	Swaps with
[	]
{	}
<	>
b	d
p	q
(	)
If either string includes a character not in the lists above, it doesn't have mirror image that can be created from the characters.

For example, the mirrored image of "[HOW]" is "[WOH]".
"""


import unittest


class IsMirrorTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(is_mirror_image("[HOW]", "[WOH]"), True)

    def test2(self):
        self.assertEqual(is_mirror_image("MOM", "MOM"), True)

    def test3(self):
        self.assertEqual(is_mirror_image("vow", "wov"), True)

    def test4(self):
        self.assertEqual(is_mirror_image("TIM", "TIM"), False)

    def test5(self):
        self.assertEqual(is_mirror_image("{WOW}", "}WOW{"), False)

    def test6(self):
        self.assertEqual(is_mirror_image("XXVII", "IIV%X"), False)

    def test7(self):
        self.assertEqual(is_mirror_image("><(((*>", "<*)))><"), True)

    def test8(self):
        self.assertEqual(is_mirror_image("WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()", "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW"), True)


TESTCASES = [
    (("[HOW]", "[WOH]",), True),
    (("MOM", "MOM",), True),
    (("vow", "wov",), True),
    (("TIM", "TIM",), False),
    (("{WOW}", "}WOW{",), False),
    (("XXVII", "IIV%X",), False),
    (("><(((*>", "<*)))><",), True),
    (("WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()", "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW",), True)
]





def is_mirror_image(s1, s2):

    result = []

    char_dict = {
        "[" : "]",
        "{" : "}",
        "<" : ">",
        "b" : "d",
        "p" : "q",
        "(" : ")",
        "]": "[",
        "}" : "{",
        ">" : "<",
        "d" : "b",
        "q" : "p",
        ")" : "("
        }
    
    symmetric_characters = {"W","w", "T","Y","U","I","O","H","A","X","V","M","o","x","v","0","8","=","+",":","|","-","_","*","^","!","."," "}
    
    for char in s1:
        if char in char_dict:
            result.append(char_dict[char])
        elif char.isalpha():
            result.append(char)
        elif char in symmetric_characters:
            result.append(char)
        else:
            return False
        
    
        
    return s2 == "".join(result)[::-1]


""" 

=> The above solution has some minor issues
    -> You treat any alphabetic character (char.isalpha()) as symmetric.
    -> But not all letters are symmetric! For example, T is symmetric, but F is not.
    -> This means "TIM" incorrectly passes as "MIT" -> mismatch with expected test case.

    
    So we remove the elif char.isalpha() branch. Only allow characters if they're in symmetric_characters or char_dict.

"""

def is_mirror_image_first(s1, s2):

    result = []

    char_dict = {
        "[" : "]", "]": "[",
        "{" : "}", "}": "{",
        "<" : ">", ">": "<",
        "b" : "d", "d": "b",
        "p" : "q", "q": "p",
        "(" : ")", ")" : "("
    }
    
    symmetric_characters = {"W","w","T","Y","U","I","O","H","A","X","V","M",
                            "o","x","v","0","8","=","+",":","|","-","_","*",
                            "^","!","."," "}
    
    for char in s1:
        if char in char_dict:
            result.append(char_dict[char])
        elif char in symmetric_characters:
            result.append(char)
        else:
            return False
        
    return s2 == "".join(result)[::-1]


"""
-> The bug was over-permissive handling of alphabetic characters.
-> Only characters ih the symmetric set or pairs dictionary should be allowed
"""


def is_mirror_image_opt(s1, s2):
    symmetric = set("WTYUIOHAXVMwoxv08=+:|-_*^!. ")
    pairs = {
        '[': ']', ']': '[',
        '{': '}', '}': '{',
        '<': '>', '>': '<',
        'b': 'd', 'd': 'b',
        'p': 'q', 'q': 'p',
        '(': ')', ')': '('
    }

    def mirror_char(ch):
        if ch in symmetric:
            return ch
        elif ch in pairs:
            return pairs[ch]
        else:
            return None     # Invalid characters
        

    mirrored = []
    for ch in reversed(s1):
        mc = mirror_char(ch)
        if mc is None:
            return False
        mirrored.append(mc)
    

    return "".join(mirrored) == s2




from utils.benchmark import benchmark

if __name__ == "__main__":


    print(is_mirror_image("[HOW]", "[WOH]"))
    print(is_mirror_image("><(((*>", "<*)))><"))
    scores = benchmark(
        {"first": is_mirror_image_first,
         "second": is_mirror_image,
         "third": is_mirror_image_opt},
        TESTCASES,
        10000
    )

    unittest.main()