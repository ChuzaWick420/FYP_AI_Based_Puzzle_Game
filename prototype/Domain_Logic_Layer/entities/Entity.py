class Entity:
    def __init__(self):
        self.x_coordinate = 0
        self.y_coordinate = 1

        self.map = []
        self.map_width = 0

    def move_up(self):
        if self.y_coordinate > 0 and self.map[self.y_coordinate - 1][self.x_coordinate] != 0:
            self.y_coordinate -= 1
            self.update_grid()

    def move_down(self):
        if self.y_coordinate < self.map_width - 1 and self.map[self.y_coordinate + 1][self.x_coordinate] != 0:
            self.y_coordinate += 1
            self.update_grid()

    def move_left(self):
        if self.x_coordinate > 0 and self.map[self.y_coordinate][self.x_coordinate - 1] != 0:
            self.x_coordinate -= 1
            self.update_grid()

    def move_right(self):
        if self.x_coordinate < self.map_width - 1 and self.map[self.y_coordinate][self.x_coordinate + 1] != 0:
            self.x_coordinate += 1
            self.update_grid()

    def get_position(self):
        return (self.x_coordinate, self.y_coordinate)

    def update_grid(self):
        pass
