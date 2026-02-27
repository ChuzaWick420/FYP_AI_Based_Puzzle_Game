from prototype.entities.Button import Button
from prototype.menus.Menu import Menu

class ResultMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        self.text.updateText("Result Menu")
        self.next_level = Button("Next Level", (450, 300))
        self.scoreboard = Button("Scoreboard", (450, 350))
        self.quit = Button("Quit", (450, 400))

        self.buttons.append(self.next_level)
        self.buttons.append(self.scoreboard)
        self.buttons.append(self.quit)
