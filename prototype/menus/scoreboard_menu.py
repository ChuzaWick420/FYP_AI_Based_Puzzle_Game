from prototype.entities.Button import Button
from prototype.menus.Menu import Menu

class ScoreBoardMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        self.text.updateText("Score Board Menu")
        self.back= Button("Home", (450, 300))

        self.buttons.append(self.back)
