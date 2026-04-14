from prototype.Data_Layer.CellTypes import CellTypes
from prototype.Domain_Logic_Layer.entities.Entity import Entity


class Ai(Entity):
    def __init__(self):
        super().__init__()
        self.path = []
        self.number_of_steps = 0
        self.step_index = 0

    def init(self, path):
        self.path = path
        self.number_of_steps = len(self.path)

    def step(self):
        (self.prev_x, self.prev_y) = self.get_position()

        if self.step_index < self.number_of_steps:
            coordinates = self.path[self.step_index]
            self.step_index += 1
            (self.x_coordinate, self.y_coordinate) = (coordinates[1], coordinates[0])
