import unittest
from solution.solution import random_solution
from characters.character import ALL_CHARACTERS
from weapons.weapon       import ALL_WEAPONS
from mansion.mansion      import Mansion

class TestCluedoSetup(unittest.TestCase):
    def test_solution_keys(self):
        sol = random_solution()
        self.assertIn("character", sol)
        self.assertIn("weapon", sol)
        self.assertIn("room", sol)

    def test_solution_values(self):
        sol = random_solution()
        valid_chars = [c.name for c in ALL_CHARACTERS]
        valid_weaps = [w.name for w in ALL_WEAPONS]
        valid_rooms = Mansion().all_rooms()

        self.assertIn(sol["character"], valid_chars)
        self.assertIn(sol["weapon"], valid_weaps)
        self.assertIn(sol["room"], valid_rooms)

if __name__ == "__main__":
    unittest.main()
