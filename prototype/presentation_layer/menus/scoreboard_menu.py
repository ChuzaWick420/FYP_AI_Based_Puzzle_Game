from prototype.Domain_Logic_Layer.entities.Button import Button
from prototype.Presentation_Layer.menus.Menu import Menu
from prototype.Data_Layer import Global

class ScoreBoardMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        starting_offset = 200
        gap = 50

        pos = (Global.WINDOW_RESOLUTION[0] // 2, starting_offset)

        self.text.updateText("Score Board Menu")
        self.text.setPosition((pos[0], pos[1] - 2 * gap))

        self.buttons.append(Button("Home",  (pos[0], pos[1] + 0 * gap)))

