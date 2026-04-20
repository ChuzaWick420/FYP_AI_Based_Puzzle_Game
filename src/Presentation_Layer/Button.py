import pygame
from src.Presentation_Layer.TextElement import TextElement

class Button:
    def __init__(self, text_str, pos):
        self.str = text_str
        self.id = self.str

        self.position = pos
        self.width = 250
        self.height = 0

        self.text_color = (255, 255, 255)
        self.border_color = (255, 255, 255)
        self.hover_color = (100, 100, 100)

        self.text = TextElement(self.str, self.text_color, self.position)

        self.text.setSize(28) # NOTE: Won't update unless setText is set
        self.text.setText(self.str)

        self.hoverFlag = False

        # NOTE: Border
        reference = self.text.textRect.copy()

        self.rect = pygame.Rect(0, 0, 0, 0)
        self.padding = 16
        self.thickness = 2
        self.border_radius = 8

        self.rect.width = self.width
        self.rect.height = reference.height + self.padding
        self.rect.center = reference.center

    def setPosition(self, pos):
        self.position = pos
        self.text.setPosition(pos)

    def isHovered(self):
        self.hoverFlag = False

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.hoverFlag = True

        return self.hoverFlag

    def render(self, display):
        if self.hoverFlag == False:
            pygame.draw.rect(display, self.border_color, self.rect, self.thickness, self.border_radius)
        else:
            pygame.draw.rect(display, self.hover_color, self.rect, self.thickness, self.border_radius)

        display.blit(self.text.text, self.text.textRect)
