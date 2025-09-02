"""  
RGB to Hex
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:

Input	Output
"rgb(255, 255, 255)"	"#ffffff"
"rgb(1, 2, 3)"	"#010203"
Make any letters lowercase.
Return a # followed by six characters. Don't use any shorthand values.
"""
def rgb_to_hex(rgb):
    r , g , b = map(int,rgb[4:-1].split(","))

    return f"#{r:02X}{g:02X}{b:02X}".lower()

if __name__ == "__main__":
    print(rgb_to_hex("rgb(1,11,111)"))
    print(rgb_to_hex("rgb(2,22, 223)"))

    