from prototype.Domain_Logic_Layer.GameStates import GameStates
class StateMachine:
    def __init__(self):
        return

    def getNextState(self, button_id, current_state):
        if current_state == GameStates.MAINMENU:
            if button_id == "Play":
                return GameStates.PLAY

            if button_id == "Select Difficulty":
                return GameStates.DIFFICULTY_SELECTION

            if button_id == "Scoreboard":
                return GameStates.SCORE_BOARD

            if button_id == "Quit":
                return GameStates.EXIT

        if current_state == GameStates.DIFFICULTY_SELECTION:
            if button_id == "Easy" or button_id == "Medium" or button_id == "Hard":
                return GameStates.MAINMENU

        if current_state == GameStates.PAUSE:
            if button_id == "Resume":
                return GameStates.PLAY

            if button_id == "Restart":
                return GameStates.PLAY

            if button_id == "Quit":
                return GameStates.MAINMENU

        if current_state == GameStates.RESULTS:
            if button_id == "Restart Level":
                return GameStates.PLAY

            if button_id == "Scoreboard":
                return GameStates.SCORE_BOARD

            if button_id == "Home":
                return GameStates.MAINMENU

        if current_state == GameStates.SCORE_BOARD:
            if button_id == "Home":
                return GameStates.MAINMENU

        if current_state == GameStates.PLAY:
            return GameStates.RESULTS
