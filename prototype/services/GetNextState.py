from prototype.data.GameStates import GameStates

def getNextState(button_id, current_state):
    if current_state == GameStates.MAINMENU:
        if button_id == "Play":
            return GameStates.PLAY
