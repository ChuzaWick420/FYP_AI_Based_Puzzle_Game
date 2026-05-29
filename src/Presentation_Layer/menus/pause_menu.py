from src.Data_Layer.ButtonType import ButtonType
from src.Data_Layer.StateInputs import StateInputs
from src.Presentation_Layer.menus.Menu import Menu
from src.Data_Layer import Global
from src.Presentation_Layer.Button import Button

class PauseMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        self._text.setText("Pause Menu")
        self._text.setPosition(Global.MENU_TITLE_POS)

        self._buttons.append(Button("Resume",  StateInputs.RESUME))
        self._buttons.append(Button("Restart", StateInputs.RESTART))
        self._buttons.append(Button("Home",    StateInputs.EXIT))

        for button in self._buttons:
            button.setType(ButtonType.TEXTUAL)

        self.stackButtons()
