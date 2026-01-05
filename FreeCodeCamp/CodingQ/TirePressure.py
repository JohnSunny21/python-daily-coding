"""  
Tire Pressure
Given an array with four numbers representing the tire pressures in psi of the four tires in your vehicle, and another array of two numbers representing the minimum and maximum pressure for your tires in bar, return an array of four strings describing each tire's status.

1 bar equal 14.5038 psi.
Return an array with the following values for each tire:

"Low" if the tire pressure is below the minimum allowed.
"Good" if it's between the minimum and maximum allowed.
"High" if it's above the maximum allowed.
"""

import unittest

class TirePressureTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(tire_status([32, 28, 35, 29], [2, 3]), ["Good", "Low", "Good", "Low"])

    def test2(self):
        self.assertEqual(tire_status([32, 28, 35, 30], [2, 2.3]), ["Good", "Low", "High", "Good"])

    def test3(self):
        self.assertEqual(tire_status([29, 26, 31, 28], [2.1, 2.5]), ["Low", "Low", "Good", "Low"])

    def test4(self):
        self.assertEqual(tire_status([31, 31, 30, 29], [1.5, 2]), ["High", "High", "High", "Good"])

    def test5(self):
        self.assertEqual(tire_status([30, 28, 30, 29], [1.9, 2.1]), ["Good", "Good", "Good", "Good"])

    


def tire_status(pressures_psi, range_bar):

    pressure_psi_bar = map(lambda x: x / 14.5038, pressures_psi)

    minimum, maximum = range_bar
    result = []

    for pressure in pressure_psi_bar:
        if pressure < minimum:
            result.append("Low")
        elif minimum <= pressure <= maximum:
            result.append("Good")
        else:
            result.append("High")

    return result


""" 
-> The above solution works because consistently converted psi -> bar before comparision.
-> But it's more efficient and less error-prone to convert the limits into psi once, and compare directly against the original psi values.
-> Both approaches are valid - the difference is in efficiency and clarity.



pressure_psi_bar = map(lambda x: x / 14.5038, pressures_psi)
=> You're converting each tire pressure from psi -> bar.
=> Then you compare those values against minimu, maximum which are already in bar.
=> That part is consistent.

So logically, it works == you're comparing bar to bar.


The subtle issue will be

The problem statement asked for.
=> Input tire pressure in psi
=> Limits in bar.
=> Output statuses.

The simplest approach is usually to convert the limits into psi(instead of converting every tire pressure into bar.). why?
=> You only convert two numbers( min and max ) instead of four tire pressures.
=> It avoids floating - point rounding errors across multiple conversions.
=> It keeps the tire pressures in their original unit(psi), which is often easier to debub.
"""


def tire_status(pressures_psi, range_bar):

    min_bar, max_bar, = range_bar
    min_psi = min_bar * 14.5038
    max_psi = max_bar * 14.5038

    result = []
    for p in pressures_psi:
        if p < min_psi:
            result.append("Low")
        elif p > max_psi:
            result.append("High")
        else:
            result.append("Good")

    return result


def tire_status_one_liner(pressures_psi, range_bar):

    min_psi , max_psi = [x * 14.5038 for x in range_bar]
    return ["Low" if p < min_psi else "High" if p > max_psi else "Good" for p in pressures_psi]


""" 
=> Convert bar limits -> psi
=> Compare each tire pressure against those limits.
=> return "Low", "Good","High" accordingly.
"""




if __name__ == "__main__":
    unittest.main()