from src.Domain_Logic_Layer.entities.Entity import Entity


class Ai(Entity):
    def __init__(self):
        super().__init__()
        self.__path = []
        self.__number_of_steps = 0
        self.__step_index = 0

    def reset(self):
        self.__step_index = 0

        self.x_coordinate = 0
        self.y_coordinate = 1

        self.prev_x = self.x_coordinate
        self.prev_y = self.y_coordinate


    def init(self, path):
        self.reset()
        self.__path = path
        self.__number_of_steps = len(self.__path)

    def step(self):
        (self.prev_x, self.prev_y) = self.get_position()

        if self.__step_index < self.__number_of_steps:
            coordinates = self.__path[self.__step_index]
            self.__step_index += 1
            (self.x_coordinate, self.y_coordinate) = (coordinates[1], coordinates[0])
