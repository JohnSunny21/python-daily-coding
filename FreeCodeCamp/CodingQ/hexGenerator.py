"""
=========================================================>      Hex Generator       <=======================================================================================
Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

The function should handle "red", "green", or "blue" as an input argument.
If the input is not one of those, the function should return "Invalid color".
The function should return a random six-character hex color code where the input color value is greater than any of the others.
Example of valid outputs for a given input:
Input	Output
"red"	"FF0000"
"green"	"00FF00"
"blue"	"0000FF"
=====================================================================================================================================================================================
O/P : ====>


"""

import random
def generate_hex(color):

    color = color.lower()

    if color not in ['red','green','blue']:
        return "Invalid color"
    

    def rand_hex(val):
        return f"{val:02X}"
    
    low1 = random.randint(0,244)
    low2 = random.randint(0,244)
    dominant = random.randint(max(low1,low2)+1,255)


    if color == 'red':
        r , g , b = dominant , low1, low2
    elif color == 'green':
        r , g , b = low1, dominant , low2
    else:
        r, g, b = low1, low2, dominant


    return rand_hex(r) + rand_hex(g) + rand_hex(b)



def test_generate_hex():

    # Test 1: Invalid Color
    assert generate_hex("yellow") == "Invalid color"

    # Test 2: Valid red hex format
    red1 = generate_hex("red")
    assert isinstance(red1,str)
    assert len(red1) == 6
    assert int(red1[:2],16) > int(red1[2:4],16)
    assert int(red1[:2],16) > int(red1[4:],16)

    # Test 3: Two different red outputs

    red2 = generate_hex("red")
    assert red1 != red2

    # Test 4: Valid green hex format

    green1 = generate_hex("green")
    assert isinstance(green1,str)
    assert len(green1) == 6
    assert int(green1[2:4],16) > int(green1[:2],16)
    assert int(green1[2:4],16) > int(green1[4:],16)

    # Test 5: Valid blue hex format
    blue1 = generate_hex("blue")
    assert isinstance(blue1,str)
    assert len(blue1) == 6
    assert int(blue1[4:],16) > int(blue1[:2],16)
    assert int(blue1[4:],16) > int(blue1[2:4],16)

    print("All Tests Passed!")

if __name__ == "__main__":

    print(generate_hex("yellow"))
    test_generate_hex()