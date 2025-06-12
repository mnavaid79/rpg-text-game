from .items import *
from .skills import *
from colorama import Fore, Style

class Entity:
    def __init__(self, name, attribute, health, mana, armor, items=None, skills=None):
        self.name = name
        self.attribute = attribute
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.armor = armor
        self.max_armor = armor
        self.items = items or {}
        self.skills = skills or {}

    def draw_health_bar(self):
        bar_length = 50
        filled_health = round((self.health / self.max_health) * bar_length)
        filled_armor = round((self.armor / self.max_health) * bar_length) if self.armor > 0 else 0
        armor_section = Fore.LIGHTBLACK_EX + "▒" * filled_armor
        health_section = Fore.RED + "█" * (filled_health - filled_armor)
        empty_space = "-" * (bar_length - filled_health)
        bar_display = f"[{armor_section}{health_section}{empty_space}]{Style.RESET_ALL}"
        print(f"{self.name} Health & Armor: {bar_display} {self.health}/{self.max_health} | {self.armor}/{self.max_armor}")

    def draw_mana_bar(self):
        bar_length = 50
        filled_mana = round((self.mana / self.max_mana) * bar_length)
        mana_section = Fore.LIGHTBLUE_EX + "█" * filled_mana
        empty_space = "-" * (bar_length - filled_mana)
        bar_display2 = f"[{mana_section}{empty_space}]{Style.RESET_ALL}"
        print(f"{self.name} Mana remaining: {bar_display2} {self.mana}/{self.max_mana}")
    
    def use_ability(self, selection, target):
        ability = list(self.skills)[int(selection) - 1]
        damage = self.skills[ability].damage
        mana_cost = self.skills[ability].mana
        if self.mana < mana_cost:
            return print("Insufficent mana for choosen skill, pick another ability!!")
        else:
            self.mana -= mana_cost
        if target.armor > 0:
            absorbed = min(target.armor, damage)
            target.armor -= absorbed
            damage -= absorbed

        target.health -= damage
        target.draw_health_bar()

        if self.attribute == 'hero':
            self.draw_mana_bar()


class Hero(Entity):
    def __init__(self, name, attribute, health, mana, armor, items=None, skills=None):
        super().__init__(name, attribute, health, mana, armor, items, skills)
        self.experience = 0
        self.level = 1
        self.xp_required = {1: 20, 2: 50, 3: 80, 4: 100}
        self.max_level = 5

    def gain_experience(self, amount):
        if self.level < self.max_level:
            self.experience += amount
            while self.level < self.max_level and self.experience >= self.xp_required.get(self.level, float('inf')):
                self.level += 1
                print(f"{self.name} has leveled up! Now at level {self.level}.")
            if self.level == self.max_level:
                self.experience = self.xp_required[self.max_level]

    def defeat_enemy(self, enemy):
        if hasattr(enemy, 'give_experience'):
            self.gain_experience(enemy.give_experience)
            print(f"{self.name} defeated {enemy.name} and gained {enemy.give_experience} XP!")
    
def consumeItemMana(self, item_name):
    item = self.items.get(item_name)
    if item:
        if isinstance(item, Orb):
            self.max_mana += item.val
            print(f"{self.name} used {item.name} and increased max mana by {item.val}!")
        else:
            self.mana = min(self.max_mana, self.mana + item.val)
            print(f"{self.name} used {item.name} and restored {item.val} mana!")

        del self.items[item_name]
        self.draw_mana_bar()
    else:
        print("Item not found or already used.")


class Enemy(Entity):
    def __init__(self, name, attribute, health, mana, armor, give_experience, items=None, skills=None):
        super().__init__(name, attribute, health, mana, armor, items, skills)
        self.give_experience = give_experience

# Hero classes
class Mage(Hero):
    def __init__(self):
        super().__init__('Mage', 'hero', health=100, mana=200, armor=100,
                         items={'staff': Staff()}, skills={'punch': Punch(), 'fireball': Fireball()})

class Knight(Hero):
    def __init__(self):
        super().__init__('Knight', 'hero', health=100, mana=20, armor=100,
                         items={'sword': Sword()}, skills={'punch': Punch(), 'slash': Slash()})

class Ranger(Hero):
    def __init__(self):
        super().__init__('Ranger', 'hero',  health=100, mana=50, armor=50,
                         items={'bow': Bow()}, skills={'punch': Punch(), 'shoot': Shoot()})

# Boss class
class MODOK(Enemy):
    def __init__(self, name):
        super().__init__('Modok', 'enemy',  health=1000, mana=1000, armor=100, give_experience=80,
                         items={'tongue': Tongue()}, skills={'lick': Lick()})

# Enemy classes
class Rat(Enemy):
    def __init__(self, name):
        super().__init__(name, 'enemy',  health=10, mana=1000, armor=10, give_experience=10,
                         skills={'claw': Claw()})

class Ogre(Enemy):
    def __init__(self, name):
        super().__init__(name, 'enemy',  health=10, mana=1000, armor=10, give_experience=20,
                         items={'sword': Sword()}, skills={'slash': Slash()})