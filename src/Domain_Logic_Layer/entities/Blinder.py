class Blinder:
    def __init__(self):
        self.size = 0
        self.position = (-1, -1)

    def setPosition(self, pos):
        self.position = pos
        self.update()

    def update(self):
        # NOTE: Following are potentially unnecessary
        self.coords_start = (self.position[0], self.position[1])
        self.coords_end = (self.coords_start[0] + self.size, self.coords_start[1] + self.size)

    def getPosition(self):
        return self.position

    def overlaps(self, obj_coords):
        flag = False

        if self.position[0] <= obj_coords[0] <= self.size and self.position[1] <= obj_coords[1] <= self.size:
            flag = True

        return flag
