from prototype.entities.Button import Button
from prototype.menus.Menu import Menu
from prototype.data import Global

class ResultMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        starting_offset = 200
        gap = 50

        pos = (Global.WINDOW_RESOLUTION[0] // 2, starting_offset)

        self.text.updateText("Result Menu", )
        self.text.setPosition((pos[0], pos[1] - 2 * gap))

        self.buttons.append(Button("Next Level", (pos[0], pos[1] + 0 * gap)))
        self.buttons.append(Button("Scoreboard", (pos[0], pos[1] + 1 * gap)))
        self.buttons.append(Button("Home",       (pos[0], pos[1] + 2 * gap)))

