class Items: 
    def __init__(self, name):
        self.name = name
        self.level = 1

class Consumables(Items):
    def __init__(self, name):
        super().__init__(name)

class Potion(Consumables):
    def __init__(self, name, val):
        super().__init__(name)
        self.val = val

class manaPotionSmall(Potion):
    def __init__(self, name):
        super().__init__(name, 10)

class manaPotionBig(Potion):
    def __init__(self, name):
        super().__init__(name, 30)

class manaPotionLarge(Potion):
    def __init__(self, name):
        super().__init__(name, 50)

class healthPotionSmall(Potion):
    def __init__(self, name):
        super().__init__(name, 10)

class healthPotionBig(Potion):
    def __init__(self, name):
        super().__init__(name, 30)

class healthPotionLarge(Potion):
    def __init__(self, name):
        super().__init__(name, 50)

class Orb(Consumables):
    def __init__(self, name, val):
        super().__init__(name)
        self.val = val

class manaOrb(Orb):
    def __init__(self, name):
        super().__init__(name, 20)

class healthOrb(Orb):
    def __init__(self, name):
        super().__init__(name, 20)

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

