from src.Data_Layer.CellTypes import CellTypes


class PowerUp:
    def __init__(self):
        self.__pos = (-1, -1)
        self.__type = CellTypes.INVALID["value"]

    def setPosition(self, pos):
        self.__pos = pos

    def getPosition(self):
        return self.__pos

    def setType(self, power_type):
        self.__type = power_type

    def getType(self):
        return self.__type
