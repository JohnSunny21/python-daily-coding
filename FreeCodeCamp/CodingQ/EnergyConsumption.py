"""  

Energy Consumption
Given the number of Calories burned during a workout, and the number of watt-hours used by your electronic devices during that workout, determine which one used more energy.

To compare them, convert both values to joules using the following conversions:

1 Calorie equals 4184 joules.
1 watt-hour equals 3600 joules.
Return:

"Workout" if the workout used more energy.
"Devices" if the device used more energy.
"Equal" if both used the same amount of energy.
"""


import unittest

class EnergyConsumptionTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(compare_energy(250, 50), "Workout")

    def test2(self):
        self.assertEqual(compare_energy(100, 200), "Devices")
    
    def test3(self):
        self.assertEqual(compare_energy(450, 523), "Equal")

    def test4(self):
        self.assertEqual(compare_energy(300, 75), "Workout")

    def test5(self):
        self.assertEqual(compare_energy(200, 250), "Devices")

    def test6(self):
        self.assertEqual(compare_energy(900, 1046), "Equal")


def compare_energy(calories_burned, watt_hours_used):

    workout_energy = calories_burned * 4184
    device_energy = watt_hours_used * 3600

    if workout_energy > device_energy:
        return "Workout"
    elif device_energy > workout_energy:
        return "Devices"
    else:
        return "Equal"
    


if __name__ == "__main__":

    unittest.main()