class Belt:
    def __init__(self, property: str, ability: str = None, value: str):
        self.property = property
        if ability != None:
            self.ability = ability
        self.valueofStr = value