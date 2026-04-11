from prototype.Data_Layer.CellTypes import CellTypes
from prototype.Domain_Logic_Layer.entities.Entity import Entity


class Player(Entity):
    def __init__(self, map):
        super().__init__()
        self.map = map
        self.map_width = len(map)

        self.prev_x = self.x_coordinate
        self.prev_y = self.y_coordinate

    def update_grid(self):
        # Clear previous position
        self.map[self.prev_y][self.prev_x] = CellTypes.PATH.value

        # Set new position
        pos = self.get_position()
        self.map[pos[1]][pos[0]] = CellTypes.PLAYER.value

        # Update previous position
        self.prev_x, self.prev_y = pos
