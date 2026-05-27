class Blinder:
    def __init__(self):
        self.__size = 0
        self.position = (-1, -1)

    def setPosition(self, pos):
        self.position = pos

    def getPosition(self):
        return self.position

    def setSize(self, size):
        self.__size = size

    def getSize(self):
        return self.__size

    def overlaps(self, obj_coords):
        flag = False

        if self.position[0] <= obj_coords[0] <= self.__size and self.position[1] <= obj_coords[1] <= self.__size:
            flag = True

        return flag
