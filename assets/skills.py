class Skills:
    def __init__(self, damage, name, mana):
        self.damage = damage
        self.name = name
        self.level = 1
        self.mana = mana

class Punch(Skills):
    def __init__(self):
        super().__init__(5, 'punch', 0)

class Fireball(Skills):
    def __init__(self):
        super().__init__(10, 'fireball', 10) 

class Shoot(Skills):
    def __init__(self):
        super().__init__(10, 'shoot', 10)

class Slash(Skills):
    def __init__(self):
        super().__init__(10, 'slash', 10)

class Claw(Skills):
    def __init__(self,):
        super().__init__(5, 'claw', 5)

class Lick(Skills):
    def __init__(self):
        super().__init__(20, 'lick', 30)