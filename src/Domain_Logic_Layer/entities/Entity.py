class Entity:
    def __init__(self):
        self._x_coordinate = 0
        self._y_coordinate = 1

        self._prev_x = self._x_coordinate
        self._prev_y = self._y_coordinate

    def getPosition(self):
        return (self._x_coordinate, self._y_coordinate)

    def getPrevPosition(self):
        return (self._prev_x, self._prev_y)

    def setPosition(self, pos):
        (self._x_coordinate, self._y_coordinate) = pos

    def setPrevPosition(self, pos):
        (self._prev_x, self._prev_y) = pos
