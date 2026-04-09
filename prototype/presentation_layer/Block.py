import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, color, dimensions, position):
        super().__init__()

        width = dimensions[0]
        height = dimensions[1]

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = position[0] * width
        self.rect.y = position[1] * height
