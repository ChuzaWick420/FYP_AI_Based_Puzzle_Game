import pygame
from src.Data_Layer import Global
from src.Data_Layer.Colors import Colors
from src.Presentation_Layer.TextElement import TextElement

class Menu:
    def __init__(self):
        self._text = TextElement("Menu", Colors.MENU_TITLE, (0, 0))
        self._text.setSize(48)
        self._buttons = []
        self.__active_btn_id = 0

    def render(self, display):
        self._text.render(display)

        for button in self._buttons:
            button.render(display)

    def handleSelection(self):
        stack_size = len(self._buttons)

        # NOTE: Wrapping the counter if out of bound.
        #       The counter is managed externally
        if self.__active_btn_id < 0:
            self.__active_btn_id = stack_size - 1
        else:
            self.__active_btn_id = self.__active_btn_id % stack_size

        index = 0

        for button in self._buttons:
            # Reset hover and selection flags
            button.setActiveFlag(False)
            button.setHoverFlag(False)

            if (button.isHovered()):
                self.__active_btn_id = index
            index += 1

    def handleHover(self):
        self.handleSelection()
        self._buttons[self.__active_btn_id].setHoverFlag(True)

    def handleTrigger(self):
        self.handleSelection()
        self._buttons[self.__active_btn_id].setActiveFlag(True)

    def getActiveBtnID(self):
        return self.__active_btn_id

    def setActiveBtnID(self, id):
        self.__active_btn_id = id

    def stackButtons(self, h_reference = Global.WINDOW_RESOLUTION[0] // 2, v_reference = Global.WINDOW_RESOLUTION[1] // 2, gap = 50):

        index = 0

        for button in self._buttons:
            pos = (h_reference, v_reference + gap * index)
            button.setPosition(pos)
            index += 1

    def getButtons(self):
        return self._buttons
