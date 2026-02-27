import pygame
from prototype.data.GameStates import GameStates
from prototype.data.SystemEvents import SystemEvents
from prototype.menus.main_menu import MainMenu
from prototype.presentation_layer.InputHandler import InputHandler
from prototype.services.GetNextState import getNextState

class Engine:
    def __init__(self, window_dimensions):
        pygame.init()
        self.resolution = window_dimensions
        self.input_handler = InputHandler()
        self.main_menu = MainMenu()
        self.current_meny = self.main_menu
        self.current_state = GameStates.MAINMENU
        self.next_state = GameStates.PLAY

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
                    for button in self.main_menu.buttons:
                        if (button.isClicked()):
                            self.next_state = getNextState(button.name, self.current_state)
                            self.input_handler.createEvent(SystemEvents.STATE_TRANSITION)

                if event == SystemEvents.STATE_TRANSITION:
                    self.current_state = self.next_state

            screen.fill("purple")
            self.main_menu.render(screen)
            pygame.display.flip()

            # empty the event buffer
            self.input_handler.reset()

        pygame.quit()

    def save(self):
        return
