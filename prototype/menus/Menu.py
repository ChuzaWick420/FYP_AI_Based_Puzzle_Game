from prototype.entities.Button import Button
from prototype.entities.TextElement import TextElement

class Menu:
    def __init__(self):
        color = (254, 197, 43)
        pos = (450, 100)
        self.text = TextElement("Menu", color, pos)
        self.buttons = []

    def render(self, display):
        display.blit(self.text.text, self.text.textRect)

        for button in self.buttons:
            button.render(display)
