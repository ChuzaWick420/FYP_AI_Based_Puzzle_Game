import pygame

class Button:
    def __init__(self, name, pos):
        self.name = name
        color = (255, 100, 100)
        font = pygame.font.Font(None, 32)
        self.text = font.render(name, True, color)
        self.textRect = self.text.get_rect()
        self.position = pos
        self.textRect.center = self.position

    def updatePosition(self, pos):
        self.position = pos
        self.textRect.center = self.position

    def isClicked(self):
        flag = False

        mouse_pos = pygame.mouse.get_pos()

        horizontal_left  = mouse_pos[0] >= self.position[0] - self.textRect.width // 2
        horizontal_right = mouse_pos[0] <= self.position[0] + self.textRect.width // 2
        vertical_up      = mouse_pos[1] >= self.position[1] - self.textRect.height // 2
        vertical_down    = mouse_pos[1] <= self.position[1] + self.textRect.height // 2

        if (horizontal_left and horizontal_right and vertical_up and vertical_down):
            flag = True

        return flag
