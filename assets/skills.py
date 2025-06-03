class Skills:
    def __init__(self, damage, name):
        self.damage = damage
        self.name = name
        self.level = 1

class Fireball(Skills):
    def __init__(self):
        super().__init__(10, 'fireball')

class Shoot(Skills):
    def __init__(self):
        super().__init__(10, 'shoot')

class Slash(Skills):
    def __init__(self):
        super().__init__(10, 'slash')

class Claw(Skills):
    def __init__(self,):
        super().__init__(5, 'claw')

class Lick(Skills):
    def __init__(self):
        super().__init__(20, 'lick')