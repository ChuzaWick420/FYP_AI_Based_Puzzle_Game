from src.Domain_Logic_Layer.entities.Entity import Entity


class Ai(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.__path = []
        self.__number_of_steps = 0
        self.__step_index = 0

    def reset(self):
        self.__step_index = 0

        pos = (0, 1)

        self.setPosition(pos)
        self.setPrevPosition(pos)


    def init(self, path):
        self.reset()
        self.__path = path
        self.__number_of_steps = len(self.__path)

    def step(self):
        pos = self.getPosition()
        self.setPrevPosition(pos)

        if self.__step_index < self.__number_of_steps:
            coordinates = self.__path[self.__step_index]
            new_pos = (coordinates[1], coordinates[0])
            self.setPosition(new_pos)

            self.__step_index += 1
