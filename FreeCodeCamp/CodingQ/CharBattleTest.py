import unittest
from CharBattle import battle

class TestBattleFunction(unittest.TestCase):
    def test_we_lost(self):
        self.assertEqual(battle("Hello","World"), "We lost")
    
    def test_we_won_1(self):
        self.assertEqual(battle("pizza", "salad"), "We won")

    def test_we_won_2(self):
        self.assertEqual(battle("C@T5", "D0G$"), "We won")

    def test_opponent_retreated(self):
        self.assertEqual(battle("kn!ght", "orc"), "Opponent retreated")

    def test_we_retreated(self):
        self.assertEqual(battle("PC", "Mac"), "We retreated")

    def test_tie_1(self):
        self.assertEqual(battle("Wizards", "Dragons"), "It was a tie")

    def test_tie_2(self):
        self.assertEqual(battle("Mr. Smith", "Dr. Jones"), "It was a tie")

if __name__ == "__main__":
    unittest.main()
