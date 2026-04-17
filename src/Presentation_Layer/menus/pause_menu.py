from src.Presentation_Layer.menus.Menu import Menu
from src.Data_Layer import Global
from src.Presentation_Layer.Button import Button

class PauseMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        starting_offset = 200
        gap = 50

        pos = (Global.WINDOW_RESOLUTION[0] // 2, starting_offset)

        self.text.setText("Pause Menu")
        self.text.setPosition((pos[0], pos[1] - 2 * gap))

        self.buttons.append(Button("Resume",  (pos[0], pos[1] + 0 * gap)))
        self.buttons.append(Button("Restart", (pos[0], pos[1] + 1 * gap)))
        self.buttons.append(Button("Home",    (pos[0], pos[1] + 2 * gap)))

