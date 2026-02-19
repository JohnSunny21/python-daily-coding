"""   

2026 Winter Games Day 14: Ski Mountaineering
Given the snow depth and slope of a mountain, determine if there's an avalanche risk.

The snow depth values are "Shallow", "Moderate", or "Deep".
Slope values are "Gentle", "Steep", or "Very Steep".
Return "Safe" or "Risky" based on this table:

"Shallow"	"Moderate"	"Deep"
"Gentle"	"Safe"	"Safe"	"Safe"
"Steep"	"Safe"	"Risky"	"Risky"
"Very Steep"	"Safe"	"Risky"	"Risky"
"""


import unittest

class SkiMountaineeringTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(avalanche_risk("Shallow", "Gentle"), "Safe")

      def test2(self):
          self.assertEqual(avalanche_risk("Shallow", "Steep"), "Safe")

      def test3(self):
          self.assertEqual(avalanche_risk("Shallow", "Very Steep"), "Safe")

      def test4(self):
          self.assertEqual(avalanche_risk("Moderate", "Gentle"), "Safe")

      def test5(self):
          self.assertEqual(avalanche_risk("Moderate", "Steep"), "Risky")

      def test6(self):
          self.assertEqual(avalanche_risk("Moderate", "Very Steep"), "Risky")

      def test7(self):
          self.assertEqual(avalanche_risk("Deep", "Gentle"), "Safe")

      def test8(self):
          self.assertEqual(avalanche_risk("Deep", "Steep"), "Risky")

      def test9(self):
          self.assertEqual(avalanche_risk("Deep", "Very Steep"), "Risky")




def avalanche_risk(snow_depth, slope):

    if slope == "Gentle" and snow_depth in ("Shallow", "Moderate", "Deep"):
        return "Safe"
    elif slope == "Steep":
        if snow_depth in ("Moderate", "Deep"): 
            return "Risky"
        else:
            return "Safe"
        
    elif slope == "Very Steep":
        if snow_depth in ("Moderate", "Deep"):
            return "Risky"
        else:
            return "Safe"

"""
The above code can be refined => Cleaner, less Repetition

"""
def avalanche_risk(snow_depth, slope):
    if slope == "Gentle":
        return "Safe"
    elif slope in ("Steep", "Very Steep"):
        if snow_depth in ("Moderate", "Deep"):
            return "Risky"
        return "Safe"
    else:
        return "Safe"     

"""
=> Removed duplication: "Steep" and "Very Steep" share the same logic, so we group them.
=> Added a fallback else to handle unexpected slope values gracefully.
=> Cleaner structure, easier to maintain.
"""

def avalanche_risk(snow_depth, slope):
    risk_table = {
        "Gentle": {"Shallow":"Safe", "Moderate":"Safe","Deep":"Safe"},
        "Steep": {"Shallow":"Safe","Moderate":"Risky","Deep":"Risky"},
        "Very Steep":{"Shallow":"Safe", "Moderate":"Risky", "Deep":"Risky"}
    }

    return risk_table[slope][snow_depth]

"""

=> The solution use a lookup table( nested dictionar) to directly map slope and snow_depth combinations to "Safe" or "Risky".
=> This avoids the long chaiins of if/elif conditions and makes the code easy to read and extend.

"""

def test_avalanche_risk():
    cases = [
        ("Shallow", "Gentle", "Safe"),
        ("Moderate", "Gentle", "Safe"),
        ("Deep", "Gentle", "Safe"),
        ("Shallow", "Steep", "Safe"),
        ("Moderate", "Steep", "Risky"),
        ("Deep", "Steep", "Risky"),
        ("Shallow", "Very Steep", "Safe"),
        ("Moderate", "Very Steep", "Risky"),
        ("Deep", "Very Steep", "Risky"),
    ]


    for snow, slope, expected in cases:
        result = avalanche_risk(snow, slope)
        assert result == expected, f"Failed for {snow}, {slope}: got {result}, expected {expected}"

    print("All test cases passed!")




if __name__ == "__main__":
    unittest.main()
    test_avalanche_risk()
