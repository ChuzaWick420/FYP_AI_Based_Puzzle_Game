from prototype.Domain_Logic_Layer.entities.Entity import Entity


class Ai(Entity):
    def __init__(self, map, path):
        super().__init__()
        self.map = map
        self.path = path
