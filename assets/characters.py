from items import Staff
from skills import Fireball

class Mage:
    def __init__(self):
        self.health = 100
        self.mana = 50
        self.armor = 10
        self.experience = 0
        self.level = 1
        self.items = Staff()
        self.skills = Fireball()

m = Mage()
print(m.skills)
print(m.items)