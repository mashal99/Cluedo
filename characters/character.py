class Character:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

# Predefined characters
Miss_Scarlett   = Character("Miss Scarlett",   "Study")
Colonel_Mustard = Character("Colonel Mustard", "Kitchen")
Mrs_White       = Character("Mrs. White",      "Hall")
Reverend_Green  = Character("Reverend Green",  "Library")
Mrs_Peacock     = Character("Mrs. Peacock",    "Lounge")
Professor_Plum  = Character("Professor Plum",  "Ballroom")

ALL_CHARACTERS = [
    Miss_Scarlett, Colonel_Mustard, Mrs_White,
    Reverend_Green, Mrs_Peacock, Professor_Plum
]