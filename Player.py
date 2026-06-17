from Entity import Entity


class Player(Entity):
    def __init__(self, name:str, position:tuple):
        super().__init__(name, position,)
        self.layer = 4



