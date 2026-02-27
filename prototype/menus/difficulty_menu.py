from prototype.entities.Button import Button
from prototype.menus.Menu import Menu

class DifficultyMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        self.text.updateText("Difficulty Menu")
        self.easy_button = Button("Easy", (450, 300))
        self.medium_button = Button("Medium", (450, 350))
        self.hard_button = Button("Hard", (450, 400))

        self.buttons.append(self.easy_button)
        self.buttons.append(self.medium_button)
        self.buttons.append(self.hard_button)
