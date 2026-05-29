from src.Data_Layer import Global
from src.Data_Layer.ButtonType import ButtonType
from src.Data_Layer.StateInputs import StateInputs
from src.Presentation_Layer.Button import Button
from src.Presentation_Layer.menus.Menu import Menu

class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        self._text.setText("Memory Maze - Human vs AI Pathfinding Game")
        self._text.setPosition(Global.MENU_TITLE_POS)

        # Buttons
        self._buttons.append(Button("Play",              StateInputs.PLAY))
        self._buttons.append(Button("Select Difficulty", StateInputs.DIFFICULTY_SELECTION))
        self._buttons.append(Button("Scoreboard",        StateInputs.SCORE_BOARD))
        self._buttons.append(Button("Quit",              StateInputs.EXIT))

        for button in self._buttons:
            button.setType(ButtonType.TEXTUAL)

        self.stackButtons()
