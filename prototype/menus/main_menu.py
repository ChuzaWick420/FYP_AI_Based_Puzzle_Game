from prototype.entities.Button import Button
from prototype.entities.TextElement import TextElement

class MainMenu:
    def __init__(self):
        color = (200, 40, 70)
        pos = (450, 100)
        self.text = TextElement("Main Menu", color, pos)

        # Buttons
        self.testButton1 = Button("Play", (450, 250))
        self.testButton2 = Button("Quit", (450, 350))

        self.buttons = [
            self.testButton1,
            self.testButton2
        ]


    def render(self, display):
        display.blit(self.text.text, self.text.textRect)

        for button in self.buttons:
            button.render(display)
