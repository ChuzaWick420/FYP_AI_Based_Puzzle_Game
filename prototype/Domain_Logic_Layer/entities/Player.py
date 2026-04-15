from prototype.Data_Layer.CellTypes import CellTypes
from prototype.Domain_Logic_Layer.entities.Entity import Entity


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.map = []
        self.map_width = 0

    def reset(self):
        self.x_coordinate = 0
        self.y_coordinate = 1

        self.prev_x = self.x_coordinate
        self.prev_y = self.y_coordinate

    def init(self, map):
        self.reset()
        self.map = map
        self.map_width = len(map)

    def move_up(self):

        next_not_wall = self.map[self.y_coordinate - 1][self.x_coordinate] != CellTypes.WALL["value"]
        within_bounds = self.y_coordinate > 0

        if within_bounds and next_not_wall:
            (self.prev_x, self.prev_y) = self.get_position()
            self.y_coordinate -= 1

    def move_down(self):

        next_not_wall = self.map[self.y_coordinate + 1][self.x_coordinate] != CellTypes.WALL["value"]
        within_bounds = self.y_coordinate < self.map_width - 1

        if within_bounds and next_not_wall:
            (self.prev_x, self.prev_y) = self.get_position()
            self.y_coordinate += 1

    def move_left(self):

        next_not_wall = self.map[self.y_coordinate][self.x_coordinate - 1] != CellTypes.WALL["value"]
        within_bounds = self.x_coordinate > 0 

        if within_bounds and next_not_wall:
            (self.prev_x, self.prev_y) = self.get_position()
            self.x_coordinate -= 1

    def move_right(self):

        next_not_wall = self.map[self.y_coordinate][self.x_coordinate + 1] != CellTypes.WALL["value"]
        within_bounds = self.x_coordinate < self.map_width - 1 

        if within_bounds and next_not_wall:
            (self.prev_x, self.prev_y) = self.get_position()
            self.x_coordinate += 1
