import pygame

class TextElement:
    def __init__(self, txt, clr, pos):
        self.font_size = 32
        self.color = clr 
        self.string = txt
        self.position = pos

        self.font = pygame.font.Font(None, self.font_size)
        self.text = self.font.render(txt, True, clr)
        self.textRect = self.text.get_rect()
        self.textRect.center = pos

    def setText(self, txt):
        self.string = txt
        self.update()

    def setSize(self, size):
        self.font_size = size
        self.update()

    def setPosition(self, pos):
        self.position = pos
        self.update()

    def setColor(self, clr):
        self.color = clr
        self.update()

    def update(self):
        self.font = pygame.font.Font(None, self.font_size)
        self.text = self.font.render(self.string, True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.position

    def render(self, display):
        display.blit(self.text, self.textRect)
