import pygame
from src.Data_Layer.ButtonType import ButtonType
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
        self.activeFlag = False
        self.useIcon = False

        self.btn_type = -1

        # NOTE: Border

        self.rect = pygame.Rect(0, 0, 0, 0)
        self.padding = 16
        self.thickness = 2
        self.border_radius = 8

    def setType(self, btn_type):
        self.btn_type = btn_type

        reference = pygame.Rect(0, 0, 0, 0)

        if (self.btn_type == ButtonType.TEXTUAL):
            self.text = TextElement(self.str, self.text_color, self.position)
            reference = self.text.textRect.copy()
            self.rect.width = self.width

        else:
            reference = self.icon.get_rect()
            reference.center = self.position
            self.rect.width = reference.width + self.padding

        self.rect.height = reference.height + self.padding
        self.rect.center = reference.center

    def loadIcon(self, path):
        image = pygame.image.load(path)
        self.icon = pygame.transform.scale(image, (32, 32))
        self.useIcon = True
        self.setType(ButtonType.VISUAL)

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

        if (self.useIcon):
            display.blit(self.icon, (self.position[0] - 16, self.position[1] - 16))
        else:
            display.blit(self.text.text, self.text.textRect)
