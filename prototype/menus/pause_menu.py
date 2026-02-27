from prototype.entities.Button import Button
from prototype.menus.Menu import Menu

class PauseMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        self.text.updateText("Pause Menu")
        self.resume = Button("Resume", (450, 300))
        self.restart = Button("Restart", (450, 350))
        self.quit = Button("Quit", (450, 400))

        self.buttons.append(self.resume)
        self.buttons.append(self.restart)
        self.buttons.append(self.quit)
