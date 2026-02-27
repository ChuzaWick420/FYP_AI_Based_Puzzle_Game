from prototype.entities.Button import Button
from prototype.entities.TextElement import TextElement

class Menu:
    def __init__(self):
        color = (200, 40, 70)
        pos = (450, 100)
        self.text = TextElement("Menu", color, pos)
        self.buttons = []
