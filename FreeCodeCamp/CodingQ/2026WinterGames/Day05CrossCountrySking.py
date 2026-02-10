"""  

2026 Winter Games Day 5: Cross-Country Skiing
Given an array of finish times for a cross-country ski race, convert them into times behind the winner.

Given times are strings in "H:MM:SS" format.
Given times will be in order from fastest to slowest.
The winners time (fastest time) should correspond to "0".
Each other time should show the time behind the winner, in the format "+M:SS".
For example, given ["1:25:32", "1:26:10", "1:27:05"], return ["0", "+0:38", "+1:33"].
"""

import unittest

class CrossCountrySkingTest(unittest.TestCase):

      def test1(self):
          self.assertEqual(get_relative_results(["1:25:32", "1:26:10", "1:27:05"]), ["0", "+0:38", "+1:33"])

      def test2(self):
          self.assertEqual(get_relative_results(["1:00:01", "1:00:05", "1:00:10"]), ["0", "+0:04", "+0:09"])

      def test3(self):
          self.assertEqual(get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]), ["0", "+0:17", "+0:42", "+2:05"])

      def test4(self):
          self.assertEqual(get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"]), ["0", "+0:02", "+1:01", "+2:17", "+2:45", "+3:03", "+3:59", "+4:18", "+7:06", "+13:07"])

      def test5(self):
          self.assertEqual(get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"]), ["0", "+9:30", "+9:38", "+9:49", "+10:40", "+12:12", "+13:15", "+13:55"])    


import time
def get_relative_results(results):

    def in_seconds(t):
        h, m, s = map(int, t.split(":"))

        return h * 3600 + m * 60 + s
    
    def fomat_diff(diff):
        minutes = diff // 60
        seconds = diff % 60

        return f"+{minutes}:{seconds:02d}"
    
    winner = in_seconds(results[0])
    times = []
    for t in results:
        diff = in_seconds(t) - winner
        if diff == 0:
            times.append("0")
        else:
            times.append(fomat_diff(diff))

    return times



if __name__ == "__main__":
    print(get_relative_results(["1:25:32", "1:26:10", "1:27:05"]))
    unittest.main()