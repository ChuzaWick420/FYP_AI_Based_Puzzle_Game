import pygame

from src.Data_Layer import Global
from src.Data_Layer.StateInputs import StateInputs
from src.Presentation_Layer.Block import Block
from src.Presentation_Layer.Button import Button
from src.Presentation_Layer.TextElement import TextElement

class PlayingScreen:
    def __init__(self):
        color = (176, 228, 204)
        self.__timer = TextElement("Timer: 00:00", color, (100, 50))
        self.__level_num = TextElement("Level: 1", color, (100, 100))

        self.pause_button = Button("Pause", StateInputs.PAUSE, (Global.WINDOW_RESOLUTION[0] - 150, 100))
        self.pause_button.loadIcon("assets/pause_button.png")

        self.__visual = pygame.sprite.Group()

    def setTimer(self, minutes, seconds):
        self.__timer.setText("Timer: {0:02}:{1:02}".format(minutes, seconds))

    def setLevel(self, level):
        self.__level_num.setText(f"Level: {str(level)}")

    def update_maze(self, render_data):
        self.__visual = self.get_visual(render_data)

    def render(self, display):
        self.__timer.render(display)
        self.__level_num.render(display)

        self.pause_button.render(display)

        # NOTE: Updates the visual and renders it
        self.__visual.draw(display)

    def get_visual(self, render_data):
        maze_visual = pygame.sprite.Group()

        # PERF: Need optimization, updates are really laggy.
        #       Following 2 lines seems to be the source of lag.
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
