import pygame

from prototype.Data_Layer import Global
from prototype.Presentation_Layer.Block import Block
from prototype.Presentation_Layer.TextElement import TextElement
from prototype.Service_Layer.Maze_Manager import Maze_Manager
from prototype.Service_Layer.spawn_entities import spawn_entities

class PlayingScreen:
    def __init__(self, render_data):
        color = (89, 255, 60)
        self.timer = TextElement("Timer: 00:00", color, (100, 50))
        self.scores = TextElement("Scores: 100", color, (100, 100))

        # self.maze_manager = Maze_Manager()
        self.update_maze(render_data)

    def setTimer(self, minutes, seconds):
        self.timer.setText("Timer: {0:02}:{1:02}".format(minutes // 60, seconds % 60))

    def update_maze(self, render_data):
        self.render_data = render_data
        self.visual = self.get_visual(render_data)

    def render(self, display):
        display.blit(self.timer.text, self.timer.textRect)
        display.blit(self.scores.text, self.scores.textRect)

        # NOTE: Updates the visual and renders it
        self.update_maze(self.render_data)
        self.visual.draw(display)

    def get_visual(self, render_data):
        maze_visual = pygame.sprite.Group()

        for color, size, pos in render_data:
            maze_visual.add(Block(color, size, pos))

        # NOTE: Center the maze visual
        rects = [sprite.rect for sprite in maze_visual.sprites()]
        group_rect = rects[0].unionall(rects[1:])

        offset_x = (Global.WINDOW_RESOLUTION[0] // 2) - group_rect.centerx
        offset_y = (Global.WINDOW_RESOLUTION[1] // 2) - group_rect.centery

        for sprite in maze_visual:
            sprite.rect.x += offset_x
            sprite.rect.y += offset_y

        return maze_visual

    # def get_map_width(self):
    #     return len(self.maze_manager.maze_map)
    #
    # def get_path(self):
    #     return self.maze_manager.path
