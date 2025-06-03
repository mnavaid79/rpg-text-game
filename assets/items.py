class Items: 
    def __init__(self, name):
        self.name = name
        self.level = 1

class Staff(Items):
    def __init__(self):
        super().__init__('staff')

class Sword(Items):
    def __init__(self):
        super().__init__('sword')

class Bow(Items):
    def __init__(self):
        super().__init__('bow')

class Tongue(Items):
    def __init__(self):
        super().__init__('tongue')

