import pygame
from prototype.data.SystemEvents import SystemEvents
from prototype.menus.main_menu import MainMenu
from prototype.presentation_layer.InputHandler import InputHandler

class Engine:
    def __init__(self, window_dimensions):
        pygame.init()
        self.resolution = window_dimensions
        self.input_handler = InputHandler()
        self.menu = MainMenu()

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

                if event == SystemEvents.MOUSE_CLICK:
                    for button in self.menu.buttons:
                        if (button.isClicked()):
                            print("Button Clicked")

            screen.fill("purple")
            self.menu.render(screen)
            pygame.display.flip()

        pygame.quit()

    def save(self):
        return
