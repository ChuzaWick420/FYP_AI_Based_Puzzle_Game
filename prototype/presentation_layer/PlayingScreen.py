import pygame

from prototype.entities.TextElement import TextElement

class PlayingScreen:
    def __init__(self):
        color = (89, 255, 60)
        self.timer = TextElement("Timer: 00:00", color, (50, 50))
        self.scores = TextElement("Scores: 69", color, (50, 100))
        self.maze = pygame.image.load("G:/Projects/FYP_AI_Based_Puzzle_Game/assets/maze.png")

    def render(self, display):
        display.blit(self.timer.text, self.timer.textRect)
        display.blit(self.scores.text, self.scores.textRect)
        display.blit(self.maze, (100, 100))
