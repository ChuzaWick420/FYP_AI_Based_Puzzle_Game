from src.Data_Layer.ButtonType import ButtonType
from src.Data_Layer.StateInputs import StateInputs
from src.Presentation_Layer.menus.Menu import Menu
from src.Data_Layer import Global
from src.Presentation_Layer.Button import Button

class DifficultyMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        self.text.setText("Difficulty Menu")
        self.text.setPosition(Global.MENU_TITLE_POS)

        self.buttons.append(Button("Easy",   StateInputs.DIFFICULTY_EASY))
        self.buttons.append(Button("Medium", StateInputs.DIFFICULTY_MEDIUM))
        self.buttons.append(Button("Hard",   StateInputs.DIFFICULTY_HARD))

        for button in self.buttons:
            button.setType(ButtonType.TEXTUAL)

        self.stackButtons()
