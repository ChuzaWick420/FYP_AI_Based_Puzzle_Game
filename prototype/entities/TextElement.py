import pygame

class TextElement:
    def __init__(self, txt, clr, pos):
        self.color = clr 
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render(txt, True, clr)
        self.textRect = self.text.get_rect()
        self.textRect.center = pos
        self.position = pos

    def updateText(self, string):
        self.text = self.font.render(string, True, self.color)
