from src.Data_Layer.StateInputs import StateInputs
from src.Domain_Logic_Layer.GameStates import GameStates

class StateMachine:
    def __init__(self):
        self.__current_state = GameStates.MAINMENU
        self.__next_state = GameStates.PLAY

    def stepState(self, input):

        if self.__current_state == GameStates.MAINMENU:
            if input == StateInputs.PLAY:
                self.__next_state = GameStates.PLAY

            if input == StateInputs.DIFFICULTY_SELECTION:
                self.__next_state = GameStates.DIFFICULTY_SELECTION

            if input == StateInputs.SCORE_BOARD:
                self.__next_state = GameStates.SCORE_BOARD

            if input == StateInputs.EXIT:
                self.__next_state = GameStates.EXIT

        if self.__current_state == GameStates.DIFFICULTY_SELECTION:
            if input == StateInputs.DIFFICULTY_EASY or input == StateInputs.DIFFICULTY_MEDIUM or input == StateInputs.DIFFICULTY_HARD:
                self.__next_state = GameStates.MAINMENU

        if self.__current_state == GameStates.PAUSE:
            if input == StateInputs.RESUME:
                self.__next_state = GameStates.PLAY

            if input == StateInputs.RESTART:
                self.__next_state = GameStates.PLAY

            if input == StateInputs.EXIT:
                self.__next_state = GameStates.MAINMENU

        if self.__current_state == GameStates.RESULTS:
            if input == StateInputs.RESTART:
                self.__next_state = GameStates.PLAY

            if input == StateInputs.NEXT:
                self.__next_state = GameStates.PLAY

            if input == StateInputs.SCORE_BOARD:
                self.__next_state = GameStates.SCORE_BOARD

            if input == StateInputs.EXIT:
                self.__next_state = GameStates.MAINMENU

        if self.__current_state == GameStates.SCORE_BOARD:
            if input == StateInputs.EXIT:
                self.__next_state = GameStates.MAINMENU

        if self.__current_state == GameStates.PLAY:
            if input == StateInputs.PAUSE:
                self.__next_state = GameStates.PAUSE

            if input == StateInputs.EXIT:
                self.__next_state = GameStates.RESULTS

        self.__current_state = self.__next_state

    def getCurrentState(self):
        return self.__current_state

    def getNextState(self):
        return self.__next_state

    def setCurrentState(self, state):
        self.__current_state = state

    def setNextState(self, state):
        self.__next_state = state
