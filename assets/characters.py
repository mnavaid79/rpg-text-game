from .items import *
from .skills import *


class Mage:
    def __init__(self):
        self.name = 'Mage'
        self.health = 100
        self.mana = 100
        self.armor = 10
        self.experience = 0
        self.level = 1
        self.attribute = "Hero"
        self.items = {'staff': Staff()}
        self.skills = {'fireball': Fireball(), 'slash': Slash()}

class Knight:
    def __init__(self):
        self.name = 'Knight'
        self.health = 100
        self.mana = 20
        self.armor = 100
        self.experience = 0
        self.level = 1
        self.attribute = "Hero"
        self.items = {'sword': Sword()}
        self.skills = {'slash': Slash()}

class Ranger:
    def __init__(self):
        self.name = 'Ranger'
        self.health = 100
        self.mana = 50
        self.armor = 50
        self.experience = 0
        self.level = 1
        self.attribute = "Hero"
        self.items = [Bow()]
        self.skills = [Shoot()]

class MODOK:
    def __init__(self):
        self.name = 'Modok'
        self.health = 1000
        self.mana = 100
        self.armor = 100
        self.experience = 0
        self.level = 1
        self.attribute = "Boss"
        self.items = [Tongue()]
        self.skills = [Lick()]

class Rat:
    def __init__(self):
        self.name = 'Rat'
        self.health = 30
        self.mana = 10
        self.armor = 0
        self.experience = 0
        self.level = 1
        self.attribute = "Enemy"
        self.skills = [Claw()]

class Ogre:
    def __init__(self):
        self.name = 'Ogre'
        self.health = 80
        self.mana = 40
        self.armor = 40
        self.experience = 0
        self.level = 1
        self.attribute = "Enemy"
        self.items = [Sword()]
        self.skills = [Slash()]
