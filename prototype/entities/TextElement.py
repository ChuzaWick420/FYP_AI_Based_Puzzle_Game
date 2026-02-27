import pygame

class TextElement:
    def __init__(self, txt, color, pos):
        font = pygame.font.Font(None, 32)
        self.text = font.render(txt, True, color)
        self.textRect = self.text.get_rect()
        self.textRect.center = pos
        self.position = pos
