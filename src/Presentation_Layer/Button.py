import pygame
from src.Data_Layer.ButtonType import ButtonType
from src.Presentation_Layer.TextElement import TextElement

class Button:
    def __init__(self, text_str, input, pos):
        self.str = text_str
        self.input = input

        self.position = pos
        self.width = 250
        self.height = 0
        self.font_size = 28

        self.text_color = (40, 90, 72)
        self.border_color = (40, 90, 72)
        self.hover_color = (176, 228, 204)

        self.text = TextElement(self.str, self.text_color, self.position)

        self.text.setSize(self.font_size)

        self.__hover_flag = False
        self.__active_flag = False
        self.__use_icon = False

        self.btn_type = -1

        # NOTE: Border

        self.rect = pygame.Rect(0, 0, 0, 0)
        self.padding = 16
        self.thickness = 2
        self.border_radius = 8

    def setInput(self, input):
        self.input = input

    def getInput(self):
        return self.input

    def setType(self, btn_type):
        self.btn_type = btn_type

        reference = pygame.Rect(0, 0, 0, 0)

        if (self.btn_type == ButtonType.TEXTUAL):
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
        self.__use_icon = True
        self.setType(ButtonType.VISUAL)

    def setPosition(self, pos):
        self.position = pos
        self.text.setPosition(pos)

    def isHovered(self):
        self.__hover_flag = False

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.__hover_flag = True

        return self.__hover_flag

    def isActive(self):
        return self.__active_flag

    def setActiveFlag(self, flag):
        self.__active_flag = flag

    def setHoverFlag(self, flag):
        self.__hover_flag = flag

    def render(self, display):
        if self.__hover_flag == False:
            pygame.draw.rect(display, self.border_color, self.rect, self.thickness, self.border_radius)
            self.text.setColor(self.text_color)
        else:
            pygame.draw.rect(display, self.hover_color, self.rect, self.thickness, self.border_radius)
            self.text.setColor(self.hover_color)

        if (self.__use_icon):
            display.blit(self.icon, (self.position[0] - 16, self.position[1] - 16))
        else:
            self.text.render(display)
