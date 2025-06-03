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
        self.max_armor = armor
        self.experience = 0
        self.level = 1
        self.attribute = attribute
        self.items = items or {}
        self.skills = skills or {}
        self.xp_required = {1: 20, 2: 50, 3: 80, 4: 100}  # XP needed for each level
        self.max_level = 5


    def draw_health_bar(self):
        bar_length = 50

        # HEALTH: Scale based on max_health only (ensures consistent width)
        filled_health = round((self.health / self.max_health) * bar_length)

        # ARMOR: Overlay, scaled separately (armor shouldn't shrink health portion)
        filled_armor = round((self.armor / self.max_health) * bar_length) if self.armor > 0 else 0

        # Construct the combined bar
        armor_section = Fore.LIGHTBLACK_EX + "▒" * filled_armor  # Light gray for armor
        health_section = Fore.RED + "█" * (filled_health - filled_armor)  # Red for health
        empty_space = "-" * (bar_length - filled_health)  # Remaining empty space

        # Display bar with both armor and health overlayed correctly
        bar_display = f"[{armor_section}{health_section}{empty_space}]{Style.RESET_ALL}"

        print(f"{self.name} Health & Armor: {bar_display} {self.health}/{self.max_health} | {self.armor}/{self.max_armor}")


    def use_ability(self, selection, target):
        ability = list(self.skills)[int(selection) - 1]
        damage = self.skills[ability].damage

        if target.armor > 0:
            absorbed = min(target.armor, damage)
            target.armor -= absorbed
            damage -= absorbed

        target.health -= damage
        return target.draw_health_bar()
    

    def gain_experience(self, amount):
        if self.level < self.max_level:
            self.experience += amount
            while self.level < self.max_level and self.experience >= self.xp_required.get(self.level, float('inf')):
                self.level += 1
                print(f"{self.name} has leveled up! Now at level {self.level}.")
            if self.level == self.max_level:
                self.experience = self.xp_required[self.max_level]  # Cap XP at max level


    def defeat_enemy(self, enemy):
        if hasattr(enemy, 'give_experience'):
            self.gain_experience(enemy.give_experience)
            print(f"{self.name} defeated {enemy.name} and gained {enemy.give_experience} XP!")





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
        self.give_experience = 80

# Enemy classes
class Rat(Character):
    def __init__(self):
        super().__init__('Rat', health=30, mana=10, armor=0, attribute="Enemy",
                         skills={'claw': Claw()})
        self.give_experience = 10

class Ogre(Character):
    def __init__(self):
        super().__init__('Ogre', health=80, mana=40, armor=40, attribute="Enemy",
                         items={'sword': Sword()}, skills={'slash': Slash()})
        self.give_experience = 20