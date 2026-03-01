import pygame

from prototype.Data_Layer import Global
from prototype.Presentation_Layer.TextElement import TextElement

class PlayingScreen:
    def __init__(self):
        color = (89, 255, 60)
        self.timer = TextElement("Timer: 00:00", color, (100, 50))
        self.scores = TextElement("Scores: 100", color, (100, 100))
        self.maze = pygame.image.load("assets/maze.png")
        self.mazeRect = self.maze.get_rect()
        self.mazeRect.center = (Global.WINDOW_RESOLUTION[0] // 2, Global.WINDOW_RESOLUTION[1] // 2)

    def render(self, display):
        display.blit(self.timer.text, self.timer.textRect)
        display.blit(self.scores.text, self.scores.textRect)
        display.blit(self.maze, self.mazeRect)
