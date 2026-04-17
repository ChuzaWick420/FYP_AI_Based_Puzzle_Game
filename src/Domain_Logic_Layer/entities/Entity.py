class Entity:
    def __init__(self):
        self.x_coordinate = 0
        self.y_coordinate = 1

        self.prev_x = self.x_coordinate
        self.prev_y = self.y_coordinate

    def get_position(self):
        return (self.x_coordinate, self.y_coordinate)
