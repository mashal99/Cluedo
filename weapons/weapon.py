class Weapon:
    def __init__(self, name):
        self.name = name

# Predefined weapons
Candlestick = Weapon("Candlestick")
Revolver    = Weapon("Revolver")
Rope        = Weapon("Rope")
Lead_Pipe   = Weapon("Lead Pipe")
Knife       = Weapon("Knife")
Wrench      = Weapon("Wrench")

ALL_WEAPONS = [
    Candlestick, Revolver, Rope,
    Lead_Pipe, Knife, Wrench
]
