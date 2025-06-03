from .items import *
from .skills import *
from colorama import Fore, Style

class Character:
    def __init__(self, name, health, mana, armor, attribute, items=None, skills=None):
        self.name = name
        self.health = health
        self.max_health = health
        self.mana = mana
        self.armor = armor
        self.experience = 0
        self.level = 1
        self.attribute = attribute
        self.items = items or {}
        self.skills = skills or {}
    
    def draw_health_bar(self):
        bar_length = 60
        filled_length = round((self.health / self.max_health) * bar_length)
        empty_length = bar_length - filled_length

        health_bar = "█" * filled_length + "-" * empty_length

        # Color coding based on remaining health
        if self.health > self.max_health * 0.6:
            color = Fore.GREEN
        elif self.health > self.max_health * 0.3:
            color = Fore.YELLOW
        else:
            color = Fore.RED

        print(f"{self.name} Health: {color}[{health_bar}] {self.health}/{self.max_health}{Style.RESET_ALL}")

    def use_ability(self, ability, target):
        damage = self.skills[ability].damage
        target.health -= damage
        return target.draw_health_bar()

# Hero classes
class Mage(Character):
    def __init__(self):
        super().__init__('Mage', health=100, mana=100, armor=10, attribute="Hero",
                         items={'staff': Staff()}, skills={'fireball': Fireball(), 'slash': Slash()})

class Knight(Character):
    def __init__(self):
        super().__init__('Knight', health=100, mana=20, armor=100, attribute="Hero",
                         items={'sword': Sword()}, skills={'slash': Slash()})

class Ranger(Character):
    def __init__(self):
        super().__init__('Ranger', health=100, mana=50, armor=50, attribute="Hero",
                         items={'bow': Bow()}, skills={'shoot': Shoot()})

# Boss class
class MODOK(Character):
    def __init__(self):
        super().__init__('Modok', health=1000, mana=100, armor=100, attribute="Boss",
                         items={'tongue': Tongue()}, skills={'lick': Lick()})

# Enemy classes
class Rat(Character):
    def __init__(self):
        super().__init__('Rat', health=30, mana=10, armor=0, attribute="Enemy",
                         skills={'claw': Claw()})

class Ogre(Character):
    def __init__(self):
        super().__init__('Ogre', health=80, mana=40, armor=40, attribute="Enemy",
                         items={'sword': Sword()}, skills={'slash': Slash()})