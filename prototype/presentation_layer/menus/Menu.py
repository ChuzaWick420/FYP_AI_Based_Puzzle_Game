from prototype.Presentation_Layer.TextElement import TextElement

class Menu:
    def __init__(self):
        color = (254, 197, 43)
        self.text = TextElement("Menu", color, (0, 0))
        self.text.setSize(48)
        self.buttons = []

    def render(self, display):
        display.blit(self.text.text, self.text.textRect)

        for button in self.buttons:
            button.render(display)
