from prototype.data.GameStates import GameStates

def getNextState(button_id, current_state):

    if current_state == GameStates.MAINMENU:
        if button_id == "Play":
            return GameStates.PLAY

        if button_id == "Select Difficulty":
            return GameStates.DIFFICULTY_SELECTION

        if button_id == "Quit":
            return GameStates.EXIT

    if current_state == GameStates.DIFFICULTY_SELECTION:
        if button_id == "Easy" or button_id == "Medium" or button_id == "Hard":
            return GameStates.MAINMENU
