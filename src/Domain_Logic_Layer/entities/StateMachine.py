from src.Data_Layer.StateInputs import StateInputs
from src.Domain_Logic_Layer.GameStates import GameStates

class StateMachine:
    def __init__(self):
        self.current_state = GameStates.MAINMENU
        self.next_state = GameStates.PLAY

    def stepState(self, input):

        if self.current_state == GameStates.MAINMENU:
            if input == StateInputs.PLAY:
                self.next_state = GameStates.PLAY

            if input == StateInputs.DIFFICULTY_SELECTION:
                self.next_state = GameStates.DIFFICULTY_SELECTION

            if input == StateInputs.SCORE_BOARD:
                self.next_state = GameStates.SCORE_BOARD

            if input == StateInputs.EXIT:
                self.next_state = GameStates.EXIT

        if self.current_state == GameStates.DIFFICULTY_SELECTION:
            if input == StateInputs.DIFFICULTY_EASY or input == StateInputs.DIFFICULTY_MEDIUM or input == StateInputs.DIFFICULTY_HARD:
                self.next_state = GameStates.MAINMENU

        if self.current_state == GameStates.PAUSE:
            if input == StateInputs.RESUME:
                self.next_state = GameStates.PLAY

            if input == StateInputs.RESTART:
                self.next_state = GameStates.PLAY

            if input == StateInputs.EXIT:
                self.next_state = GameStates.MAINMENU

        if self.current_state == GameStates.RESULTS:
            if input == StateInputs.RESTART:
                self.next_state = GameStates.PLAY

            if input == StateInputs.NEXT:
                self.next_state = GameStates.PLAY

            if input == StateInputs.SCORE_BOARD:
                self.next_state = GameStates.SCORE_BOARD

            if input == StateInputs.EXIT:
                self.next_state = GameStates.MAINMENU

        if self.current_state == GameStates.SCORE_BOARD:
            if input == StateInputs.EXIT:
                self.next_state = GameStates.MAINMENU

        if self.current_state == GameStates.PLAY:
            if input == StateInputs.PAUSE:
                self.next_state = GameStates.PAUSE

            if input == StateInputs.EXIT:
                self.next_state = GameStates.RESULTS

        self.current_state = self.next_state

    def getCurrentState(self):
        return self.current_state

    def getNextState(self):
        return self.next_state
