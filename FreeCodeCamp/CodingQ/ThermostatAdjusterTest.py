import unittest
from ThermostatAdjuster import adjust_thermostat

class ThermostatAdjusterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(adjust_thermostat(68,72),"heat")

    def test2(self):
        self.assertEqual(adjust_thermostat(75,72),"cool")

    def test3(self):
        self.assertEqual(adjust_thermostat(72,72),"hold")

    def test4(self):
        self.assertEqual(adjust_thermostat(-20.5,-10.1),"heat")

    def test5(self):
        self.assertEqual(adjust_thermostat(100,99.9),"cool")

    def test6(self):
        self.assertEqual(adjust_thermostat(0.0,0.0),"hold")

if __name__ == "__main__":
    unittest.main()