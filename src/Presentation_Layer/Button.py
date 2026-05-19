import pygame
from src.Data_Layer.ButtonType import ButtonType
from src.Data_Layer.Colors import Colors
from src.Presentation_Layer.TextElement import TextElement

class Button:
    def __init__(self, text_str, input, pos = (0, 0)):
        self.__str = text_str
        self.__input = input

        self.__position = pos
        self.__width = 250
        self.__font_size = 28

        self.text = TextElement(self.__str, Colors.TEXT, self.__position)

        self.text.setSize(self.__font_size)

        self.__hover_flag = False
        self.__active_flag = False
        self.__use_icon = False

        self.__btn_type = -1

        # NOTE: Border

        self.__rect = pygame.Rect(0, 0, 0, 0)
        self.__padding = 16
        self.__thickness = 2
        self.__border_radius = 8

    def setInput(self, input):
        self.__input = input

    def getInput(self):
        return self.__input

    def setType(self, btn_type):
        self.__btn_type = btn_type

        reference = pygame.Rect(0, 0, 0, 0)

        if (self.__btn_type == ButtonType.TEXTUAL):
            reference = self.text.getRect()
            self.__rect.width = self.__width

        else:
            reference = self.icon.get_rect()
            reference.center = self.__position
            self.__rect.width = reference.width + self.__padding

        self.__rect.height = reference.height + self.__padding
        self.__rect.center = reference.center

    def loadIcon(self, path):
        image = pygame.image.load(path)
        self.icon = pygame.transform.scale(image, (32, 32))
        self.__use_icon = True
        self.setType(ButtonType.VISUAL)

    def setPosition(self, pos):
        self.__position = pos
        self.text.setPosition(pos)
        self.setType(self.__btn_type)

    def isHovered(self):
        self.__hover_flag = False

        mouse_pos = pygame.mouse.get_pos()

        if self.__rect.collidepoint(mouse_pos):
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
            pygame.draw.rect(display, Colors.BORDER, self.__rect, self.__thickness, self.__border_radius)
            self.text.setColor(Colors.TEXT)
        else:
            pygame.draw.rect(display, Colors.HOVER, self.__rect, self.__thickness, self.__border_radius)
            self.text.setColor(Colors.HOVER)

        if (self.__use_icon):
            display.blit(self.icon, (self.__position[0] - 16, self.__position[1] - 16))
        else:
            self.text.render(display)
