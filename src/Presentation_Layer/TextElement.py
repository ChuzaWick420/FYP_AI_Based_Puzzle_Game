import pygame

class TextElement:
    def __init__(self, txt, clr, pos):
        self.__font_size = 32
        self.__color = clr 
        self.__string = txt
        self.__position = pos

        self.__font = pygame.font.Font(None, self.__font_size)
        self.__text = self.__font.render(txt, True, clr)
        self.__textRect = self.__text.get_rect()
        self.__textRect.center = pos

    def setText(self, txt):
        self.__string = txt
        self.__update()

    def setSize(self, size):
        self.__font_size = size
        self.__update()

    def setPosition(self, pos):
        self.__position = pos
        self.__update()

    def setColor(self, clr):
        self.__color = clr
        self.__update()

    def getRect(self):
        return self.__textRect

    def __update(self):
        self.__font = pygame.font.Font(None, self.__font_size)
        self.__text = self.__font.render(self.__string, True, self.__color)
        self.__textRect = self.__text.get_rect()
        self.__textRect.center = self.__position

    def render(self, display):
        display.blit(self.__text, self.__textRect)
