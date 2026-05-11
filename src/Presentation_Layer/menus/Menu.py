import pygame
from src.Presentation_Layer.TextElement import TextElement

class Menu:
    def __init__(self):
        color = (176, 228, 204)
        self.text = TextElement("Menu", color, (0, 0))
        self.text.setSize(48)
        self.buttons = []
        self.active_btn_id = 0

    def render(self, display):
        display.blit(self.text.text, self.text.textRect)

        for button in self.buttons:
            button.render(display)

    def handle_selection(self):
        stack_size = len(self.buttons)

        # NOTE: Wrapping the counter if out of bound.
        #       The counter is managed externally
        if self.active_btn_id < 0:
            self.active_btn_id = stack_size - 1
        else:
            self.active_btn_id = self.active_btn_id % stack_size

        index = 0

        for button in self.buttons:
            # Reset hover and selection flags
            button.setActiveFlag(False)
            button.setHoverFlag(False)

            if (button.isHovered()):
                self.active_btn_id = index
            index += 1

    def handle_hover(self):
        self.handle_selection()
        self.buttons[self.active_btn_id].setHoverFlag(True)

    def handle_trigger(self):
        self.handle_selection()
        self.buttons[self.active_btn_id].setActiveFlag(True)
