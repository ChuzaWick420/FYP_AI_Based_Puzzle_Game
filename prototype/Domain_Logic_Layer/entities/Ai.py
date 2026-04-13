from prototype.Data_Layer.CellTypes import CellTypes
from prototype.Domain_Logic_Layer.entities.Entity import Entity


class Ai(Entity):
    def __init__(self, map, path):
        super().__init__()
        self.map = map
        self.path = path
        self.number_of_steps = len(self.path)
        self.step_index = 0
        self.prev_x = self.x_coordinate
        self.prev_y = self.y_coordinate

        # DEBUG:
        # print("Number of steps: ", self.number_of_steps)

    def step(self):
        pos = (self.prev_x, self.prev_y)
        if self.step_index < self.number_of_steps:
            coordinates = self.path[self.step_index]
            self.step_index += 1
            pos = (coordinates[1], coordinates[0])
        return pos

    def update_grid(self):
        # Clear previous position
        self.map[self.prev_y][self.prev_x] = CellTypes.PATH.value

        # Set new position
        pos = self.step()
        self.map[pos[1]][pos[0]] = CellTypes.AI.value

        # Update previous position
        self.prev_x, self.prev_y = pos
