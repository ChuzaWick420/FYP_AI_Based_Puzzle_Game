from src.Data_Layer.CellTypes import CellTypes
from src.Domain_Logic_Layer.entities.Entity import Entity


class Player(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.map = []
        self.map_width = 0

    def reset(self):
        pos = (0, 1)

        self.setPosition(pos)
        self.setPrevPosition(pos)

    def init(self, map):
        self.reset()
        self.map = map
        self.map_width = len(map)

    def move_up(self):

        next_not_wall = self.map[self._y_coordinate - 1][self._x_coordinate] != CellTypes.WALL["value"]
        within_bounds = self._y_coordinate > 0

        if within_bounds and next_not_wall:
            old_pos = self.getPosition()
            self.setPrevPosition(old_pos)
            self._y_coordinate -= 1

    def move_down(self):

        next_not_wall = self.map[self._y_coordinate + 1][self._x_coordinate] != CellTypes.WALL["value"]
        within_bounds = self._y_coordinate < self.map_width - 1

        if within_bounds and next_not_wall:
            old_pos = self.getPosition()
            self.setPrevPosition(old_pos)
            self._y_coordinate += 1

    def move_left(self):

        next_not_wall = self.map[self._y_coordinate][self._x_coordinate - 1] != CellTypes.WALL["value"]
        within_bounds = self._x_coordinate > 0 

        if within_bounds and next_not_wall:
            old_pos = self.getPosition()
            self.setPrevPosition(old_pos)
            self._x_coordinate -= 1

    def move_right(self):

        next_not_wall = self.map[self._y_coordinate][self._x_coordinate + 1] != CellTypes.WALL["value"]
        within_bounds = self._x_coordinate < self.map_width - 1 

        if within_bounds and next_not_wall:
            old_pos = self.getPosition()
            self.setPrevPosition(old_pos)
            self._x_coordinate += 1
