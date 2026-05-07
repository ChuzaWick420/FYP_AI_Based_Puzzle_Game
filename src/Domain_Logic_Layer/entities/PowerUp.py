from src.Data_Layer.CellTypes import CellTypes


class PowerUp:
    def __init__(self):
        self.pos = (-1, -1)
        self.type = CellTypes.INVALID["value"]

    def setPosition(self, pos):
        self.pos = pos

    def getPosition(self):
        return self.pos

    def setType(self, power_type):
        self.type = power_type

    def getType(self):
        return self.type
