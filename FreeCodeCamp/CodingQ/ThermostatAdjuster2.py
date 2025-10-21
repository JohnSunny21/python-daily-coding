"""
Thermostat Adjuster 2
Given the current temperature of a room in Fahrenheit and a target temperature in Celsius, return a string indicating how to adjust the room temperature based on these constraints:

Return "Heat: X degrees Fahrenheit" if the current temperature is below the target. With X being the number of degrees in Fahrenheit to heat the room to reach the target, rounded to 1 decimal place.
Return "Cool: X degrees Fahrenheit" if the current temperature is above the target. With X being the number of degrees in Fahrenheit to cool the room to reach the target, rounded to 1 decimal place.
Return "Hold" if the current temperature is equal to the target.
To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32 to the result (F = (C * 1.8) + 32).
"""
import unittest

class ThermostatAdjusterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(adjust_thermostat(32,0),"Hold")

    def test2(self):
        self.assertEqual(adjust_thermostat(70,25),"Heat: 7.0 degrees Fahrenheit")

    def test3(self):
        self.assertEqual(adjust_thermostat(72,18),"Cool: 7.6 degrees Fahrenheit")
    
    def test4(self):
        self.assertEqual(adjust_thermostat(212,100),"Hold")
    
    def test5(self):
        self.assertEqual(adjust_thermostat(59,22),"Heat: 12.6 degrees Fahrenheit")



def adjust_thermostat(current_f, target_c):

    Fahrenheit  = (target_c * 1.8) + 32


    diff = abs(round(Fahrenheit - current_f,1))

    if current_f == Fahrenheit:
        return "Hold"
    elif current_f < Fahrenheit:
        return f"Heat: {diff} degrees Fahrenheit"
    elif current_f > Fahrenheit:
        return f"Cool: {diff} degrees Fahrenheit"
    


if __name__ == "__main__":
    print(adjust_thermostat(32,0))
    unittest.main()