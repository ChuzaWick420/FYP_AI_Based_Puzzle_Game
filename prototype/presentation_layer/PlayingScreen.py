import pygame

from prototype.Data_Layer import Global
from prototype.Presentation_Layer.Ai import Ai
from prototype.Presentation_Layer.Player import Player
from prototype.Presentation_Layer.PowerUp import PowerUp
from prototype.Presentation_Layer.TextElement import TextElement
from prototype.Service_Layer.get_maze import get_presentation_grid
from prototype.Service_Layer.maze_generator import visualize_grid
from prototype.Service_Layer.spawn_entities import spawn_entities

class PlayingScreen:
    def __init__(self):
        color = (89, 255, 60)
        self.timer = TextElement("Timer: 00:00", color, (100, 50))
        self.scores = TextElement("Scores: 100", color, (100, 100))
        # self.maze = pygame.image.load("assets/maze.png")
        # self.mazeRect = self.maze.get_rect()
        # self.mazeRect.center = (Global.WINDOW_RESOLUTION[0] // 2, Global.WINDOW_RESOLUTION[1] // 2)


        self.grid = get_presentation_grid(16 * 16)

        spawn_entities(self.grid)

        # self.player  = Player()
        # self.ai      = Ai()
        # self.powerup = PowerUp()

        # self.player.spawn(self.maze_data[1])
        # self.ai.spawn(self.maze_data[1])
        # self.powerup.spawn(self.maze_data[1])

        self.visual = visualize_grid(self.grid)


    def setTimer(self, minutes, seconds):
        self.timer.setText("Timer: {0:02}:{1:02}".format(minutes // 60, seconds % 60))

    def render(self, display):
        display.blit(self.timer.text, self.timer.textRect)
        display.blit(self.scores.text, self.scores.textRect)
        # display.blit(self.maze, self.mazeRect)
        self.visual.draw(display)

        # self.player.render(display)
        # self.ai.render(display)
        # self.powerup.render(display)


    # NOTE: Moved implementation is moved inside generate_maze()

    # def get_visual(self):
    #     group = self.maze_data[2]
    #     rects = [sprite.rect for sprite in group.sprites()]
    #     group_rect = rects[0].unionall(rects[1:])
    #
    #     offset_x = (Global.WINDOW_RESOLUTION[0] // 2) - group_rect.centerx
    #     offset_y = (Global.WINDOW_RESOLUTION[1] // 2) - group_rect.centery
    #
    #     print("Magic x: ", offset_x)
    #     print("Magic y: ", offset_y)
    #
    #     for sprite in group:
    #         sprite.rect.x += offset_x
    #         sprite.rect.y += offset_y
    #
    #     return group

