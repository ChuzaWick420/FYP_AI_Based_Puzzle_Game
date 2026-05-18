import pygame
from src.Data_Layer import Global
from src.Presentation_Layer.TextElement import TextElement

class Menu:
    def __init__(self):
        color = (176, 228, 204)
        self.text = TextElement("Menu", color, (0, 0))
        self.text.setSize(48)
        self.buttons = []
        self.active_btn_id = 0

    def render(self, display):
        self.text.render(display)

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

    def getActiveBtnID(self):
        return self.active_btn_id

    def setActiveBtnID(self, id):
        self.active_btn_id = id

    def stackButtons(self, h_reference = Global.WINDOW_RESOLUTION[0] // 2, v_reference = Global.WINDOW_RESOLUTION[1] // 2, gap = 50):

        index = 0

        for button in self.buttons:
            pos = (h_reference, v_reference + gap * index)
            button.setPosition(pos)
            index += 1
