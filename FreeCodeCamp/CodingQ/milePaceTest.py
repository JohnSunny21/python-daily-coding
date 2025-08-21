import unittest
from milePace import mile_pace

class milePaceTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(mile_pace(3,"24:00"),"08:00")

    def test2(self):
        self.assertEqual(mile_pace(1,"06:45"),"06:45")

    def test3(self):
        self.assertEqual(mile_pace(2,"07:00"),"03:30")

    def test4(self):
        self.assertEqual(mile_pace(26.2,"120:35"),"04:36")

if __name__ == "__main__":
    unittest.main()