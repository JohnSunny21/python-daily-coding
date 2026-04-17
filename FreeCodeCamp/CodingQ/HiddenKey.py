""" 

Hidden Key
Welcome to the 250th daily challenge!

Given an encoded string, decode it using an encryption key and return it.

To find the key:

Look at all daily challenges up to today whose challenge number is a multiple of 25 (including this one).
Take the first letter from each of those challenge titles and combine them into a string. If the title starts with a non-letter, find its first letter.
To decode the message, go over each letter in the encoded message and:

Look at the corresponding letter in the key (repeat the key if the message is longer than the key).
Convert the key letter to its corresponding number: "A" = 1, "B" = 2, ..., "Z" = 26.
Shift the encoded letter backward in the alphabet by that number.
If the shift goes before "A", wrap around to "Z".
For example, if the encoded message starts with "Y" and the first key letter is "V" (22), shift "Y" back 22 places to get "C". Repeat this process for each letter to decode the full message.

Only letters are shifted, spaces are returned as-is.
All given and returned letters are uppercase.
"""

import unittest

class HiddenKeyTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(decode_refined("YAVJYNXE"), "CONGRATS")

    def test2(self):
        self.assertEqual(decode_refined("YALLUT PQUMJP"), "CODING LEGEND")

    def test3(self):
        self.assertEqual(decode_refined("UAC DYR EISAKYM"), "YOU ARE AWESOME")

    def test4(self):
        self.assertEqual(decode_refined("GQMS NBMZU"), "KEEP GOING")

    def test5(self):
        self.assertEqual(decode_refined("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB"), "A WINNER IS A DREAMER WHO NEVER GIVES UP")


TESTCASES = [
    (("YAVJYNXE",), "CONGRATS"),
    (("YALLUT PQUMJP",), "CODING LEGEND"),
    (("UAC DYR EISAKYM",), "YOU ARE AWESOME"),
    (("GQMS NBMZU",), "KEEP GOING"),
    (("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB",), "A WINNER IS A DREAMER WHO NEVER GIVES UP")
]

"""
The problem that are multiples of 25 are 25 , 50 ,75, 100, 125, 150, 175 , 200 , 225, 250

The day 25th problem is Vowel Repeater
The day 50th problem is Longest Word
The day 75th problem is Hidden Treasure
The day 100th problem is 100 Characters which is 'C'
The day 125th problem is Game of Life
The day 150th problem is Markdown Unordered list Parser
The day 175th problem is Digital Detox
The day 200th problem is Letter and Number Count
The day 225th problem is No Consecutive Repeats
The day 250th problem is Hidden key

The Encryption key is "vlhcgmdlnh" 
"""

import math
def decode(message):
    encryption_key = "vlhcgmdlnh".upper()
    need_length = math.ceil(len(message) / len(encryption_key))

    full_key = encryption_key * need_length

    char_dict = {chr(i): i - ord('A') + 1 for i in range(65, 91)}

    num_dict = {i - ord('A')  + 1 : chr(i) for i in range(65, 91)}
    result = []

    for key, msg in zip(full_key, message):
        if msg.isalpha():
            letter_num = (char_dict[msg] - char_dict[key]) % 26
            result.append(num_dict[letter_num])
        else:
            result.append(msg)

    return "".join(result)

"""
=> In the above version the repeating of the key is where things went a little off 

    -> In the above verison, you calculate need_length = ceil(len(message) / len(excryption_key)) and then multiply the key string by that. 
    That works fine for generating a long enough key, but when you later zip full_key and message, you're paring them one-to-one. If your full_key overshoots, it's harmless, but if you undershoot
    you'll miss characters.
    -> The bigger issue is that you don't actually need to pre-expand the key at all. You can just use modulo indexing ( i  % len(encryption_key)) to cycle through the
    key as you go. That way, the key nature repeats without worring about length mismatches.


"""


def decode_refined(message):

    encryption_key = "vlhcgmdlnh".upper()
    char_dict = {chr(i) : i - ord('A') + 1 for i in range(65, 91)}
    num_dict = {i: chr(ord('A') + i - 1) for i in range(1, 27)}


    result = []

    for i, msg in enumerate(message):
        if msg.isalpha():
            key = encryption_key[i % len(encryption_key)]  # This cycles the key automatically. there is no need for math.ceil or multiplying the key string.
            shift = char_dict[key]
            letter_num = (char_dict[msg] - shift)  % 26
            # Warp - around : if result is 0, it means 'Z'

            result.append(num_dict[letter_num if letter_num != 0 else 26])
        else:
            result.append(msg)

    return "".join(result)


""" 
=> There actually is a chancce of hitting 0 in above math 
    -> letter_num = (char_dict[msg] - char_dict[key] ) % 26

    -> Suppose char_dict[msg] == char_dict[key].
        Example: encoded letter "A" and key letter "A"
        Then (1 - 1 ) % 26 = 0
    
    -> But the num_dict is built with keys 1 - 26 . There's no entry for 0 
        So if you try num_dict[0], you'll get a keyError.

    That's why the extra check is needed.

    num_dict[letter_num if letter_num != 0 else 26]
    It maps the "0 case" back to 26, which corresponds to "Z".

-> % 26 produces results in the range  0 .. 25
-> But your dictionary is 1... 26
-> So the mismatch happens only when the modulo result is 0.
-> That case means the shifted letter wrapped exactly to "Z".




we can fix that like
Instead of the conditional, you could build num_dict with 0 ... 25 keys

num_dict = {i : chr(ord('A')  i) for i in range(26)}

Then you'd use:

letter_num = (char_dict[msg] - char_dict[key]) % 26
result.append(num_dict[letter_num])

This way, 0 maps to "A" , 25 maps to "Z", and you avoid the special case.
"""


def decode_message(message: str) -> str:
    key = "vlhcgmdlnh".upper()
    result = []
    key_nums = [ord(c) - ord('A') + 1 for c in key]

    for i, ch in enumerate(message):
        if ch == " " :
            result.append(" ")
        else:
            shift = key_nums[i % len(key)]
            new_ord = ord(ch) - shift
            while new_ord < ord('A'):
                new_ord += 26
            result.append(chr(new_ord))

    return "".join(result)

""" 
=> The key acts like repeating shift pattern.
=> It's essentially a variant of the Vigenère cipher, but only shifting backward
"""

# The above version fails cause it treats the space as the key so below solution works.
# 

# Working version:
# The key must advance only when we process a letter.
# Spaces stay unchanged and should NOT consume a key character.
def decode_refined(message: str) -> str:
    encryption_key = "VLHCGMDLNH"
    result = []
    key_index = 0

    for ch in message:
        if ch == " ":
            result.append(" ")
            continue

        # Convert the current key letter to its shift value:
        # A -> 1, B -> 2, ..., Z -> 26
        shift = ord(encryption_key[key_index % len(encryption_key)]) - ord("A") + 1

        # Convert the encoded letter to a 0-based position, shift backward,
        # and wrap around with modulo 26.
        decoded_pos = (ord(ch) - ord("A") - shift) % 26
        result.append(chr(ord("A") + decoded_pos))

        # Only letters move the key forward.
        key_index += 1

    return "".join(result)





from utils.benchmark import benchmark

if __name__ == "__main__":
    print(decode_refined("YALLUT PQUMJP"))
    scores = benchmark(
        {"first": decode_refined},
        TESTCASES,
        10000
    )

    unittest.main()
