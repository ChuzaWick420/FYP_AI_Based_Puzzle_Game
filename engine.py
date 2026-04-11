import pygame
import time
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

        # Configuration
        self.resolution = Global.WINDOW_RESOLUTION
        self.elapsed_time = 0
        self.frame_rate = 60
        self.PHYSICS_TIME_UNIT = 1.0 / 120.0 
        self.physics_accumulator = 0.0
        self.window_background = "black"

        # Derived Configuration
        self.frame_time = 1.0 / self.frame_rate

        # Objects
        self.input_handler = InputHandler()
        self.stateMachine = StateMachine()

        # Menus
        self.main_menu       = MainMenu()
        self.difficulty_menu = DifficultyMenu()
        self.pause_menu      = PauseMenu()
        self.result_menu     = ResultMenu()
        self.scoreboard_menu = ScoreBoardMenu()

        self.playing_screen = PlayingScreen()

        # States
        self.current_menu = self.main_menu
        self.isRunning = True

    def start(self):
        self.load()
        self.execute()
        self.cleanup()

    def load(self):
        return

    def handlePhysics(self, current, last):
        dt = current - last
        dt = min(dt, 0.25) # NOTE: Clamp dt to avoid spiral of death

        self.physics_accumulator += dt
        while self.physics_accumulator >= self.PHYSICS_TIME_UNIT:
            # TODO: Update Physics here
            self.physics_accumulator -= self.PHYSICS_TIME_UNIT

    def handleProcesses(self, frame_start):
       frame_end = time.perf_counter()
       elapsed = frame_end - frame_start

       remaining_time = self.frame_time - elapsed

       if remaining_time > 0:
           bg_start = time.perf_counter()

           while (time.perf_counter() - bg_start) < remaining_time:
               events = self.input_handler.processEvents()
               self.handleEvents(events)
               self.input_handler.reset()  # NOTE: empty the event buffer

    def execute(self):

        self.screen = pygame.display.set_mode(self.resolution)
        self.ticks = pygame.time.get_ticks()

        last_time = time.perf_counter()

        while self.isRunning:

            # NOTE: Time Slice execution time into
            # 1. Rendering (30 or 60 Frames per second)
            # 2. Physics (time units)
            # 3. Background computations

            frame_start = time.perf_counter()
            current_time = time.perf_counter()

            self.handlePhysics(current_time, last_time)
            self.render()
            self.handleProcesses(frame_start)

            last_time = current_time

    def render(self):
        self.screen.fill(self.window_background) # Screen Background

        if self.stateMachine.current_state == GameStates.RESULTS:
            minutes = self.elapsed_time // 60
            seconds = self.elapsed_time % 60
            self.result_menu.setTimer(minutes, seconds)

        if self.stateMachine.current_state == GameStates.PLAY:
            self.elapsed_time = (pygame.time.get_ticks() - self.ticks) // 1000
            minutes = self.elapsed_time // 60
            seconds = self.elapsed_time % 60
            self.playing_screen.setTimer(minutes, seconds)
            self.playing_screen.render(self.screen)
        else:
            self.ticks = pygame.time.get_ticks()
            self.current_menu.render(self.screen)

        pygame.display.flip() # Display

    def cleanup(self):
        pygame.quit()

    def manageMenuTransition(self):
        if self.stateMachine.next_state == GameStates.EXIT:
            self.isRunning = False

        if self.stateMachine.next_state == GameStates.DIFFICULTY_SELECTION:
            self.current_menu = self.difficulty_menu

        if self.stateMachine.next_state == GameStates.MAINMENU:
            self.current_menu = self.main_menu

        if self.stateMachine.next_state == GameStates.RESULTS:
            self.current_menu = self.result_menu

        if self.stateMachine.next_state == GameStates.PAUSE:
            self.current_menu = self.pause_menu

        if self.stateMachine.next_state == GameStates.SCORE_BOARD:
            self.current_menu = self.scoreboard_menu

        self.stateMachine.current_state = self.stateMachine.next_state

    def handleEvents(self, events):
        for event in events:
            if event == SystemEvents.TERMINATE_GAME:
                self.isRunning = False

            if event == SystemEvents.MOUSE_CLICK:
                if self.stateMachine.current_state == GameStates.PLAY:
                    self.stateMachine.stepState(None)
                    self.input_handler.createEvent(SystemEvents.STATE_TRANSITION)
                else:
                    for button in self.current_menu.buttons:
                        if (button.isClicked()):
                            self.stateMachine.stepState(button.name)
                            self.input_handler.createEvent(SystemEvents.STATE_TRANSITION)

            if event == SystemEvents.STATE_TRANSITION:
                self.manageMenuTransition()
