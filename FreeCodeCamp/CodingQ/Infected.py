"""
Infected
On November 2nd, 1988, the first major internet worm was released, infecting about 10% of computers connected to the internet after only a day.

In this challenge, you are given a number of days that have passed since an internet worm was released, and you need to determine how many computers are infected using the following rules:

On day 0, the first computer is infected.
Each subsequent day, the number of infected computers doubles.
Every 3rd day, a patch is applied after the virus spreads and reduces the number of infected computers by 20%. Round the number of patched computers up to the nearest whole number.
For example, on:

Day 0: 1 total computer is infected.
Day 1: 2 total computers are infected.
Day 2: 4 total computers are infected.
Day 3: 8 total computers are infected. Then, apply the patch: 8 infected * 20% = 1.6 patched. Round 1.6 up to 2. 8 computers infected - 2 patched = 6 total computers infected after day 3.
Return the number of total infected computers after the given amount of days have passed.
"""

import unittest,math

class InfectedTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(infected(1),2)
    
    def test2(self):
        self.assertEqual(infected(3),6)

    def test3(self):
        self.assertEqual(infected(8),152)

    def test4(self):
        self.assertEqual(infected(17),39808)

    def test5(self):
        self.assertEqual(infected(25),5217638)




def infected(days):
    infected = 1
    for day in range(1 , days+1):
        infected *= 2
        if day%3 == 0:
            patched = math.ceil(infected * 0.20)
            infected -= patched
        


    return infected

if __name__ == "__main__":
    print(infected(8))
    unittest.main()