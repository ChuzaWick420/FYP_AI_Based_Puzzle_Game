from src.Data_Layer.ButtonType import ButtonType
from src.Presentation_Layer.TextElement import TextElement
from src.Presentation_Layer.menus.Menu import Menu
from src.Data_Layer import Global
from src.Presentation_Layer.Button import Button

class ResultMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        starting_offset = 200
        gap = 50

        pos = (Global.WINDOW_RESOLUTION[0] // 2, starting_offset)

        self.text.setText("Result Menu")
        self.text.setPosition((pos[0], pos[1] - 3 * gap))

        # Extras
        color = (254, 197, 43)
        self.winner_info = TextElement("You Win!", color, (pos[0], pos[1] - 2 * gap))
        self.completion_time = TextElement("Timer:", color, (pos[0], pos[1] - 1 * gap))

        self.buttons.append(Button("Restart Level", (pos[0], pos[1] + 0 * gap)))
        self.buttons.append(Button("Scoreboard", (pos[0], pos[1] + 1 * gap)))
        self.buttons.append(Button("Home",       (pos[0], pos[1] + 2 * gap)))

        for button in self.buttons:
            button.setType(ButtonType.TEXTUAL)

    def render(self, display):
        display.blit(self.text.text, self.text.textRect)
        display.blit(self.winner_info.text, self.winner_info.textRect)
        display.blit(self.completion_time.text, self.completion_time.textRect)

        for button in self.buttons:
            button.render(display)

    def setTimer(self, minutes, seconds):
        self.completion_time.setText("Timer: {0:02}:{1:02}".format(minutes // 60, seconds % 60))
