import unittest
from spaceJam import space_jam

class spaceJamTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(space_jam("freeCodeCamp"),"F  R  E  E  C  O  D  E  C  A  M  P")

    def test2(self):
        self.assertEqual(space_jam("   free   Code   Camp   "),"F  R  E  E  C  O  D  E  C  A  M  P")

    def test3(self):
        self.assertEqual(space_jam("Hello World?!"),"H  E  L  L  O  W  O  R  L  D  ?  !")

    def test4(self):
        self.assertEqual(space_jam("C@t$ & D0g$"),"C  @  T  $  &  D  0  G  $")

    def test5(self):
        self.assertEqual(space_jam("allyourbase"),"A  L  L  Y  O  U  R  B  A  S  E")


if __name__ == "__main__":
    unittest.main()