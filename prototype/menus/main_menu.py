from prototype.data import Global
from prototype.entities.Button import Button
from prototype.entities.TextElement import TextElement
from prototype.menus.Menu import Menu

class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        starting_offset = 200
        gap = 50

        pos = (Global.WINDOW_RESOLUTION[0] // 2, starting_offset)

        self.text.updateText("Main Menu")

        self.text.setPosition((pos[0], pos[1] - 2 * gap))

        # Buttons
        self.buttons.append(Button("Play",              (pos[0], pos[1] + 0 * gap)))
        self.buttons.append(Button("Select Difficulty", (pos[0], pos[1] + 1 * gap)))
        self.buttons.append(Button("Score Board",       (pos[0], pos[1] + 2 * gap)))
        self.buttons.append(Button("Quit",              (pos[0], pos[1] + 3 * gap)))
