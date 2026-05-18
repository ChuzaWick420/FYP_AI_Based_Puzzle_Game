import pygame

class TextElement:
    def __init__(self, txt, clr, pos):
        self.color = clr 
        self.string = txt
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render(txt, True, clr)
        self.textRect = self.text.get_rect()
        self.textRect.center = pos
        self.position = pos

    def setText(self, string):
        self.text = self.font.render(string, True, self.color)
        self.setPosition(self.position)

    def setSize(self, size):
        self.font = pygame.font.Font(None, size)
        self.setPosition(self.position)

    def setPosition(self, pos):
        self.textRect = self.text.get_rect()
        self.position = pos
        self.textRect.center = pos

    def setColor(self, clr):
        self.color = clr
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render(self.string, True, clr)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.position
