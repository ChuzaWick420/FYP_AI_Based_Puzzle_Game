from src.Data_Layer.ButtonType import ButtonType
from src.Data_Layer.StateInputs import StateInputs
from src.Presentation_Layer.TextElement import TextElement
from src.Presentation_Layer.menus.Menu import Menu
from src.Data_Layer import Global
from src.Presentation_Layer.Button import Button

class ResultMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        pos = Global.MENU_TITLE_POS
        gap = 50

        self._text.setText("Result Menu")
        self._text.setPosition(pos)

        # Extras
        color = (64, 138, 113)
        self.__winner_info = TextElement("You Win!", color, (pos[0], pos[1] + 1 * gap))
        self.__completion_time = TextElement("Timer:", color, (pos[0], pos[1] + 2 * gap))

        self._buttons.append(Button("Restart",    StateInputs.RESTART))
        self._buttons.append(Button("Scoreboard", StateInputs.SCORE_BOARD))
        self._buttons.append(Button("Home",       StateInputs.EXIT))

        for button in self._buttons:
            button.setType(ButtonType.TEXTUAL)

        self.stackButtons()

    def render(self, display):
        self._text.render(display)
        self.__winner_info.render(display)
        self.__completion_time.render(display)

        for button in self._buttons:
            button.render(display)

    def setTimer(self, minutes, seconds):
        self.__completion_time.setText("Timer: {0:02}:{1:02}".format(minutes, seconds))

    def setWinner(self, winner):
        if winner == "Player":
            self.__winner_info.setText("Player Wins!")
            self._buttons[0].setInput(StateInputs.NEXT)
            self._buttons[0].text.setText("Next")

        elif winner == "AI":
            self.__winner_info.setText("AI Wins!")
            self._buttons[0].setInput(StateInputs.RESTART)
            self._buttons[0].text.setText("Restart")
