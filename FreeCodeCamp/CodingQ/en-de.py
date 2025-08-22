"""
Message Decoder
Given a secret message string, and an integer representing the number of letters that were used to shift the message to encode it, return the decoded string.

A positive number means the message was shifted forward in the alphabet.
A negative number means the message was shifted backward in the alphabet.
Case matters, decoded characters should retain the case of their encoded counterparts.
Non-alphabetical characters should not get decoded.

=========================================================
O/P =============>

decode("Xlmw mw e wigvix qiwweki.", 4) should return "This is a secret message."
decode("Byffi Qilfx!", 20) should return "Hello World!"

"""

def decode_own(message, shift):
    final = ''
    if shift < 0:
        for i in message:
            if (i != " " and i.isalpha()):
                code = ord(i) + shift
                final += chr(code)
            else:
                final += i
    else:
        for i in message:
            if (i != " " and i.isalpha()):
                code = ord(i) - shift
                final += chr(code)
            else:
                final += i
    
    return final



def decode(message, shift):
    final = ''
    if shift > 0:

        for i in message:
            if i.isalpha():
                base = ord('A') if i.isupper() else ord('a')
                code = (ord(i) - base - shift) % 26 + base
                final += chr(code)
            else:
                final += i
    else:
        for i in message:
            if i.isalpha():
                base = ord('A') if i.isupper() else ord('a')
                code = (ord(i) - base - shift) % 26 + base
                final += chr(code)
            else:
                final += i
    return final

def decode2(message, shift):
    final = ''
    for char in message:
        if char.isalpha():
            # Determine ASCII base depending on case
            base = ord('A') if char.isupper() else ord('a')
            # Reverse the shift direction for decoding
            decoded_char = chr((ord(char) - base - shift) % 26 + base)
            final += decoded_char
        else:
            # Keep non-alphabet characters as-is
            final += char
    return final

print(decode("Zqd xnt njzx?", -1))


# print(decode("Xlmw mw e wigvix qiwweki.", 4))
