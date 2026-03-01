import pygame
from prototype.Data_Layer.GameStates import GameStates
from prototype.Data_Layer.SystemEvents import SystemEvents
from prototype.Presentation_Layer.menus.difficulty_menu import DifficultyMenu
from prototype.Presentation_Layer.menus.main_menu import MainMenu
from prototype.Presentation_Layer.menus.pause_menu import PauseMenu
from prototype.Presentation_Layer.menus.result_menu import ResultMenu
from prototype.Presentation_Layer.menus.scoreboard_menu import ScoreBoardMenu
from prototype.Presentation_Layer.InputHandler import InputHandler
from prototype.Presentation_Layer.PlayingScreen import PlayingScreen
from prototype.Service_Layer.GetNextState import getNextState

class Engine:
    def __init__(self, window_dimensions):
        pygame.init()
        self.resolution = window_dimensions
        self.input_handler = InputHandler()
        self.elapsed_time = 0

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
        ticks = pygame.time.get_ticks()

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

            screen.fill("black") # Screen Background

            # NOTE: Gameplay Logic Start

            if self.current_state == GameStates.RESULTS:
                self.result_menu.setTimer("Timer: {0:02}:{1:02}".format(self.elapsed_time // 60, self.elapsed_time % 60))

            if self.current_state == GameStates.PLAY:
                self.elapsed_time = (pygame.time.get_ticks() - ticks) // 1000
                self.playing_screen.timer.updateText("Timer: {0:02}:{1:02}".format(self.elapsed_time // 60, self.elapsed_time % 60))
                self.playing_screen.render(screen)
            else:
                ticks = pygame.time.get_ticks()
                self.current_menu.render(screen)

            # NOTE: Gameplay Logic End

            pygame.display.flip() # Display

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
