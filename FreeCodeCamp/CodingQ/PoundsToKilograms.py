""" 
Pounds to Kilograms
Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

Replace "(lbs)" with the input number.
Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
1 pound equals 0.453592 kilograms.
If the input is 1, use "pound" instead of "pounds".
If the converted value is 1, use "kilogram" instead of "kilograms".
"""

import unittest

class PoundsToKilograms(unittest.TestCase):

    def test1(self):
        self.assertEqual(convert_to_kgs(1), "1 pound equals 0.45 kilograms.")

    def test2(self):
        self.assertEqual(convert_to_kgs(0),"0 pounds equals 0.00 kilograms.")

    def test3(self):
        self.assertEqual(convert_to_kgs(100),"100 pounds equals 45.36 kilograms.")

    def test4(self):
        self.assertEqual(convert_to_kgs(2.5), "2.5 pounds equals 1.13 kilograms.")

    def test5(self):
        self.assertEqual(convert_to_kgs(2.20462),"2.20462 pounds equals 1.00 kilograms.")


"""
Subtle issue with this approach

The condition: 
    if kilograms == 1:
        ddelimiter = "kilogram"

is fragile because kilograms is a float.

    lbs = 2.20462
    kilograms = round(lbs * 0.453592, 2) # 1.0

Here kilograms == 1 is true, so you get "1.00 kilogram". That works

But if floating - point rounding gave 0.9999999 -> 1.0, it's fine.
However, if you ever compare floats directly, it can be risky. A safer approach is to compare the formatted string.
refining the below code.

"""
def convert_to_kgs(lbs):

    kilograms = round (lbs * 0.453592,2)

    pdelimiter = "pounds"
    ddelimiter = "kilograms"

    if lbs == 1:
        pdelimiter = "pound"
    if kilograms == 1:
        ddelimiter = "kilogram"

    return f"{lbs} {pdelimiter} equals {kilograms:.2f} {ddelimiter}"


def convert_to_kgs_refined(lbs):

    kilograms = lbs * 0.453592
    kgs_str = f"{kilograms:.2f}"

    pdelimiter = "pound" if lbs == 1 else "pounds"
    ddelimiter = "kilogram" if kgs_str == "1.00" else "kilograms"

    return f"{lbs} {pdelimiter} equals {kgs_str} {ddelimiter}."

def convert_to_kgs(lbs):

    kgs = lbs * 0.453592
    kgs_str = f"{kgs:.2f}" # always 2 decimals

    pound_word = "pound" if lbs == 1 else "pounds"
    kilogram_word = "kilogram" if kgs == "1.00" else "kilograms"

    return f"{lbs} {pound_word} equals {kgs_str} {kilogram_word}."


if __name__ == "__main__":
    print(convert_to_kgs(50))
    unittest.main()