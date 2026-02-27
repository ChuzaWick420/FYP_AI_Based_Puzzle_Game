import pygame
from prototype.data.SystemEvents import SystemEvents
from prototype.presentation_layer.InputHandler import InputHandler

class Engine:
    def __init__(self, window_dimensions):
        self.resolution = window_dimensions
        self.input_handler = InputHandler()
        pygame.init()

    def load(self):
        return

    def start(self):
        screen = pygame.display.set_mode(self.resolution)
        isRunning = True

        while isRunning:
            events = self.input_handler.processEvents()

            for event in events:
                if event == SystemEvents.TERMINATE_GAME:
                    isRunning = False

                # if event == SystemEvents.MOUSE_CLICK:
                #

            screen.fill("purple")
            pygame.display.flip()

        pygame.quit()

    def save(self):
        return
