"""
2026 Winter Games Day 2: Snowboarding
Given a snowboarder's starting stance and a rotation in degrees, determine their landing stance.

A snowboarder's stance is either "Regular" or "Goofy".
Trick rotations are multiples of 90 degrees. Positive indicates clockwise rotation, and negative indicate counter-clockwise rotation.
The landing stance flips every 180 degrees of rotation.
For example, given "Regular" and 90, return "Regular". Given "Regular" and 180 degrees, return "Goofy".
"""

import unittest

class SnowboardTest(unittest.TestCase):

    def test1(self):
        # 180° rotation flips stance
        self.assertEqual(get_landing_stance("Regular", 180), "Goofy")

    def test2(self):
        # 2340° = 180° + 6 full spins (6*360 = 2160)
        # So effectively 180° → flip
        self.assertEqual(get_landing_stance("Regular", 2340), "Goofy")

    def test3(self):
        # 2160° = 6 full spins → stance stays the same
        self.assertEqual(get_landing_stance("Goofy", 2160), "Goofy")

    def test4(self):
        # -540° = -3*180° → odd multiple of 180 → flip
        self.assertEqual(get_landing_stance("Goofy", -540), "Regular")


def get_landing_stance(start_stance, rotation):
    """
    Determine the landing stance after a rotation.

    rotation = ((rotation % 360) + 360) % 360
    ------------------------------------------------
    Why this normalization?
    - rotation % 360 reduces any rotation to within -359..359
      Example: 450 % 360 = 90, -450 % 360 = -90
    - Adding +360 ensures negative values become positive
      Example: -90 % 360 = -90 → +360 = 270
    - Final % 360 ensures result is always in range 0..359
      Example: -270 → ((-270 % 360) + 360) % 360 = 90

    So this line guarantees rotation is always between 0 and 359,
    making it easy to handle both clockwise and counter-clockwise spins.
    """

    rotation = ((rotation % 360) + 360) % 360

    # Count how many 180° flips are in the rotation
    flips = (rotation // 180) % 2

    # If flips is odd → stance flips
    if flips == 1:
        return "Goofy" if start_stance == "Regular" else "Regular"
    else:
        # If flips is even → stance stays the same
        return start_stance



"""
Key Commented Explanation
- rotation % 360 → reduces rotation to within -359..359.
- + 360 → shifts negatives into positive range.
- % 360 → ensures final result is between 0..359.
So:
- -270 → normalized to 90.
- 450 → normalized to 90.
- -540 → normalized to 180.
This way, both clockwise and counter‑clockwise rotations are handled consistently.




"""
if __name__ == "__main__":
    unittest.main()