class Items: 
    def __init__(self, name):
        self.name = name
        self.level = 1
    
    def item_Effect(self, player):
        pass

class Consumables(Items):
    def __init__(self, name):
        super().__init__(name)

class Potion(Consumables):
    def __init__(self, name, val, effectType):
        super().__init__(name)
        self.val = val
        self.effectType = effectType

    def apply_effect(self, player):
        if self.effectType == "mana":
            player.mana = min(player.max_mana, player.mana + self.val)
            print(f"\n{player.name} restored {self.val} mana!")
        elif self.effectType == "health":
            player.health = min(player.max_health, player.health + self.val)
            print(f"\n{player.name} restored {self.val} health!")

class manaPotionSmall(Potion):
    def __init__(self, name):
        super().__init__(name, 10, "mana")

class manaPotionBig(Potion):
    def __init__(self, name):
        super().__init__(name, 30, "mana")

class manaPotionLarge(Potion):
    def __init__(self, name):
        super().__init__(name, 50, "mana")

class healthPotionSmall(Potion):
    def __init__(self, name):
        super().__init__(name, 10, "health")

class healthPotionBig(Potion):
    def __init__(self, name):
        super().__init__(name, 30, "health")

class healthPotionLarge(Potion):
    def __init__(self, name):
        super().__init__(name, 50, "health")

class Orb(Consumables):
    def __init__(self, name, val, effectType):
        super().__init__(name)
        self.val = val
        self.effectType = effectType
    
    def apply_effect(self, player):
        if self.effectType == "mana":
            player.max_mana += self.val
            print(f"\n{player.name}'s max mana increased by {self.val}!")
        elif self.effectType == "health":
            player.max_health += self.val
            print(f"\n{player.name}'s max health increased by {self.val}!")

class manaOrb(Orb):
    def __init__(self, name):
        super().__init__(name, 20, "mana")

class healthOrb(Orb):
    def __init__(self, name):
        super().__init__(name, 20, "health")

class Weapons(Items):
    def __init__(self, name):
        super().__init__(name)

class Staff(Weapons):
    def __init__(self):
        super().__init__('staff')

class Sword(Weapons):
    def __init__(self):
        super().__init__('sword')

class Bow(Weapons):
    def __init__(self):
        super().__init__('bow')

class Tongue(Weapons):
    def __init__(self):
        super().__init__('tongue')

