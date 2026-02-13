"""  

2026 Winter Games Day 8: Luge
Given an array of five numbers, each representing the time (in seconds) it took a luger to complete a segment of a track, determine which segment had the fastest speed and what that speed was.

The track is divided into the following segments:

Segment 1: 320 meters
Segment 2: 280 meters
Segment 3: 350 meters
Segment 4: 300 meters
Segment 5: 250 meters
The first value in the given array corresponds to the time for segment 1, the second value to segment 2, and so on.

To calculate the speed (in meters per second) for a segment, divide the distance by the time.

Return "The luger's fastest speed was X m/s on segment Y.". Where X is the fastest speed, rounded to two decimal places, and Y is the segment number where the fastest speed occurred.
"""

import unittest

class LugeTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]), "The luger's fastest speed was 35.07 m/s on segment 5.")

    def test2(self):
        self.assertEqual(get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284]), "The luger's fastest speed was 37.75 m/s on segment 2.")

    def test3(self):
        self.assertEqual(get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912]), "The luger's fastest speed was 38.49 m/s on segment 3.")

    def test4(self):
        self.assertEqual(get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840]), "The luger's fastest speed was 37.69 m/s on segment 1.")

    def test5(self):
        self.assertEqual(get_fastest_speed([8.204, 7.230, 9.673, 7.645, 6.508]), "The luger's fastest speed was 39.24 m/s on segment 4.")


def get_fastest_speed(times):

    segments = {
        1: 320,
        2: 280,
        3: 350,
        4: 300,
        5: 250
    }

    min_time = float('inf')
    final_index = 0

    for index, time in enumerate(times, start=1):
        if time < min_time:
            min_time = time
            final_index = index
        
    speed = round(segments[final_index] / min_time, 2)

    return f"The luger's fastest speed was {speed} m/s on segment {final_index}."

"""
This solution is close but it has certain issues

=>  In this apporach we are currently finding the segment with the minium time and then dividing distance
    by that time. That works only if the shortest time corresponds to the fastest speed, but because each segment
    has a different distance, the fastest speed isn't necessarily the one with the smallest time.

    For Example: Segment 2: 280 m in 20 s -> 14 m/s
                 Segment 3: 350 m in 30 s -> 11.67 m/s

                 Even though 20's is shorter than 30s, segment 2 is faster
                 because of the distance/ time ratio.

    So we can refine the solution as follows.
"""

def get_fastest_speed(times):
    segments = {
        1: 320,
        2: 280,
        3: 350,
        4: 300,
        5: 250
    }

    max_speed = 0
    final_index = 0

    for index, time in enumerate(times, start=1):
        speed = segments[index] / time
        if speed > max_speed:
            max_speed = speed
            final_index = index

    return f"The luger's fastest speed was {max_speed:.2f} m/s on segment {final_index}."


def get_fastest_speed(times):

    distances = [320, 280, 350, 300, 250]

    speeds = [distances[i]/ times[i] for i in range(5)]

    max_speed = max(speeds)
    segment = speeds.index(max_speed)  + 1

    return f"The luger's fastest speed was {max_speed:.2f} m/s on segment {segment}."

if __name__ == "__main__":
    # print(get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]))
    print(get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284]))
    unittest.main()

