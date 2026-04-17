import pygame
from src.Presentation_Layer.TextElement import TextElement
from src.Presentation_Layer.Border import Border

class Button:
    def __init__(self, name, pos):
        self.name = name
        color = (255, 255, 255)
        self.text = TextElement(name, color, pos)
        self.position = pos
        self.text.setSize(28) # NOTE: Won't update unless setText is set
        self.text.setText(name)

        self.border = Border(self.text.textRect.copy())

    def setPosition(self, pos):
        self.position = pos
        self.text.setPosition(pos)

    def isClicked(self):
        flag = False

        mouse_pos = pygame.mouse.get_pos()

        if self.border.rect.collidepoint(mouse_pos):
            flag = True

        return flag

    def render(self, display):
        self.border.render(display)
        display.blit(self.text.text, self.text.textRect)
