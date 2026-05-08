import pygame
import time
from src.Data_Layer import Global
from src.Data_Layer.CellTypes import CellTypes
from src.Data_Layer.DB_Manager import DB_Manager
from src.Data_Layer.StateInputs import StateInputs
from src.Domain_Logic_Layer.GameStates import GameStates
from src.Data_Layer.SystemEvents import SystemEvents
from src.Domain_Logic_Layer.entities.Ai import Ai
from src.Domain_Logic_Layer.entities.EventListener import EventListener
from src.Domain_Logic_Layer.entities.Player import Player
from src.Domain_Logic_Layer.entities.StateMachine import StateMachine
from src.Presentation_Layer.menus.difficulty_menu import DifficultyMenu
from src.Presentation_Layer.menus.main_menu import MainMenu
from src.Presentation_Layer.menus.pause_menu import PauseMenu
from src.Presentation_Layer.menus.result_menu import ResultMenu
from src.Presentation_Layer.menus.scoreboard_menu import ScoreBoardMenu
from src.Presentation_Layer.InputHandler import InputHandler
from src.Presentation_Layer.PlayingScreen import PlayingScreen
from src.Service_Layer.Maps_Manager import Maps_Manager

class Engine:
    def __init__(self):
        pygame.init()

        # Configuration
        self.resolution = Global.WINDOW_RESOLUTION
        self.frame_rate = 60
        self.PHYSICS_FREQUENCY = 120.0 # NOTE: In Hz
        self.ticks_ai_step = 0
        self.physics_accumulator = 0.0
        self.ticks_play_time = 0
        self.window_background = "black"
        self.elapsed_play_time = 0
        self.blinders_spawned = False
        self.visible_for_seconds = 10

        # Derived Configuration
        self.frame_time = 1.0 / self.frame_rate
        self.PHYSICS_TIME_UNIT = 1.0 / self.PHYSICS_FREQUENCY
        self.levels_per_category = Global.MAX_LEVELS // 3

        # Objects
        self.input_handler = InputHandler()
        self.event_listener = EventListener()
        self.stateMachine = StateMachine()
        self.maps_manager = Maps_Manager()
        self.db_manager = DB_Manager()
        self.player = Player()
        self.ai = Ai()

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
        self.isKeyUp = True
        self.play_time = 0

        # NOTE: This data depends on dataase to be loaded.
        self.current_level = 0
        self.ai_speed_ideal = 0
        self.ai_speed_current = 0

    def start(self):
        self.load()
        self.execute()
        self.cleanup()

    def initialize(self):

        # NOTE: Initializing Maze Manager
        if len(self.adjacent_matrix) == 0:
            self.maps_manager.initialize_graph(self.current_level)
        else:
            self.maps_manager.initialize_graph(self.current_level, self.adjacent_matrix)

        # NOTE: Update maze's visual
        self.playing_screen.update_maze(self.maps_manager.get_render_data())

        # NOTE: initializing Player and AI
        self.player.init(self.maps_manager.maze_map)
        self.ai.init(self.maps_manager.path)

        # NOTE: AI's speed in blocks per second depending on level number
        max_speed = 3
        min_speed = 1

        self.ai_speed_ideal = min_speed + self.current_level * (max_speed - min_speed) / Global.MAX_LEVELS
        self.ai_speed_current = self.ai_speed_ideal

    def load(self):
        self.db_manager.load()

        self.current_level = self.db_manager.file_data["current_level"]
        self.adjacent_matrix = self.db_manager.file_data["Graph_adjacent_matrix"]

        # self.db_manager.log()

    def handlePhysics(self, current, last):
        dt = current - last
        dt = min(dt, 0.25) # NOTE: Clamp dt to avoid spiral of death

        self.physics_accumulator += dt
        while self.physics_accumulator >= self.PHYSICS_TIME_UNIT:
            # NOTE: Update Physics here
            if self.stateMachine.current_state == GameStates.PLAY:
                self.ticks_ai_step += 1
                self.ticks_play_time += 1
            self.physics_accumulator -= self.PHYSICS_TIME_UNIT

        if (self.ticks_play_time >= 1 * self.PHYSICS_FREQUENCY):
            self.elapsed_play_time += 1
            self.event_listener.createEvent(SystemEvents.TIME_UPDATE)
            self.ticks_play_time = 0

        if self.ticks_ai_step * self.ai_speed_current >= self.PHYSICS_FREQUENCY:
            if self.stateMachine.current_state == GameStates.PLAY:
                self.ai.step()
                self.event_listener.createEvent(SystemEvents.MAZE_UPDATE)

            # Reset
            self.ticks_ai_step = 0

    def handleProcesses(self, frame_start):
        frame_end = time.perf_counter()
        elapsed = frame_end - frame_start

        remaining_time = self.frame_time - elapsed

        if remaining_time > 0:
            bg_start = time.perf_counter()

            while (time.perf_counter() - bg_start) < remaining_time:
                event = self.input_handler.processEvents()
                if event != None:
                    self.event_listener.createEvent(event)

                self.handleEvents()

    def execute(self):
        self.initialize()
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

        if self.stateMachine.current_state == GameStates.PLAY:
            self.playing_screen.render(self.screen)
        else:
            self.current_menu.render(self.screen)
            self.current_menu.handle_hover()

        pygame.display.flip() # Display

    def cleanup(self):

        # save current level number
        self.db_manager.file_data["current_level"] = self.current_level

        # Save map for current level
        self.db_manager.file_data["Graph_adjacent_matrix"] = self.maps_manager.graph.adj_matrix

        self.db_manager.flush() 
        pygame.quit()

    def manageMenuTransition(self):

        # NOTE: Reset the active button tracker
        self.current_menu.active_btn_id = 0

        if self.stateMachine.next_state == GameStates.EXIT:
            self.event_listener.createEvent(SystemEvents.TERMINATE_GAME)

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

    def handleEvents(self):
        # Events
        for event in self.event_listener.getEvents():

            if event == SystemEvents.DIFFICULTY_EASY:
                self.current_level = 0 * self.levels_per_category + 1
                self.event_listener.createEvent(SystemEvents.LEVEL_GENERATED)
            if event == SystemEvents.DIFFICULTY_MEDIUM:
                self.current_level = 1 * self.levels_per_category + 1
                self.event_listener.createEvent(SystemEvents.LEVEL_GENERATED)
            if event == SystemEvents.DIFFICULTY_HARD:
                self.current_level = 2 * self.levels_per_category + 1
                self.event_listener.createEvent(SystemEvents.LEVEL_GENERATED)

            if event == SystemEvents.LEVEL_GENERATED:
                self.initialize()

            if event == SystemEvents.LEVEL_RESET:
                self.player.reset()
                self.ai.reset()
                # NOTE: Reset the frame buffer
                self.maps_manager.initialize()
                # NOTE: Reset play time
                self.elapsed_play_time = 0
                self.ai_speed_current = self.ai_speed_ideal

            # NOTE: Maze update
            # PERF: Causing few second lags at timestamps: 6, 19, 35 seconds onwards
            if event == SystemEvents.MAZE_UPDATE:
                self.handleEventMaze()

            # NOTE: Keyboard handling
            if event == SystemEvents.KEY_RELEASE:
                self.isKeyUp = True

            self.handleEventKeyboard(event)

            # NOTE: Mouse handling
            if event == SystemEvents.MOUSE_CLICK:
                self.handleEventMouse()

            # NOTE: Termination
            if event == SystemEvents.TERMINATE_GAME:
                self.isRunning = False

            if event == SystemEvents.LEVEL_FINISHED:
                self.event_listener.createEvent(SystemEvents.STATE_TRANSITION)

            if event == SystemEvents.STATE_TRANSITION:
                self.manageMenuTransition()

            if event == SystemEvents.TIME_UPDATE:
                minutes = self.elapsed_play_time // 60
                seconds = self.elapsed_play_time % 60
                self.result_menu.setTimer(minutes, seconds)
                self.playing_screen.setTimer(minutes, seconds)

                if (self.elapsed_play_time >= self.visible_for_seconds and self.blinders_spawned == False):
                    self.maps_manager.spawn_blinders()
                    self.blinders_spawned = True

            self.event_listener.processed(event)

    def handle_buttons(self):

        self.current_menu.handle_trigger()

        if self.stateMachine.current_state == GameStates.PLAY:
            if (self.playing_screen.pause_button.isHovered() == True):
                self.stateMachine.stepState(StateInputs.PAUSE)
                self.event_listener.createEvent(SystemEvents.STATE_TRANSITION)

        else:
            # NOTE: Check for button trigger
            for button in self.current_menu.buttons:
                if (button.activeFlag == True):
                    input = button.getInput()

                    # NOTE: Difficulty Selection
                    if self.stateMachine.current_state == GameStates.DIFFICULTY_SELECTION and input == StateInputs.DIFFICULTY_EASY:
                        self.event_listener.createEvent(SystemEvents.DIFFICULTY_EASY)
                    if self.stateMachine.current_state == GameStates.DIFFICULTY_SELECTION and input == StateInputs.DIFFICULTY_MEDIUM:
                        self.event_listener.createEvent(SystemEvents.DIFFICULTY_MEDIUM)
                    if self.stateMachine.current_state == GameStates.DIFFICULTY_SELECTION and input == StateInputs.DIFFICULTY_HARD:
                        self.event_listener.createEvent(SystemEvents.DIFFICULTY_HARD)

                    # NOTE: Reseting level
                    if self.stateMachine.current_state == GameStates.PAUSE and (input == StateInputs.RESTART or input == StateInputs.EXIT):
                        self.event_listener.createEvent(SystemEvents.LEVEL_RESET)
                    if self.stateMachine.current_state == GameStates.RESULTS:
                        self.event_listener.createEvent(SystemEvents.LEVEL_RESET)

                    self.stateMachine.stepState(input)
                    self.event_listener.createEvent(SystemEvents.STATE_TRANSITION)

    def handleEventMouse(self):
        self.handle_buttons()

    def handleEventMaze(self):
        # Get Entity positions
        previous_ai     = (self.ai.prev_x, self.ai.prev_y)
        current_ai      = (self.ai.x_coordinate, self.ai.y_coordinate)
        previous_player = (self.player.prev_x, self.player.prev_y)
        current_player  = (self.player.x_coordinate, self.player.y_coordinate)

        # Ask maze manager to update cells
        # NOTE: handling Player and AI movements
        self.maps_manager.update_cell(previous_player, CellTypes.INVALID["value"])
        self.maps_manager.update_cell(previous_ai,     CellTypes.INVALID["value"])
        self.maps_manager.update_cell(current_ai,      CellTypes.AI     ["value"])
        self.maps_manager.update_cell(current_player,  CellTypes.PLAYER ["value"])

        if (current_player == current_ai):
            self.maps_manager.update_cell(current_player,  CellTypes.PLAYER_AND_AI["value"])

        # NOTE: handling powerups
        if (self.maps_manager.others_map[current_player[1]][current_player[0]] == CellTypes.POWERUP_SLOW["value"]):
            self.ai_speed_current = self.ai_speed_ideal - 1
            self.maps_manager.others_map[current_player[1]][current_player[0]] = CellTypes.INVALID["value"]

        if (self.maps_manager.others_map[current_player[1]][current_player[0]] == CellTypes.POWERUP_REVEAL["value"]):
            self.maps_manager.disable_random_blinders()
            self.maps_manager.others_map[current_player[1]][current_player[0]] = CellTypes.INVALID["value"]

        # NOTE: handling Winner information

        width = len(self.maps_manager.maze_map)
        goal = (width - 1, width - 2)

        if (current_ai == goal or current_player == goal):
            self.stateMachine.stepState(StateInputs.EXIT)
            self.event_listener.createEvent(SystemEvents.LEVEL_FINISHED)

        if (current_ai == goal):
            self.result_menu.winner_info.setText("You Lose!")
            self.result_menu.buttons[0].text.setText("Restart")
            self.result_menu.buttons[0].setInput(StateInputs.RESTART)

        if (current_player == goal):
            self.result_menu.winner_info.setText("You Win!")
            self.result_menu.buttons[0].text.setText("Next")
            self.result_menu.buttons[0].setInput(StateInputs.NEXT)

        # ask playing screen to update render data
        self.playing_screen.update_maze(self.maps_manager.get_render_data())

    def handleEventKeyboard(self, event):

        if self.isKeyUp == True:

            if (event == SystemEvents.RETURN_PRESSED):
                self.handle_buttons()

            if (event == SystemEvents.PAUSE_PRESSED and self.stateMachine.current_state == GameStates.PLAY):
                self.stateMachine.stepState(StateInputs.PAUSE)
                self.event_listener.createEvent(SystemEvents.STATE_TRANSITION)

            is_up_pressed    = event == SystemEvents.UP_PRESSED
            is_down_pressed  = event == SystemEvents.DOWN_PRESSED
            is_left_pressed  = event == SystemEvents.LEFT_PRESSED
            is_right_pressed = event == SystemEvents.RIGHT_PRESSED

            isPlaying = self.stateMachine.current_state == GameStates.PLAY

            if is_up_pressed and isPlaying:    self.player.move_up()
            if is_down_pressed and isPlaying:  self.player.move_down()
            if is_left_pressed and isPlaying:  self.player.move_left()
            if is_right_pressed and isPlaying: self.player.move_right()

            if is_up_pressed and not isPlaying:
                self.current_menu.active_btn_id -= 1
            if is_down_pressed and not isPlaying:
                self.current_menu.active_btn_id += 1

            if is_right_pressed or is_left_pressed or is_up_pressed or is_down_pressed:
                self.isKeyUp = False

                if isPlaying:
                    self.event_listener.createEvent(SystemEvents.MAZE_UPDATE)
