import pygame
from prototype.Data_Layer import Global
from prototype.Domain_Logic_Layer.GameStates import GameStates
from prototype.Data_Layer.SystemEvents import SystemEvents
from prototype.Domain_Logic_Layer.entities.StateMachine import StateMachine
from prototype.Presentation_Layer.menus.difficulty_menu import DifficultyMenu
from prototype.Presentation_Layer.menus.main_menu import MainMenu
from prototype.Presentation_Layer.menus.pause_menu import PauseMenu
from prototype.Presentation_Layer.menus.result_menu import ResultMenu
from prototype.Presentation_Layer.menus.scoreboard_menu import ScoreBoardMenu
from prototype.Presentation_Layer.InputHandler import InputHandler
from prototype.Presentation_Layer.PlayingScreen import PlayingScreen

class Engine:
    def __init__(self):
        pygame.init()
        self.resolution = Global.WINDOW_RESOLUTION
        self.input_handler = InputHandler()
        self.elapsed_time = 0
        self.stateMachine = StateMachine()

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
        self.isRunning = True

    def load(self):
        return

    def start(self):
        self.screen = pygame.display.set_mode(self.resolution)
        self.ticks = pygame.time.get_ticks()

        while self.isRunning:
            events = self.input_handler.processEvents()
            self.handleEvents(events)
            self.render()

            # empty the event buffer
            self.input_handler.reset()

        self.save()

    def save(self):
        pygame.quit()

    def manageStateTransition(self):
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

        self.current_state = self.next_state

    def handleEvents(self, events):
        for event in events:
            if event == SystemEvents.TERMINATE_GAME:
                self.isRunning = False

            if event == SystemEvents.MOUSE_CLICK:
                if self.current_state == GameStates.PLAY:
                    self.next_state = self.stateMachine.getNextState(None, self.current_state)
                    self.input_handler.createEvent(SystemEvents.STATE_TRANSITION)
                else:
                    for button in self.current_menu.buttons:
                        if (button.isClicked()):
                            self.next_state = self.stateMachine.getNextState(button.name, self.current_state)
                            self.input_handler.createEvent(SystemEvents.STATE_TRANSITION)

            if event == SystemEvents.STATE_TRANSITION:
                self.manageStateTransition()

    def render(self):
        self.screen.fill("black") # Screen Background

        if self.current_state == GameStates.RESULTS:
            minutes = self.elapsed_time // 60
            seconds = self.elapsed_time % 60
            self.result_menu.setTimer(minutes, seconds)

        if self.current_state == GameStates.PLAY:
            self.elapsed_time = (pygame.time.get_ticks() - self.ticks) // 1000
            minutes = self.elapsed_time // 60
            seconds = self.elapsed_time % 60
            self.playing_screen.setTimer(minutes, seconds)
            self.playing_screen.render(self.screen)
        else:
            self.ticks = pygame.time.get_ticks()
            self.current_menu.render(self.screen)

        pygame.display.flip() # Display
