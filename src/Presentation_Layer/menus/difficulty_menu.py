from src.Data_Layer.ButtonType import ButtonType
from src.Data_Layer.StateInputs import StateInputs
from src.Presentation_Layer.menus.Menu import Menu
from src.Data_Layer import Global
from src.Presentation_Layer.Button import Button

class DifficultyMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        starting_offset = 200
        gap = 50

        pos = (Global.WINDOW_RESOLUTION[0] // 2, starting_offset)

        self.text.setText("Difficulty Menu")
        self.text.setPosition((pos[0], pos[1] - 2 * gap))

        self.buttons.append(Button("Easy",   StateInputs.DIFFICULTY_EASY,   (pos[0], pos[1] + 0 * gap)))
        self.buttons.append(Button("Medium", StateInputs.DIFFICULTY_MEDIUM, (pos[0], pos[1] + 1 * gap)))
        self.buttons.append(Button("Hard",   StateInputs.DIFFICULTY_HARD,   (pos[0], pos[1] + 2 * gap)))

        for button in self.buttons:
            button.setType(ButtonType.TEXTUAL)
