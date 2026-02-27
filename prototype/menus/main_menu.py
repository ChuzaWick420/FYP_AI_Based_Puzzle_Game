from prototype.entities.Button import Button
from prototype.entities.TextElement import TextElement
from prototype.menus.Menu import Menu

class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        # Buttons
        self.testButton1 = Button("Play", (450, 250))
        self.testButton2 = Button("Select Difficulty", (450, 300))
        self.testButton3 = Button("Score Board", (450, 350))
        self.testButton4 = Button("Quit", (450, 400))

        self.text.updateText("Main Menu")
        self.buttons.append(self.testButton1)
        self.buttons.append(self.testButton2)
        self.buttons.append(self.testButton3)
        self.buttons.append(self.testButton4)
