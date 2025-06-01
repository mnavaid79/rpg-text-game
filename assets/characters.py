from items import Staff
from items import Sword
from items import Bow
from items import Tongue
from skills import Fireball
from skills import Slash
from skills import Shoot
from skills import Lick


class Mage:
    def __init__(self):
        self.health = 100
        self.mana = 100
        self.armor = 10
        self.experience = 0
        self.level = 1
        self.attribute = "Hero"
        self.items = Staff()
        self.skills = Fireball()

class Knight:
    def __init__(self):
        self.health = 100
        self.mana = 20
        self.armor = 100
        self.experience = 0
        self.level = 1
        self.attribute = "Hero"
        self.items = Sword()
        self.skills = Slash()

class Ranger:
    def __init__(self):
        self.health = 100
        self.mana = 50
        self.armor = 50
        self.experience = 0
        self.level = 1
        self.attribute = "Hero"
        self.items = Bow()
        self.skills = Shoot()

class MODOK:
    def __init__(self):
        self.health = 1000
        self.mana = 100
        self.armor = 100
        self.experience = 0
        self.level = 1
        self.attribute = "Boss"
        self.items = Tongue()
        self.skills = Lick()

m = Mage()
print(m.skills)
print(m.items)