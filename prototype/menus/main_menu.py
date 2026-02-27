from prototype.entities.Button import Button
from prototype.entities.TextElement import TextElement
from prototype.menus.Menu import Menu

class MainMenu(Menu):
    def __init__(self):

        # NOTE: defining a constructor in child override the parent constructor so we are manually calling the parent's constructor
        Menu.__init__(self) 

        # Buttons
        self.testButton1 = Button("Play", (450, 250))
        self.testButton2 = Button("Quit", (450, 350))

        self.text.updateText("Main Menu")
        self.buttons.append(self.testButton1)
        self.buttons.append(self.testButton2)


    def render(self, display):
        display.blit(self.text.text, self.text.textRect)

        for button in self.buttons:
            button.render(display)
