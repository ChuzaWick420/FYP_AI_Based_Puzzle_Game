import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, color, dimensions, position):
        super().__init__()

        self.__width = 0
        self.__height = 0
        self.__position = (0, 0)

        self.setDimensions(dimensions)
        self.setPosition(position)

        self.image = pygame.Surface([self.__width, self.__height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = self.__position[0]
        self.rect.y = self.__position[1]

    def setPosition(self, position):
        self.__position = position

    def setDimensions(self, dimensions):
        self.__width = dimensions[0]
        self.__height = dimensions[1]
