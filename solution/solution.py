import random
from characters.character import ALL_CHARACTERS
from weapons.weapon       import ALL_WEAPONS
from mansion.mansion      import Mansion

def random_solution():
    mansion = Mansion()
    return {
        "character": random.choice(ALL_CHARACTERS).name,
        "weapon":    random.choice(ALL_WEAPONS).name,
        "room":      random.choice(mansion.all_rooms())
    }

if __name__ == "__main__":
    sol = random_solution()
    print(f"🔍 Solution (hidden in real game): {sol}")
