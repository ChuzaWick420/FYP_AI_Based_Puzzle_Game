import pygame

class Button:
    def __init__(self, name, pos):
        self.name = name
        color = (255, 100, 100)
        font = pygame.font.Font(None, 32)
        self.text = font.render(name, True, color)
        self.textRect = self.text.get_rect()
        self.position = pos
        self.textRect.center = self.position

    def updatePosition(self, pos):
        self.position = pos
        self.textRect.center = self.position
