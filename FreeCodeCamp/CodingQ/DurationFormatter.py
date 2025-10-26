"""
Duration Formatter
Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

Seconds: Should always be two digits.
Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
Hours: Should be included only if they're greater than zero.
"""
import unittest

class DurationFormatterTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(format_meth(500),"8:20")
    
    def test2(self):
        self.assertEqual(format_meth(4000),"1:6:40")
    
    def test3(self):
        self.assertEqual(format_meth(1),"0:01")

    def test4(self):
        self.assertEqual(format_meth(5555),"1:32:35")
    
    def test5(self):
        self.assertEqual(format_meth(99999),"27:46:39")



def format_meth(seconds):

    hours = seconds // 60 // 60
    minutes = seconds // 60 % 60
    seconds = seconds % 60
    # if minutes < 10:
    #     minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)

    if hours:
        return f"{hours}:{minutes}:{seconds}"
    else:
        return f"{minutes}:{seconds}"
    

    
def format_meth_refined(seconds):
    hours = seconds // 3600 
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    # Format seconds with two digits
    secs_str = f"{secs:02d}"

    # Format minutes without leading  zeros unless it's zero

    minutes_str = str(minutes)

    if hours > 0:
        return f"{hours}:{minutes_str}:{secs_str}"
    
    else:
        return f"{minutes_str}:{secs_str}"


if __name__ == "__main__":
    print(format_meth(500))
    print(format_meth(4000))
    unittest.main()
