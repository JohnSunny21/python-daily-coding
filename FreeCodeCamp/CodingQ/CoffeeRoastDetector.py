""" 


Coffee Roast Detector
Given a string representing the beans used to make a cup of coffee, determine the roast of the cup.

The given string will contain the following characters, each representing a type of bean:

An apostrophe (') is a light roast bean worth 1 point each.
A dash (-) is a medium roast bean worth 2 points each.
A period (.) is a dark roast bean worth 3 points each.
The roast level is determined by the average of all the beans.

Return:

"Light" if the average is less than 1.75.
"Medium" if the average is 1.75 to 2.5.
"Dark" if the average is greater than 2.5.
"""

import unittest


class CoffeeRoastDetectorTest(unittest.TestCase):

    pass



def detect_roast(beans):

    light = []
    medium = []
    dark = []

    for char in beans:
        if char == "'":
            light.append(1)
        elif char == "-":
            medium.append(2)
        elif char == ".":
            dark.append(3)
    
    
    light = sum(light) / len(light) if light else 0
    medium = sum(medium) / len(medium) if medium else 0
    dark = sum(dark) / len(dark) if dark else 0


    avg = (light + medium + dark) / 3


    if avg < 1.75:
        return "Light"
    elif 1.75 <= avg <= 2.5:
        return "Medium"
    else:
        return "Dark"
    





if __name__ == "__main__":
    print(detect_roast("''-''''''-'-''--''''"))
    # unittest.main()