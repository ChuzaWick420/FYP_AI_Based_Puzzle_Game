import pygame
from prototype.data.GameStates import GameStates
from prototype.data.SystemEvents import SystemEvents
from prototype.menus.difficulty_menu import DifficultyMenu
from prototype.menus.main_menu import MainMenu
from prototype.menus.pause_menu import PauseMenu
from prototype.menus.result_menu import ResultMenu
from prototype.menus.scoreboard_menu import ScoreBoardMenu
from prototype.presentation_layer.InputHandler import InputHandler
from prototype.presentation_layer.PlayingScreen import PlayingScreen
from prototype.services.GetNextState import getNextState

class Engine:
    def __init__(self, window_dimensions):
        pygame.init()
        self.resolution = window_dimensions
        self.input_handler = InputHandler()

        # Menus
        self.main_menu = MainMenu()
        self.difficulty_menu = DifficultyMenu()
        self.pause_menu = PauseMenu()
        self.result_menu = ResultMenu()
        self.scoreboard_menu = ScoreBoardMenu()

        self.playing_screen = PlayingScreen()

        # States
        self.current_menu = self.main_menu
        self.current_state = GameStates.MAINMENU
        self.next_state = GameStates.PLAY

    def load(self):
        return

    def start(self):
        screen = pygame.display.set_mode(self.resolution)
        self.isRunning = True

        while self.isRunning:
            events = self.input_handler.processEvents()

            for event in events:
                if event == SystemEvents.TERMINATE_GAME:
                    self.isRunning = False

                if event == SystemEvents.MOUSE_CLICK:
                    if self.current_state == GameStates.PLAY:
                        self.next_state = getNextState(None, self.current_state)
                        self.input_handler.createEvent(SystemEvents.STATE_TRANSITION)
                    else:
                        for button in self.current_menu.buttons:
                            if (button.isClicked()):
                                self.next_state = getNextState(button.name, self.current_state)
                                self.input_handler.createEvent(SystemEvents.STATE_TRANSITION)

                if event == SystemEvents.STATE_TRANSITION:
                    self.manageState()
                    self.current_state = self.next_state

            screen.fill("purple")

            if self.current_state == GameStates.PLAY:
                self.playing_screen.render(screen)
            else:
                self.current_menu.render(screen)

            pygame.display.flip()

            # empty the event buffer
            self.input_handler.reset()

        pygame.quit()

    def save(self):
        return

    def manageState(self):
        if self.next_state == GameStates.EXIT:
            self.isRunning = False

        if self.next_state == GameStates.DIFFICULTY_SELECTION:
            self.current_menu = self.difficulty_menu

        if self.next_state == GameStates.MAINMENU:
            self.current_menu = self.main_menu

        if self.next_state == GameStates.RESULTS:
            self.current_menu = self.result_menu

        if self.next_state == GameStates.PAUSE:
            self.current_menu = self.pause_menu

        if self.next_state == GameStates.SCORE_BOARD:
            self.current_menu = self.scoreboard_menu
