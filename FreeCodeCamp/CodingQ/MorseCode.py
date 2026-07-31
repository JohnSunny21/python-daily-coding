""" 


Morse Code
Given a Morse code string, return the decoded message using the following table:

Code	Letter	Code	Letter
.-	A	-.	N
-...	B	---	O
-.-.	C	.--.	P
-..	D	--.-	Q
.	E	.-.	R
..-.	F	...	S
--.	G	-	T
....	H	..-	U
..	I	...-	V
.---	J	.--	W
-.-	K	-..-	X
.-..	L	-.--	Y
--	M	--..	Z
Letters are separated by a single space
Words are separated by three spaces
"""

import unittest

class MorseCodeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(decode_morse("--.."), "Z")

    def test2(self):
        self.assertEqual(decode_morse("... --- ..."), "SOS")

    def test3(self):
        self.assertEqual(decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--."), "FREECODECAMP")

    def test4(self):
        self.assertEqual(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."), "HELLO WORLD")

    def test5(self):
        self.assertEqual(decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --."), "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG")


TESTCASES = [
    (("--..",), "Z"),
    (("... --- ...",), "SOS"),
    (("..-. .-. . . -.-. --- -.. . -.-. .- -- .--.",), "FREECODECAMP"),
    ((".... . .-.. .-.. ---   .-- --- .-. .-.. -..",), "HELLO WORLD"),
    (("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --.",), "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG")
]


morse_dict = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z"

}



def decode_morse(code):

    words = code.split("   ")


    result = []

    for word in words:

        letters = word.split(" ")
        temp_word = []
        for item in letters:
            temp_word.append(morse_dict[item])

        result.append("".join(temp_word))

    return " ".join(result)




from utils.benchmark import benchmark

if __name__ == "__main__":

    scores = benchmark({"first": decode_morse}, TESTCASES, 10000)

    unittest.main()