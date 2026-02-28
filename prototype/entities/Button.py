import pygame
from prototype.entities.TextElement import TextElement

class Button:
    def __init__(self, name, pos):
        self.name = name
        color = (33, 128, 24)
        self.text = TextElement(name, color, pos)
        self.position = pos

    def updatePosition(self, pos):
        self.position = pos
        self.text.setPosition(pos)


    def isClicked(self):
        flag = False

        mouse_pos = pygame.mouse.get_pos()

        horizontal_left  = mouse_pos[0] >= self.position[0] - self.text.textRect.width // 2
        horizontal_right = mouse_pos[0] <= self.position[0] + self.text.textRect.width // 2
        vertical_up      = mouse_pos[1] >= self.position[1] - self.text.textRect.height // 2
        vertical_down    = mouse_pos[1] <= self.position[1] + self.text.textRect.height // 2

        if (horizontal_left and horizontal_right and vertical_up and vertical_down):
            flag = True

        return flag

    def render(self, display):
        display.blit(self.text.text, self.text.textRect)
