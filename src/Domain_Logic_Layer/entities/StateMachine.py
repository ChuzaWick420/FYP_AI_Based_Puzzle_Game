from src.Domain_Logic_Layer.GameStates import GameStates

class StateMachine:
    def __init__(self):
        self.current_state = GameStates.MAINMENU
        self.next_state = GameStates.PLAY

    def stepState(self, button_id):
        if self.current_state == GameStates.MAINMENU:
            if button_id == "Play":
                self.next_state = GameStates.PLAY

            if button_id == "Select Difficulty":
                self.next_state = GameStates.DIFFICULTY_SELECTION

            if button_id == "Scoreboard":
                self.next_state = GameStates.SCORE_BOARD

            if button_id == "Quit":
                self.next_state = GameStates.EXIT

        if self.current_state == GameStates.DIFFICULTY_SELECTION:
            if button_id == "Easy" or button_id == "Medium" or button_id == "Hard":
                self.next_state = GameStates.MAINMENU

        if self.current_state == GameStates.PAUSE:
            if button_id == "Resume":
                self.next_state = GameStates.PLAY

            if button_id == "Restart":
                self.next_state = GameStates.PLAY

            if button_id == "Home":
                self.next_state = GameStates.MAINMENU

        if self.current_state == GameStates.RESULTS:
            if button_id == "Restart":
                self.next_state = GameStates.PLAY

            if button_id == "Next":
                self.next_state = GameStates.PLAY

            if button_id == "Scoreboard":
                self.next_state = GameStates.SCORE_BOARD

            if button_id == "Home":
                self.next_state = GameStates.MAINMENU

        if self.current_state == GameStates.SCORE_BOARD:
            if button_id == "Home":
                self.next_state = GameStates.MAINMENU

        if self.current_state == GameStates.PLAY:
            if button_id == "Pause":
                self.next_state = GameStates.PAUSE
            if button_id == "Finished":
                self.next_state = GameStates.RESULTS
