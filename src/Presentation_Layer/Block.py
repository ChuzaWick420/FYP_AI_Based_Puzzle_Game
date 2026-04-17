import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, color, dimensions, position):
        super().__init__()

        self.width = 0
        self.height = 0
        self.position = (0, 0)
        self.color = (0, 0, 0)

        self.setDimensions(dimensions)
        self.setColor(color)
        self.setPosition(position)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def setPosition(self, position):
        self.position = position

    def setDimensions(self, dimensions):
        self.width = dimensions[0]
        self.height = dimensions[1]

    def setColor(self, color):
        self.color = color
